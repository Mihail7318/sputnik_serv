# Generated by Django 3.1 on 2020-08-22 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='file',
            field=models.FileField(upload_to='document/', verbose_name='Фаил'),
        ),
    ]
