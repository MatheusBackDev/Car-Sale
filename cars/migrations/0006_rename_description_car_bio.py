# Generated by Django 5.0.4 on 2024-05-23 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_car_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='description',
            new_name='bio',
        ),
    ]
