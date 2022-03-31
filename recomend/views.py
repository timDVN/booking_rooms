from django.shortcuts import render, redirect
from . import models


# Create your views here.
def view_rec(request):
    if request.method == 'post':
        min_capacity = request.POST['min_capacity']
        session_start = request.POST['sesion_start']
        session_end = request.POST['session_end']
        suitable = list()
        for room in models.Room.objects.filter(capacity__gte=min_capacity):
            if room.is_free(session_start, session_end):
                suitable.append(room.room_name)
        # как-то вывести suitable


def book_room(request):
    if request.method == 'post':
        auditorium = request.POST['room_name']
        session_start = request.POST['sesion_start']
        session_end = request.POST['session_end']
        suitable = list()
        for room in models.Room.objects.filter(room_name=auditorium):
            if room.is_free(session_start, session_end):
                book = models.Schedule(room, session_start, session_end)
                return redirect('/')
#             show error
