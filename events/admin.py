from django.contrib import admin
from .models import event, PostsImages
# Register your models here.
#admin.site.register(event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('event_title', 'image', 'date')
admin.site.register(event, EventAdmin)


admin.site.register(PostsImages)