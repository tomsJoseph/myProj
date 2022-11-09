from .models import *
from rest_framework import viewsets
from .serializers import *

class NoteTypeViewSet(viewsets.ModelViewSet):
    queryset = NoteType.objects.all()
    serializer_class = NoteTypeSerializer


class WDayViewSet(viewsets.ModelViewSet):
    queryset = WDay.objects.all()
    serializer_class = WDaySerializer


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

