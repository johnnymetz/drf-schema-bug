from core.models import Team

Team.objects.all().delete()

for i in range(3):
    Team.objects.create(name=f"Team {i}")


def run():
    print("Done.")
