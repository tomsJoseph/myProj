from .models import *
from rest_framework import viewsets
from .serializers import *
from rest_framework.generics import ListAPIView
from .pagination import Results5SetPagination
from .permissions import AdminOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class NoteTypeViewSet(viewsets.ModelViewSet):
    queryset = NoteType.objects.all()
    serializer_class = NoteTypeSerializer
    permission_classes = [AdminOrReadOnly]



class WDayViewSet(viewsets.ModelViewSet):
    queryset = WDay.objects.all()
    serializer_class = WDaySerializer


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    pagination_class = Results5SetPagination
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(creator = self.request.user)




