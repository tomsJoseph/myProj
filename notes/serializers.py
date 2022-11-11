from rest_framework import serializers
from .models import *


class NoteTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteType
        fields = ['id', 'tname', 'created', 'added_by']


class WDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = WDay
        fields = ['id', 'day_name', 'created']



class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'note_text', 'ntype', 'wdays', 'created']
