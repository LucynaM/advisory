from django.contrib import admin
from .models import Events

# Register your models here.

@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ('title', 'creation_date')
    fields = ('title', 'content', 'photo_desktop', 'photo_mobile', 'tags')

    @staticmethod
    def get_departments(obj):
        return ', '.join(department.name for department in obj.departments.all())
