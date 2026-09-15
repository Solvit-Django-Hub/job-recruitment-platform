from django.contrib import admin

from .models import Application


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = (
        "job",
        "candidate",
        "status",
        "applied_at",
        "updated_at",
    )
    list_filter = ("status",)
    search_fields = (
        "job__title",
        "candidate__user__username",
        "candidate__user__email",
    )