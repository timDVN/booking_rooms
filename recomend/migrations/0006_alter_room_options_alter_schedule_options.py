# Generated by Django 4.0.3 on 2022-03-31 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recomend', '0005_rename_end_schedule_finish'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'verbose_name': 'Комната', 'verbose_name_plural': 'Комнаты'},
        ),
        migrations.AlterModelOptions(
            name='schedule',
            options={'verbose_name': 'Бронь', 'verbose_name_plural': 'Бронь'},
        ),
    ]
