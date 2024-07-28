from rest_framework import serializers
from djoser.serializers import UserSerializer

from api.models import User, Project, Task, Comment


class UserSerializer(UserSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'avatar',
            'role'
        )
        search_fields = ('id', 'username',)


class ProjectSerializer(serializers.ModelSerializer):
    # add author
    class Meta:
        model = Project
        fields = (
            'title',
            'description',
            'start_time',
            'end_time',
            'file'
        )
        search_fields = ('title',)


class TaskSerializer(serializers.ModelSerializer):
    # add author
    project = serializers.SlugRelatedField(
        queryset=Project.objects.all(), slug_field='title', required=True)
    assignee = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field='username')

    class Meta:
        model = Task
        fields = (
            'title',
            'description',
            'start_date',
            'end_date',
            'priority',
            'assignee',
            'project'
        )
        search_fields = ('title',)


class CommentSerializer(serializers.ModelSerializer):
    task = serializers.SlugRelatedField(
        queryset=Task.objects.all(), slug_field='title')
    author = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field='username')

    class Meta:
        model = Comment
        fields = (
            'task',
            'author',
            'text'
        )
        search_fields = ('task', 'author')
