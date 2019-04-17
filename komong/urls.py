from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include('api.urls')),  # All of api

    path('', include('rest_framework.urls', namespace='rest_framework')),
    path('doc/', schema_view),
]
