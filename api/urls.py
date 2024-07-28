from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import UserViewSet, ProjectViewSet, TaskViewSet, CommmentViewSet

router_v1 = DefaultRouter()
router_v1.register(r'users', UserViewSet, basename='users')
router_v1.register(r'projects', ProjectViewSet, basename='projects')
router_v1.register(
    r'projects/(?P<projects_id>\d+)/tasks', TaskViewSet, basename='tasks')
router_v1.register(
    r'projects/(?P<projects_id>\d+)/tasks/(?P<task_id>\d+)/comments',
    CommmentViewSet, basename='comments')

urlpatterns = [
    path('api/v1/', include(router_v1.urls)),
]
