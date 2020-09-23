# Generated by Django 3.1 on 2020-09-15 11:21

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0003_uslugi'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='uslugi',
            options={'verbose_name': 'Достижение', 'verbose_name_plural': 'Достижения'},
        ),
        migrations.AlterField(
            model_name='uslugi',
            name='file',
            field=models.FileField(upload_to='rewards/', verbose_name='Фаил'),
        ),
        migrations.AlterField(
            model_name='uslugi',
            name='text',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='Описание (необязательно)'),
        ),
        migrations.AlterField(
            model_name='uslugi',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Название достижения (нигде не отображается импользуется для удобства поиска)'),
        ),
    ]