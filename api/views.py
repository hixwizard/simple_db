from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.permissions import IsOwnerOrReadOnly
from api.models import User, Project, Task, Comment
from api.mixins import PerformUpdateMixin, PerformDestroyMixin
from api.serializers import (
    UserSerializer, ProjectSerializer, TaskSerializer, CommentSerializer
)


class UserViewSet(viewsets.ModelViewSet):
    """
    Пользователи.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticated)


class ProjectViewSet(
    PerformUpdateMixin,
    PerformDestroyMixin,
    viewsets.ModelViewSet
):
    """
    Проекты.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticated)


class TaskViewSet(
    PerformUpdateMixin,
    PerformDestroyMixin,
    viewsets.ModelViewSet
):
    """
    Задачи к проектам.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticated)


class CommmentViewSet(PerformDestroyMixin, viewsets.ModelViewSet):
    """
    Комментарии к задаче.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticated)
