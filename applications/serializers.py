from rest_framework import serializers

from .models import Application


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = (
            "id",
            "job",
            "candidate",
            "cover_letter",
            "status",
            "applied_at",
            "updated_at",
        )
        read_only_fields = (
            "id",
            "candidate",
            "status",
            "applied_at",
            "updated_at",
        )