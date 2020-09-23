from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Document(models.Model):
    title = models.CharField('Название документа', max_length=50)
    file = models.FileField('Фаил',upload_to="document/")

    class Meta:
        verbose_name = "Документ"
        verbose_name_plural = "Документы"

class Uslugi(models.Model):
    title = models.CharField('Название достижения (нигде не отображается импользуется для удобства поиска)', max_length=50)
    text = RichTextField('Описание (необязательно)', blank=True)
    date = models.DateField(auto_now_add=True, verbose_name='Дата публикации')
    file = models.FileField('Фаил', upload_to="rewards/")

    class Meta:
        verbose_name = "Достижение"
        verbose_name_plural = "Достижения"
