# Generated by Django 4.2.6 on 2023-10-13 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0003_alter_organization_admin_name_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
