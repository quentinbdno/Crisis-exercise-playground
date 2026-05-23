from django.urls import path

from messaging.consumers import ExerciseConsumer

websocket_urlpatterns = [
    path("ws/exercises/<int:exercise_id>/", ExerciseConsumer.as_asgi()),
]
