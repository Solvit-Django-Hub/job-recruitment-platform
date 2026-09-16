from rest_framework import serializers

from .models import CandidateProfile


class CandidateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateProfile
        fields = (
            "id",
            "user",
            "bio",
            "phone",
            "location",
            "skills",
            "education",
            "experience",
            "resume",
            "created_at",
            "updated_at",
        )
        read_only_fields = (
            "id",
            "user",
            "created_at",
            "updated_at",
        )