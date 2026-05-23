from django.contrib import admin

from exercises.models import Exercise, ExerciseRoom, StimulusDelivery

admin.site.register(Exercise)
admin.site.register(ExerciseRoom)
admin.site.register(StimulusDelivery)
