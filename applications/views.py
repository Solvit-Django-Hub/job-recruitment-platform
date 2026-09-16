from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from accounts.permissions import IsCompany

from .models import Application
from .serializers import (
    ApplicationSerializer,
    CompanyApplicationSerializer,
)


class ApplicationListCreateView(generics.ListCreateAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Application.objects.filter(
            candidate__user=self.request.user
        )

    def perform_create(self, serializer):
        candidate = self.request.user.candidate_profile
        serializer.save(candidate=candidate)


class ApplicationDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Application.objects.filter(
            candidate__user=self.request.user
        )


class CompanyApplicationListView(generics.ListAPIView):
    serializer_class = CompanyApplicationSerializer
    permission_classes = [IsAuthenticated, IsCompany]

    def get_queryset(self):
        return Application.objects.filter(
            job__company__owner=self.request.user
        )


class CompanyApplicationDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = CompanyApplicationSerializer
    permission_classes = [IsAuthenticated, IsCompany]

    def get_queryset(self):
        return Application.objects.filter(
            job__company__owner=self.request.user
        )