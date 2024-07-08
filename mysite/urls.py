from django.urls import include, path

from rest_framework.schemas import get_schema_view

urlpatterns = [
    path("", include("core.urls")),
    path("openapi/", get_schema_view()),
]
