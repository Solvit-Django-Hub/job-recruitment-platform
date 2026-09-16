from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Job
from .serializers import JobSerializer


class JobListCreateView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]

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