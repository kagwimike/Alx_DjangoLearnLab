from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import RegisterSerializer, LoginSerializer
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            return Response({'message':'User registered successfully'})
        return Response(serializer.errors)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            return Response(serializer.validated_data)
        return Response(serializer.errors)


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            'username': user.username,
            'email': user.email,
            'bio': user.bio
        })
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_user(request, user_id):

    User = get_user_model()

    try:
        user_to_follow = User.objects.get(id=user_id)

        if request.user == user_to_follow:
            return Response({"error":"You cannot follow yourself"})

        request.user.following.add(user_to_follow)

        return Response({"message":"User followed successfully"})

    except User.DoesNotExist:
        return Response({"error":"User not found"})   
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unfollow_user(request, user_id):

    User = get_user_model()

    try:
        user_to_unfollow = User.objects.get(id=user_id)

        request.user.following.remove(user_to_unfollow)

        return Response({"message":"User unfollowed successfully"})

    except User.DoesNotExist:
        return Response({"error":"User not found"})   