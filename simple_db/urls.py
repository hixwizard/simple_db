from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('', include('api.urls')),
]
# /auth/users/ регистрация
# /auth/users/me получить пользователя
# /auth/jwt/create/ создать токен
# /auth/jwt/refresh/ обновить токен
