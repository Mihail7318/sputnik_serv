from django.db import models

# Create your models here.
class Setting(models.Model):
    title_site = models.CharField("Название сайта", max_length=100)
    descript = models.CharField("Название в шапке сайта", max_length=100)
    phone = models.CharField("Номер телефона на главной", max_length=100)
    info_pres = models.BooleanField("Показать блок информации")
    holiday_pres = models.BooleanField("Показать блок <Праздники>")
    video_pres = models.BooleanField("Показать видео блок")


    class Meta:
        verbose_name = "Настройки"
        verbose_name_plural = "Настройки"
