from core.models import Team
import pytest


@pytest.mark.django_db
class TestTeam:
    def test_get_teams(self, client):
        team1 = Team.objects.create(name="Team 1")
        team2 = Team.objects.create(name="Team 2")

        response = client.get("/teams/")
        assert response.status_code == 200
        assert len(response.data) == 2
        assert {team["id"] for team in response.data} == {x.id for x in [team1, team2]}

    def test_create_team(self, client):
        name = "My Team"
        response = client.post("/teams/", {"name": name})
        assert response.status_code == 201
        assert Team.objects.count() == 1

        team = Team.objects.get()
        assert team.id == response.data["id"]
        assert team.name == name
        assert team.color == Team.Color.RED
