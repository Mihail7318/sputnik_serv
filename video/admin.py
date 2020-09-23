from django.contrib import admin
from .models import Video

# Register your models here.
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title','date','file','view')
admin.site.register(Video,VideoAdmin)
# Register your models here.
