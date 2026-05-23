from celery import shared_task
from django.utils import timezone


@shared_task
def deliver_stimulus(delivery_id):
    from audit.services import audit
    from exercises.models import StimulusDelivery

    delivery = StimulusDelivery.objects.select_related("exercise", "stimulus").get(pk=delivery_id)
    delivery.status = StimulusDelivery.Status.DELIVERED
    delivery.delivered_at = timezone.now()
    delivery.save(update_fields=["status", "delivered_at"])
    audit("stimulus.delivered", resource=delivery.stimulus, exercise=delivery.exercise, scenario=delivery.exercise.scenario)
    return delivery.id


@shared_task
def run_ai_agent(agent_id, exercise_id, prompt):
    from audit.services import audit
    from ai_agents.models import AIAgent
    from exercises.models import Exercise

    agent = AIAgent.objects.get(pk=agent_id)
    exercise = Exercise.objects.get(pk=exercise_id)
    audit("ai_agent.prompt_queued", resource=agent, exercise=exercise, scenario=exercise.scenario, metadata={"prompt": prompt[:500]})
    return {"agent_id": agent.id, "status": "queued"}
