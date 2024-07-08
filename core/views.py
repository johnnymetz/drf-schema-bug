from rest_framework.viewsets import ModelViewSet

from core.models import Team
from core.serializers import TeamSerializer


class TeamView(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
