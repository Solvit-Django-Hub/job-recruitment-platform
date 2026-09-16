from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import CandidateProfile
from .serializers import CandidateProfileSerializer


class CandidateProfileListCreateView(generics.ListCreateAPIView):
    queryset = CandidateProfile.objects.all()
    serializer_class = CandidateProfileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CandidateProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CandidateProfile.objects.all()
    serializer_class = CandidateProfileSerializer
    permission_classes = [IsAuthenticated]