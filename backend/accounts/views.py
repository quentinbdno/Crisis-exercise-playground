import pyotp
from django.contrib.auth import login, logout
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from accounts.models import User
from accounts.serializers import LoginSerializer, UserSerializer
from audit.services import audit


class AuthViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    @action(detail=False, methods=["post"])
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        if user.mfa_enabled:
            return Response({"mfa_required": True, "user_id": user.id})
        login(request, user)
        audit("auth.login", actor=user)
        return Response(UserSerializer(user).data)

    @action(detail=False, methods=["post"], permission_classes=[IsAuthenticated])
    def logout(self, request):
        audit("auth.logout", actor=request.user)
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=["post"], permission_classes=[IsAuthenticated])
    def mfa_setup(self, request):
        secret = pyotp.random_base32()
        request.user.mfa_secret = secret
        request.user.save(update_fields=["mfa_secret"])
        uri = pyotp.totp.TOTP(secret).provisioning_uri(name=request.user.email, issuer_name="Crisis Exercise")
        audit("auth.mfa_setup_started", actor=request.user)
        return Response({"secret": secret, "provisioning_uri": uri})

    @action(detail=False, methods=["post"])
    def mfa_verify(self, request):
        user = User.objects.get(pk=request.data.get("user_id"))
        token = request.data.get("token", "")
        if pyotp.TOTP(user.mfa_secret).verify(token):
            user.mfa_enabled = True
            user.save(update_fields=["mfa_enabled"])
            login(request, user)
            audit("auth.mfa_verified", actor=user)
            return Response(UserSerializer(user).data)
        return Response({"detail": "Invalid MFA token"}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["post"])
    def invitation(self, request):
        return Response({"detail": "Invitation acceptance placeholder"})

    @action(detail=False, methods=["post"])
    def password_reset(self, request):
        return Response({"detail": "Password reset placeholder"})

    @action(detail=False, methods=["get"])
    def sso_providers(self, request):
        return Response(["oidc", "saml", "entra_id", "google_workspace", "keycloak"])


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("last_name", "first_name")
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    @action(detail=True, methods=["post"])
    def disable(self, request, pk=None):
        user = self.get_object()
        user.is_active = False
        user.save(update_fields=["is_active"])
        audit("iam.user_disabled", actor=request.user, resource=user)
        return Response(UserSerializer(user).data)

    @action(detail=True, methods=["post"])
    def enable(self, request, pk=None):
        user = self.get_object()
        user.is_active = True
        user.save(update_fields=["is_active"])
        audit("iam.user_enabled", actor=request.user, resource=user)
        return Response(UserSerializer(user).data)
