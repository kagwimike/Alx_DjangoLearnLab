from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager


class Post(models.Model):

    title = models.CharField(max_length=200)
    content = models.TextField()
    upvotes = models.IntegerField(default=0)

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts"
    )

    published_date = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    tags = TaggableManager(blank=True)

    class Meta:
        ordering = ["-published_date"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})


class Comment(models.Model):

    post = models.ForeignKey(
        Post,
        related_name="comments",
        on_delete=models.CASCADE
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments"
    )

    # NEW: reply support
    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        related_name="replies",
        on_delete=models.CASCADE
    )

    content = models.TextField()

    # NEW: Reddit-style upvotes
    upvotes = models.ManyToManyField(
        User,
        related_name="upvoted_comments",
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"{self.author.username} on {self.post.title}"

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.post.pk})

    # NEW: count upvotes
    def upvote_count(self):
        return self.upvotes.count()