# Generated by Django 3.1.5 on 2021-01-26 19:41

import core.models
from django.db import migrations, models
import media


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210125_1406'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Todo',
        ),
        migrations.AddField(
            model_name='cidade',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to=media),
        ),
        migrations.AddField(
            model_name='famoso',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to=media),
        ),
    ]
