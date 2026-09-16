from django.urls import path

from .views import (
    CandidateProfileDetailView,
    CandidateProfileListCreateView,
)


urlpatterns = [
    path(
        "",
        CandidateProfileListCreateView.as_view(),
        name="profile-list-create",
    ),
    path(
        "<int:pk>/",
        CandidateProfileDetailView.as_view(),
        name="profile-detail",
    ),
]