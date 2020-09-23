from django.contrib import admin
from .models import Document, Uslugi

# Register your models here.
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title',)
admin.site.register(Document,DocumentAdmin)
# Register your models here.
class UslugiAdmin(admin.ModelAdmin):
    list_display = ('title','date')
admin.site.register(Uslugi,UslugiAdmin)
