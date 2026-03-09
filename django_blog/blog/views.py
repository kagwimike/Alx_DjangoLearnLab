from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q
from django.utils import timezone
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from taggit.models import Tag
from .models import Post, Comment
from .forms import RegisterForm, ProfileUpdateForm, CommentForm

# DRF Imports
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from .serializers import PostSerializer, CommentSerializer

# ---------------------------------------------------------
# 1. TEMPLATE VIEWS (Standard Django HTML)
# ---------------------------------------------------------

def home(request):
    return render(request, "blog/base.html")

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect("profile")
    else:
        form = RegisterForm()
    return render(request, "blog/register.html", {"form": form})


def search_posts(request):
    query = request.GET.get("q")
    results = []

    if query:
        results = Post.objects.filter(title__icontains=query)

    return render(request, "blog/search_results.html", {
        "query": query,
        "results": results
    })


@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect("profile")
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, "blog/profile.html", {"form": form})

# Post Views
class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    ordering = ["-created_at"]

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content", "tags"]
    template_name = "blog/post_form.html"
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.published_date = timezone.now()
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "content", "tags"]
    template_name = "blog/post_form.html"
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        return self.request.user == self.get_object().author

class PostByTagListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    def get_queryset(self):
        self.tag = get_object_or_404(Tag, slug=self.kwargs["tag_slug"])
        return Post.objects.filter(tags__in=[self.tag])
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag"] = self.tag
        return context

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("post-list")
    def test_func(self):
        return self.request.user == self.get_object().author

# Comment Views (HTML)
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/comment_form.html"
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(Post, pk=self.kwargs["pk"])
        return super().form_valid(form)
    def get_success_url(self):
        return self.object.post.get_absolute_url()

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/comment_form.html"
    def test_func(self):
        return self.request.user == self.get_object().author
    def get_success_url(self):
        return self.object.post.get_absolute_url()

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = "blog/comment_confirm_delete.html"
    def test_func(self):
        return self.request.user == self.get_object().author
    def get_success_url(self):
        return self.object.post.get_absolute_url()

# ---------------------------------------------------------
# 2. API VIEWS (React Frontend)
# ---------------------------------------------------------
# ---------------------------------------------------------
# 2. API VIEWS (React Frontend)
# ---------------------------------------------------------

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def user_profile_api(request):
    user = request.user

    post_count = Post.objects.filter(author=user).count()
    comment_count = Comment.objects.filter(author=user).count()

    return Response({
        "username": user.username,
        "post_count": post_count,
        "comment_count": comment_count,
        "date_joined": user.date_joined
    })


# -------------------------
# Register
# -------------------------

class RegisterAPI(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")

        if not username or not password:
            return Response({"error": "Username and password required"}, status=400)

        if User.objects.filter(username=username).exists():
            return Response({"error": "User already exists"}, status=400)

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return Response({
            "message": "User created",
            "username": user.username
        }, status=201)


# -------------------------
# Posts
# -------------------------

class PostListAPI(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            published_date=timezone.now()
        )


class PostDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        if self.request.user != self.get_object().author:
            raise PermissionError("You cannot edit this post")
        serializer.save()

    def perform_destroy(self, instance):
        if self.request.user != instance.author:
            raise PermissionError("You cannot delete this post")
        instance.delete()


# -------------------------
# Comments
# -------------------------

class CommentCreateAPI(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        post_id = self.request.data.get("post")
        post = get_object_or_404(Post, id=post_id)

        serializer.save(
            author=self.request.user,
            post=post
        )


class CommentDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        if self.request.user != self.get_object().author:
            raise PermissionError("You cannot edit this comment")
        serializer.save()

    def perform_destroy(self, instance):
        if self.request.user != instance.author:
            raise PermissionError("You cannot delete this comment")
        instance.delete()


# -------------------------
# Comment Upvote
# -------------------------

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def comment_upvote(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if comment.author == request.user:
        return Response({"error": "You cannot upvote your own comment"}, status=400)

    comment.upvotes = (comment.upvotes or 0) + 1
    comment.save()

    return Response({"upvotes": comment.upvotes})


# -------------------------
# Post Upvote
# -------------------------

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def upvote_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    post.upvotes = (post.upvotes or 0) + 1
    post.save()

    return Response({"upvotes": post.upvotes})