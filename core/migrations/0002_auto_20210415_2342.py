# Generated by Django 3.1.7 on 2021-04-15 18:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='upload',
            field=models.FileField(upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['wav', 'mp3', 'ogg'])]),
        ),
    ]
