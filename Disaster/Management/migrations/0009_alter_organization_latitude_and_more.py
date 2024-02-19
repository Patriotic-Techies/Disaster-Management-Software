# Generated by Django 4.2.6 on 2023-10-15 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0008_rename_location_organization_organization_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
    ]