# Generated by Django 2.2.4 on 2019-11-27 23:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Blog_sys', '0012_auto_20191128_0015'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='date_sent',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
