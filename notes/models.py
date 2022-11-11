from django.db import models
from django.contrib.auth.models import User

class NoteType(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    tname = models.CharField(max_length=100)
    added_by = models.ForeignKey(User, null=True, on_delete = models.SET_NULL, default = None)

    def __str__(self):
        return self.tname


class WDay(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    day_name = models.CharField(max_length=100)

    def __str__(self):
        return self.day_name


class Note(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    note_text = models.CharField(max_length=500) #Textfield is possilbe
    ntype = models.ForeignKey(NoteType, null=True, on_delete = models.SET_NULL)
    wdays = models.ManyToManyField(WDay)
    creator = models.ForeignKey(User, null=True, on_delete = models.SET_NULL, default = None)


    def __str__(self):
        return self.note_text
