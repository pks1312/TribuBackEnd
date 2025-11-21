from rest_framework import serializers
from .models import Professional


class ProfessionalSerializer(serializers.ModelSerializer):
    specialties_list = serializers.SerializerMethodField()

    class Meta:
        model = Professional
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

    def get_specialties_list(self, obj):
        if obj.specialties:
            return [s.strip() for s in obj.specialties.split(',')]
        return []

