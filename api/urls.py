from django.urls import path, include

urlpatterns = [
    path('v1/', include('api.users.urls')),
    path('auth/', include('api.auth.urls')),
]
