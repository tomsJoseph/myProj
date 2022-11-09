from django.contrib import admin
from .models import NoteType, Note, WDay
# Register your models here.
admin.site.register(NoteType)
admin.site.register(WDay)
admin.site.register(Note)