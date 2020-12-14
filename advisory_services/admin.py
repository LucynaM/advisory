from django.contrib import admin
from .models import Department, Service

# Register your models here.

# Register your models here.
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_team_members')
    fields = ('name', 'content', 'photo_desktop', 'photo_mobile', 'team_members', 'events')

    @staticmethod
    def get_team_members(obj):
        return ', '.join(team_member.name for team_member in obj.team_members.all())


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_department', 'get_team_members')
    fields = ('name', 'department', 'content', 'photo_desktop', 'photo_mobile', 'team_members', 'tags')

    @staticmethod
    def get_department(obj):
        return obj.name

    @staticmethod
    def get_team_members(obj):
        return ', '.join(team_member.name for team_member in obj.team_members.all())
