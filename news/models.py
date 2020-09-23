from PIL import Image, ImageDraw
from django.db import models
from ckeditor.fields import RichTextField

class image_article(models.Model):
    image = models.ImageField(upload_to="images/", blank=True)
    
    def __str__(self):
        return self.image.url


    class Meta:
        verbose_name = "Картинка"
        verbose_name_plural = "Картинки"


class article(models.Model):
    title = models.CharField('Название стьатьи', max_length=100)
    text = RichTextField('Текст записи', blank=True)
    image = models.ImageField(null=False, upload_to="images/", verbose_name='Изображение')
    date_a = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    list_img = models.ManyToManyField(image_article, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Новости"



class covid(models.Model):
    title = models.CharField('Название блока', max_length=100)
    text = RichTextField('Содержание блока', blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Инфорамация'
        verbose_name_plural = "Информация"
