from django.urls import path

from .views import (
    ApplicationDetailView,
    ApplicationListCreateView,
    CompanyApplicationDetailView,
    CompanyApplicationListView,
)


urlpatterns = [
    path(
        "",
        ApplicationListCreateView.as_view(),
        name="application-list-create",
    ),
    path(
        "<int:pk>/",
        ApplicationDetailView.as_view(),
        name="application-detail",
    ),
    path(
        "company/",
        CompanyApplicationListView.as_view(),
        name="company-application-list",
    ),
    path(
        "company/<int:pk>/",
        CompanyApplicationDetailView.as_view(),
        name="company-application-detail",
    ),
]