from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .validators import validate_signup
from .serializers import UserSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework.exceptions import APIException


class SignupView(APIView):
    def post(self, request):
        is_valid, err_msg_list = validate_signup(request.data)
        if not is_valid:
            return Response({'error': err_msg_list}, status=400)
        
        user = User.objects.create_user(
            # **request.data
            username = request.data.get('username'),
            password = request.data.get('password'),
            nickname = request.data.get('nickname'),
            birth = request.data.get('birth'),
            first_name = request.data.get('first_name'),
            last_name = request.data.get('last_name'),
            email = request.data.get('email'),
        )
        serializer = UserSerializer(user)
        res_data = serializer.data
        #token
        refresh = RefreshToken.for_user(user)
        refresh_token = str(refresh)
        access_token = str(refresh.access_token)
        res_data["tokens"] = {
            "access": access_token,
            "refresh": refresh_token
        }
        return Response(res_data)

class SigninView(APIView):
    def post(self, request):
        username=request.data.get('username')
        password=request.data.get('password')
        user=authenticate(username=username, password=password)
        
        if not user:
            return Response({'error': '아이디 또는 비밀번호가 일치하지 않습니다.'}, status=400)

        serializer=UserSerializer(user)
        res_data = serializer.data
        
        #token
        refresh = RefreshToken.for_user(user)
        refresh_token = str(refresh)
        access_token = str(refresh.access_token)
        res_data["tokens"] = {
            "access": access_token,
            "refresh": refresh_token
        }
        # res_data['access_token'] = access_token
        # res_data['refresh_token'] = refresh_token
        return Response(res_data)

class SignoutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            refresh_token_str = request.data.get('refresh_token')
            if not refresh_token_str:
                return Response({'error': 'Refresh token is required'}, status=400)
            
            refresh_token = RefreshToken(refresh_token_str)            
            refresh_token.blacklist()
            
            return Response({'message': 'Successfully logged out'}, status=200)
        except TokenError as e:
            raise APIException(f"Token is invalid or expired: {e}")
        except Exception as e:
            raise APIException(f"An unexpected error occurred: {e}")

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, username):
        user = User.objects.get(username=username)
        serializer = UserSerializer(user)
        return Response(serializer.data)