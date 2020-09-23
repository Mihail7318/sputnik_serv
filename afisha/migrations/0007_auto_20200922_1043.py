# Generated by Django 3.1 on 2020-09-22 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afisha', '0006_auto_20200918_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='afisha',
            name='imagekin',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Внешняя ссылка'),
        ),
        migrations.AlterField(
            model_name='afisha',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/', verbose_name='Изображение'),
        ),
    ]
