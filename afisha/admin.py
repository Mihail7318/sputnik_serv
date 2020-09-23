from django.contrib import admin
from .models import afisha, holiday

class AfishaAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_in', 'date_out', 'time', 'price', 'date_pub', 'genre', 'imagekin')
    fields = ('title', ('date_in', 'date_out'), 'time', 'price')
admin.site.register(afisha, AfishaAdmin)

class HolidayAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_h', 'date_pub')
admin.site.register(holiday,HolidayAdmin)
# Register your models here.
