def audit(action, actor=None, resource=None, exercise=None, scenario=None, metadata=None):
    from audit.models import AuditLog

    return AuditLog.objects.create(
        actor=actor if getattr(actor, "is_authenticated", False) else None,
        action=action,
        resource_type=resource.__class__.__name__ if resource else "",
        resource_id=str(getattr(resource, "pk", "")) if resource else "",
        exercise=exercise,
        scenario=scenario,
        metadata=metadata or {},
    )
