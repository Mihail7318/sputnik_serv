# Generated by Django 3.1 on 2020-09-21 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0002_auto_20200824_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='view',
            field=models.BooleanField(default=True, verbose_name='Показать'),
            preserve_default=False,
        ),
    ]