# Generated by Django 4.1.2 on 2024-01-26 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]