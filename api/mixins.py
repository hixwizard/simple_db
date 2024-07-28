from rest_framework import status


class PerformUpdateMixin:
    def perform_update(self, serializer):
        if self.request.user.is_authenticated & (
                self.request.user.is_admin |
                self.request.user.is_moderator):
            return super().perform_update(serializer)
        return status.HTTP_405_METHOD_NOT_ALLOWED


class PerformDestroyMixin:
    def perform_destroy(self, instance):
        if self.request.user.is_authenticated & (
                self.request.user.is_admin |
                self.request.user.is_moderator):
            return super().perform_destroy(instance)
        return status.HTTP_405_METHOD_NOT_ALLOWED
