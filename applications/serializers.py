from django.utils import timezone
from rest_framework import serializers

from .models import Application
from jobs.models import Job


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

    def validate_job(self, job):
        if not job.is_active:
            raise serializers.ValidationError(
                "This job is no longer active."
            )

        if job.application_deadline < timezone.now():
            raise serializers.ValidationError(
                "The application deadline has passed."
            )

        return job

    def validate(self, attrs):
        request = self.context.get("request")

        if request and request.user.is_authenticated:
            candidate = getattr(
                request.user,
                "candidate_profile",
                None,
            )

            if candidate:
                exists = Application.objects.filter(
                    job=attrs["job"],
                    candidate=candidate,
                ).exists()

                if exists:
                    raise serializers.ValidationError(
                        "You have already applied for this job."
                    )

        return attrs


class CompanyApplicationSerializer(serializers.ModelSerializer):
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
            "job",
            "candidate",
            "cover_letter",
            "applied_at",
            "updated_at",
        )

    def validate_status(self, value):
        valid_statuses = dict(Application.Status.choices)

        if value not in valid_statuses:
            raise serializers.ValidationError(
                "Invalid application status."
            )

        return value