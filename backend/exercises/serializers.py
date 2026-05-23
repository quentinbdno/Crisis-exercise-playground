from rest_framework import serializers

from exercises.models import Exercise, ExerciseRoom, StimulusDelivery


class ExerciseRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseRoom
        fields = "__all__"


class StimulusDeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = StimulusDelivery
        fields = "__all__"


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = "__all__"
