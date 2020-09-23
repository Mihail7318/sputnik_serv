from django.db import models

# Create your models here.
class Video(models.Model):
    title = models.CharField('Название видео', max_length=50, blank=True)
    date = models.DateTimeField('Дата публикаци', auto_created=True)
    description = models.CharField('Описание видео (необязательно)',max_length=250, blank=True)
    image = models.ImageField(null=False, upload_to="images/", verbose_name='Изображение видео')
    file = models.FileField('Фаил', upload_to="video/")
    view = models.BooleanField('Показать')

    class Meta:
        verbose_name = "Видео"
        verbose_name_plural = "Видео"