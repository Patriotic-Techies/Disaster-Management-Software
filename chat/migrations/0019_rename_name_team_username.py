# Generated by Django 4.2.6 on 2024-02-19 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0018_user_latitude_user_longitude'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='name',
            new_name='username',
        ),
    ]
