from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
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

