from rest_framework import serializers

from core.models import Team


class TeamSerializer(serializers.ModelSerializer):
    # Note: This changes:
    #
    #   default: !!python/object/apply:core.models.Color
    #   - Red
    #
    # to:
    #
    #  default: Red
    #
    # color = serializers.ChoiceField(choices=Team.Color.choices, default=Team.Color.RED.value)

    class Meta:
        model = Team
        fields = "__all__"
