from django.contrib import admin
from django.urls import path, include

from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title="TASK API")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('task.urls')),
    path('api/auth/', include('jwtauth.urls'), name='jwtauth'),
    path('api/docs/', schema_view),
]
