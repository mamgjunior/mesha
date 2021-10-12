from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'obras'

router = routers.DefaultRouter()
router.register(app_name, views.ObrasViewSet)

urlpatterns = [
    path('', include(router.urls)),
]