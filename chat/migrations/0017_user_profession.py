# Generated by Django 4.2.6 on 2024-02-19 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0016_team_user_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profession',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
