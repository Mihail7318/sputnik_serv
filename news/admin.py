from django.contrib import admin
from django.contrib import admin
from django import forms
from .models import article, covid, image_article
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe


class ArticleAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = article
        fields = '__all__'


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_image', 'date_a')
    list_filter = ('title','date_a')
    form = ArticleAdminForm
    def get_image(self, obj):
    	return mark_safe(f'<img src = {obj.image.url} width="50" height="50"')

class ListimgAdmin(admin.ModelAdmin):
    list_display = ('get_image', )
    def get_image(self, obj):
    	return mark_safe(f'<img src = {obj.image.url} width="50" height="50"')


admin.site.register(article, ArticleAdmin)
admin.site.register(covid)
admin.site.register(image_article, ListimgAdmin)
# Register your models here.
