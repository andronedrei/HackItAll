from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User


class RegisterView(APIView):
    """
    API view to handle user registration
    """
    def post(self, request):
        """
        Handle POST request to register a new user
        """
        # Get data from request
        email = request.data.get('email')
        password = request.data.get('password')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')

        if not email or not password or not first_name or not last_name:
            return Response(
                {"error": "All fields are required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Create user
        try:
            user = User.objects.create_user(
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )
            return Response(
                {"message": "User created successfully!"},
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

class LoginView(APIView):
    permission_classes = [AllowAny]  # Allow anyone to access the login view

    def post(self, request):
        email = request.data.get('email')  # Use email instead of username
        password = request.data.get('password')

        # Authenticate the user using email and password
        user = authenticate(request, email=email, password=password)

        if user is not None:
            # Log the user in (creates a session)
            login(request, user)
            return JsonResponse({'message': 'Login successful!'}, status=200)
        else:
            return JsonResponse({'error': 'Invalid email or password'}, status=401)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"message": "Logged out successfully!"})


class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Since we're using email as the username, we refer to it here
        return Response({"message": f"Welcome, {request.user.email}!"})


class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": f"Welcome, {request.user.username}!"})


class HelloView(APIView):
    permission_classes = [AllowAny]  # Allow anyone to access the login view

    def get(self, request):
        return Response({'message': 'Hello, world!'})

