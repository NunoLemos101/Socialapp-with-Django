# Generated by Django 2.2.4 on 2019-11-25 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog_sys', '0007_announcements'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='animals',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='cars',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='culture',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='jobs',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='policy',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='services',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='sport',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='technology',
            field=models.BooleanField(default=False),
        ),
    ]
