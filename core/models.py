from django.db import models


class Team(models.Model):
    class Color(models.TextChoices):
        RED = "Red"
        GREEN = "Green"
        BLUE = "Blue"

    name = models.CharField(max_length=255)

    color = models.CharField(
        max_length=20,
        choices=Color,
        default=Color.RED,
        # Color.default only shows up in the schema if color has a database index
        db_index=True,
        help_text="The team's color",
    )
