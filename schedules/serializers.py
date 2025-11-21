from rest_framework import serializers
from .models import Schedule


class ScheduleSerializer(serializers.ModelSerializer):
    professional_name = serializers.CharField(source='professional.name', read_only=True)

    class Meta:
        model = Schedule
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

