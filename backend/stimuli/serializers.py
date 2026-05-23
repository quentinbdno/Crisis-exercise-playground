from rest_framework import serializers

from stimuli.models import Stimulus


class StimulusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stimulus
        fields = "__all__"
