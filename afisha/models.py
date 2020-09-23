from django.db import models
from ckeditor.fields import RichTextField
from parser import pars
# Create your models here.
class afisha(models.Model):
    title = models.CharField('Название фильма', max_length=50)
    description = models.TextField('Текст записи', blank=True, null=True)
    imagekin = models.URLField('Внешняя ссылка', max_length=120, blank=True, null=True)
    date_in = models.DateField('Дата начала показа')
    date_out = models.DateField('Дата окочания показа')
    time = models.CharField('Время показа', max_length=20)
    price = models.IntegerField()
    date_pub = models.DateField(auto_now_add=True)
    genre = models.CharField('Жанр', max_length=20, blank=True, null=True)
    year = models.CharField('Год', max_length=20, blank=True, null=True)
    age = models.CharField('Возраст', max_length=20, blank=True, null=True)
    timefilm = models.CharField('Время', max_length=20, blank=True, null=True)

    def save(self, *args, **kwargs):
        q = pars.get_pars(self.title)
        self.description = q["description"]
        self.genre = q["genres"]
        self.year = q["year"]
        self.age = q["age"]
        self.timefilm = q["time"]
        self.imagekin = q["posterUrl"]
        super(afisha, self).save(*args, **kwargs)
        




    class Meta:
        verbose_name = "Афиша"
        verbose_name_plural = "Афиша"

class holiday(models.Model):
    title = models.CharField('Название праздника', max_length=50)
    description = RichTextField('Описание праздника', blank=True)
    image = models.ImageField(null=False, upload_to="images/", verbose_name='Изображение')
    date_h = models.DateField('Дата')
    date_pub = models.DateField(auto_now_add=True)


    class Meta:
        verbose_name = "Праздник"
        verbose_name_plural = "Праздники"