# Generated by Django 2.1.1 on 2018-10-18 09:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guestbook', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='time',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
