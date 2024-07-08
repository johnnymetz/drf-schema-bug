from django.urls import path

from core.views import TeamView

urlpatterns = [
    path("teams/", TeamView.as_view({"get": "list", "post": "create"})),
]
