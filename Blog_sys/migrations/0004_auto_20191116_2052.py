# Generated by Django 2.2.6 on 2019-11-16 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog_sys', '0003_auto_20191116_1612'),
    ]

    operations = [
        migrations.RenameField(
            model_name='likes',
            old_name='likes_number',
            new_name='likes_count',
        ),
        migrations.RemoveField(
            model_name='likes',
            name='user_who_liked',
        ),
    ]
