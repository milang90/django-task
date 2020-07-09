from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied

class HelloView(APIView):
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = (IsOwner,)

    # Ensure a user sees only own Note objects.
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Task.objects.filter(owner=user)
        raise PermissionDenied()

    # Set user as owner of a Notes object.
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
