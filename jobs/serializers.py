from django.utils import timezone
from rest_framework import serializers

from .models import Job


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = (
            "id",
            "company",
            "title",
            "description",
            "requirements",
            "location",
            "employment_type",
            "salary",
            "application_deadline",
            "is_active",
            "created_at",
            "updated_at",
        )
        read_only_fields = (
            "id",
            "company",
            "created_at",
            "updated_at",
        )

    def validate_application_deadline(self, value):
        if value <= timezone.now():
            raise serializers.ValidationError(
                "Application deadline must be in the future."
            )

        return value