from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from accounts.views import AuthViewSet, UserViewSet
from ai_agents.views import AIAgentViewSet, LLMConnectorViewSet
from audit.views import AuditLogViewSet
from exercises.views import ExerciseViewSet
from iam.views import CrisisCellViewSet, PermissionViewSet, RoleViewSet
from media_library.views import AttachmentViewSet
from messaging.views import ChannelViewSet, MessageViewSet
from scenarios.views import ScenarioViewSet
from stimuli.views import StimulusViewSet

router = DefaultRouter()
router.register("auth", AuthViewSet, basename="auth")
router.register("users", UserViewSet)
router.register("roles", RoleViewSet)
router.register("permissions", PermissionViewSet)
router.register("crisis-cells", CrisisCellViewSet)
router.register("scenarios", ScenarioViewSet)
router.register("stimuli", StimulusViewSet)
router.register("exercises", ExerciseViewSet)
router.register("channels", ChannelViewSet)
router.register("messages", MessageViewSet)
router.register("attachments", AttachmentViewSet)
router.register("ai-agents", AIAgentViewSet)
router.register("llm-connectors", LLMConnectorViewSet)
router.register("audit-logs", AuditLogViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
