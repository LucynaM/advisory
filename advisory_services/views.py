from django.shortcuts import render
from django.views import View
from .models import Department, Service
from advisory_events.models import Events


# Create your views here.
class DepartmentPage(View):
    def get(self, request, pk, slug):

        view_type = 'department'
        content = Department.objects.get(pk=pk, slug=slug)
        is_mobile = request.user_agent.is_mobile
        is_tablet = request.user_agent.is_tablet
        is_touch_capable = request.user_agent.is_touch_capable

        services_list = Service.objects.filter(department=pk)
        team_members_list = content.team_members.all()
        events_list = content.events.all().order_by('-creation_date')

        ctx = {
            'content': content,
            'content_navigation_list': services_list,
            'team_members_list': team_members_list,
            'events_list': events_list,
            'is_mobile': is_mobile,
            'view_type': view_type
        }

        return render(request, 'advisory_services/department_page.html', ctx)


class ServicePage(View):
    def get(self, request, dept_pk, dept_slug, pk, slug):

        content = Service.objects.get(pk=pk, slug=slug)
        services_list = Service.objects.filter(department=content.department)
        team_members_list = content.team_members.all()

        is_mobile = request.user_agent.is_mobile
        view_type = 'service'

        ctx = {
            'content': content,
            'content_navigation_list': services_list,
            'team_members_list': team_members_list,
            'is_mobile': is_mobile,
            'view_type': view_type

        }

        return render(request, 'advisory_services/service_page.html', ctx)


class EventPage(View):

    def get(self, request, dept_pk, dept_slug, pk, slug):
        content = Events.objects.get(pk=pk, slug=slug)
        department = Department.objects.get(pk=dept_pk, slug=dept_slug)
        events_list = department.events.all().order_by('-creation_date')

        is_mobile = request.user_agent.is_mobile
        view_type = 'event'

        ctx = {
            'content': content,
            'content_navigation_list': events_list,
            'department': department,
            'is_mobile': is_mobile,
            'view_type': view_type

        }

        return render(request, 'advisory_services/event_page.html', ctx)


class TeamPage(View):

    def get(self, request, dept_pk, dept_slug):
        department = Department.objects.get(pk=dept_pk, slug=dept_slug)
        team_members_list = department.team_members.all()

        is_mobile = request.user_agent.is_mobile
        view_type = 'team_members'

        ctx = {
            'content': team_members_list,
            'content_navigation_list': team_members_list,
            'department': department,
            'is_mobile': is_mobile,
            'view_type': view_type
        }

        return render(request, 'advisory_services/team_page.html', ctx)
