from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import UserProfile
from .serializers import UserSerializer, UserProfileSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar usuarios
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]  # Cambiar según necesidades
    
    @action(detail=False, methods=['get'])
    def me(self, request):
        """Obtener información del usuario actual"""
        if request.user.is_authenticated:
            serializer = self.get_serializer(request.user)
            return Response(serializer.data)
        return Response({'detail': 'No autenticado'}, status=status.HTTP_401_UNAUTHORIZED)
    
    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def login(self, request):
        """Login de usuario con email o username"""
        username_or_email = request.data.get('username') or request.data.get('email')
        password = request.data.get('password')
        
        if not username_or_email or not password:
            return Response(
                {'detail': 'Email/Usuario y contraseña son requeridos'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Intentar autenticar primero con username
        user = authenticate(request, username=username_or_email, password=password)
        
        # Si falla, intentar buscar por email
        if user is None:
            try:
                user_obj = User.objects.get(email=username_or_email)
                user = authenticate(request, username=user_obj.username, password=password)
            except User.DoesNotExist:
                pass
        
        if user is not None:
            login(request, user)
            serializer = self.get_serializer(user)
            return Response({
                'user': serializer.data,
                'message': 'Login exitoso'
            })
        else:
            return Response(
                {'detail': 'Credenciales inválidas'},
                status=status.HTTP_401_UNAUTHORIZED
            )
    
    @action(detail=False, methods=['post'])
    def logout(self, request):
        """Logout de usuario"""
        logout(request)
        return Response({'message': 'Logout exitoso'})

