# Generated by Django 5.0.6 on 2024-06-17 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moon', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutmoon',
            name='farm_logo',
            field=models.ImageField(blank=True, null=True, upload_to='Logos/'),
        ),
        migrations.AddField(
            model_name='aboutmoon',
            name='harvesta_logo',
            field=models.ImageField(blank=True, null=True, upload_to='Logos/'),
        ),
        migrations.AddField(
            model_name='aboutmoon',
            name='units_of_cattle_logo',
            field=models.ImageField(blank=True, null=True, upload_to='Logos/'),
        ),
        migrations.AddField(
            model_name='aboutmoon',
            name='units_of_technic_logo',
            field=models.ImageField(blank=True, null=True, upload_to='Logos/'),
        ),
    ]
