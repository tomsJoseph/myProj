from django.urls import path
from django.urls.conf import include
from .views import *
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'notetypes', NoteTypeViewSet)
router.register(r'days', WDayViewSet)
router.register(r'notes', NoteViewSet)

urlpatterns = [
       path('', include(router.urls)),
]