from django.contrib import admin
from .models import Schedule, Room

admin.site.register(Room)
admin.site.register(Schedule)