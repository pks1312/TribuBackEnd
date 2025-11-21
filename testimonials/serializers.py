from rest_framework import serializers
from .models import Testimonial


class TestimonialSerializer(serializers.ModelSerializer):
    service_name = serializers.CharField(source='service.name', read_only=True)

    class Meta:
        model = Testimonial
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'is_approved')

