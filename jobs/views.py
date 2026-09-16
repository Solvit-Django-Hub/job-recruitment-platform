from rest_framework import filters, generics
from rest_framework.permissions import IsAuthenticated

from .models import Job
from .serializers import JobSerializer


class JobListCreateView(generics.ListCreateAPIView):
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    search_fields = [
        "title",
        "description",
        "requirements",
        "location",
        "employment_type",
        "company__name",
    ]

    ordering_fields = [
        "created_at",
        "salary",
        "application_deadline",
    ]

    ordering = ["-created_at"]

    def get_queryset(self):
        return Job.objects.filter(is_active=True)

    def perform_create(self, serializer):
        company = self.request.user.company
        serializer.save(company=company)


class JobDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Job.objects.filter(
            company__owner=self.request.user
        )