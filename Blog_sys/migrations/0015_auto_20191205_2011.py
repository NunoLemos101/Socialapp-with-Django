# Generated by Django 2.2.4 on 2019-12-05 19:11

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Blog_sys', '0014_friendrequest'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FriendRequest',
            new_name='FollowRequest',
        ),
    ]
