# Generated by Django 5.0.6 on 2024-07-08 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Team",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                (
                    "color",
                    models.CharField(
                        choices=[("Red", "Red"), ("Green", "Green"), ("Blue", "Blue")],
                        default="Red",
                        help_text="The team's color",
                        max_length=20,
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="team",
            constraint=models.UniqueConstraint(
                fields=("name", "color"), name="uniq_tag_name_color"
            ),
        ),
    ]
