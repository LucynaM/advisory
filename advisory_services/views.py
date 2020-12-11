from django.shortcuts import render
from django.views import View
from .models import Department, Service


# Create your views here.
class DepartmentPage(View):
    def get(self, request, pk, slug):

        content = Department.objects.get(pk=pk, slug=slug)
        is_mobile = request.user_agent.is_mobile
        is_tablet = request.user_agent.is_tablet
        is_touch_capable = request.user_agent.is_touch_capable
        view_type = 'department'
        services_list = Service.objects.filter(department=pk)
        team_members_list = content.team_members.all()



        ctx = {
            'content': content,
            'services_list': services_list,
            'team_members_list': team_members_list,
            'is_mobile': is_mobile,
            'view_type': view_type
        }

        return render(request, 'advisory_services/base_page.html', ctx)


class ServicePage(View):
    def get(self, request, dept_slug, pk, slug):

        content = Service.objects.get(pk=pk, slug=slug)
        services_list = Service.objects.filter(department=content.department)
        team_members_list = content.team_members.all()

        is_mobile = request.user_agent.is_mobile
        is_tablet = request.user_agent.is_tablet
        is_touch_capable = request.user_agent.is_touch_capable
        view_type = 'service'

        ctx = {
            'content': content,
            'services_list': services_list,
            'team_members_list': team_members_list,
            'is_mobile': is_mobile,
            'view_type': view_type

        }

        return render(request, 'advisory_services/base_page.html', ctx)
