from rest_framework import serializers
from .models import GalleryImage


class GalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = ['id', 'title', 'description', 'image_url', 'category', 'is_active', 'created_at', 'updated_at']
        read_only_fields = ('created_at', 'updated_at')

