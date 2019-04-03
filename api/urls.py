from django.urls import path, include

urlpatterns = [
    path('v1/', include('api.users.urls')),
]
