from django.contrib import admin
from .models import TeamMember, Specialization


# Register your models here.
@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'get_departments')
    fields = ('first_name', 'last_name', 'academic_title', 'title', 'email', 'phone', 'content',
              'photo_desktop', 'photo_mobile', 'specializations')

    @staticmethod
    def get_departments(obj):
        return ', '.join(department.name for department in obj.departments.all())


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_team_members')
    #fields = ('name', 'get_team_members')

    @staticmethod
    def get_team_members(obj):
        return ', '.join(team_member.name for team_member in obj.team_members.all())

