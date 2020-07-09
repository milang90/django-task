from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import TaskViewSet

router = SimpleRouter()
router.register('task', TaskViewSet, basename="task")
urlpatterns = router.urls
