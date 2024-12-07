# accounts/views.py
from django.contrib.auth import authenticate
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Profile
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer, ProfileSerializer
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        # Deserialize and validate the user data
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  # Save the user object

            # Create or update the user's profile
            profile_data = {
                'user': user.id,  # Assign the user
                'firstName': request.data.get('firstName', ''),
                'lastName': request.data.get('lastName', ''),
                'email': request.data.get('email', ''),
                'age': request.data.get('age', 0),
                'phone': request.data.get('phone', ''),
                'dateOfBirth': request.data.get('dateOfBirth', None),
                'nationalityCountry': request.data.get('nationalityCountry', ''),
                'nationalityCity': request.data.get('nationalityCity', ''),
                'residenceCountry': request.data.get('residenceCountry', ''),
                'residenceCity': request.data.get('residenceCity', ''),
                'profilePicture': request.data.get('profilePicture', ''),
                'latitude': request.data.get('latitude', 0.0),
                'longitude': request.data.get('longitude', 0.0),
            }

            # Create or update the profile
            profile, created = Profile.objects.update_or_create(user=user, defaults=profile_data)

            # Serialize the user and profile data to return in the response
            user_serializer = UserSerializer(user)
            profile_serializer = ProfileSerializer(profile)

            return Response({
                'user': user_serializer.data,
                'profile': profile_serializer.data,
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            # Authenticate the user
            user = authenticate(
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password']
            )
            if user is not None:
                # Generate the token
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)
                return Response(
                    {'message': 'Login successful', 'access_token': access_token},
                    status=status.HTTP_200_OK
                )
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileCreateUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.profile  # Ensure we're dealing with the current user's profile