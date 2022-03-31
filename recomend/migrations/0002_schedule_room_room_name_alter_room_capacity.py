# Generated by Django 4.0.3 on 2022-03-31 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recomend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.CharField(max_length=100)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='room_name',
            field=models.CharField(default=22, max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='room',
            name='capacity',
            field=models.IntegerField(),
        ),
    ]
