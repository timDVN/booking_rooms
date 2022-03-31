from django.db import models


# Create your models here.
class Room(models.Model):
    room_name = models.CharField('название аудитории', max_length=100, unique=True)
    capacity = models.IntegerField('вместимость аудитори', blank=False)

    @property
    def get_capacity(self):
        return self.capacity

    def __str__(self):
        return f'''Аудитория:{self.room_name}  Вместимость:{self.capacity}'''

    def is_free(self, begin, end):
        return check_free(self, begin, end)

    class Meta:
        verbose_name = 'Аудитория'
        verbose_name_plural = 'Аудитории'


class Schedule(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start = models.DateTimeField('Старт сессии', blank=False)
    finish = models.DateTimeField('Конец сессии', blank=False)

    def __init__(self, auditorium, strt, fnsh, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.room = auditorium
        self.start = strt
        self.finish = fnsh

    def __str__(self):
        return f'''{self.room}  Старт сессии: {self.start}  Конец сесии:{self.finish}'''

    class Meta:
        verbose_name = 'Бронь'
        verbose_name_plural = 'Бронь'


def check_free(room, begin, end):
    i = 0
    for shc in Schedule.objects.filter(room=room):
        if (begin <= shc.start <= end) or (begin <= shc.end <= end) or (shc.start <= begin and shc.finish >= end):
            i += 1
    return i == 0
