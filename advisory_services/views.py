from django.shortcuts import render
from django.views import View
from .models import Department, Service


# Create your views here.
class DepartmentPage(View):
    def get(self, request, pk, slug):

        department = Department.objects.get(pk=pk, slug=slug)
        is_mobile = request.user_agent.is_mobile
        is_tablet = request.user_agent.is_tablet
        is_touch_capable = request.user_agent.is_touch_capable

        services_list = Service.objects.filter(department=pk)
        team_members_list = department.team_members.all()



        ctx = {
            'content': department,
            'services_list': services_list,
            'team_members_list': team_members_list,
            'is_mobile': is_mobile,
        }

        return render(request, 'advisory_services/base_page.html', ctx)


class ServicePage(View):
    def get(self, request, dept_slug, pk, slug):

        service = Service.objects.get(pk=pk, slug=slug)
        services_list = Service.objects.filter(department=service.department)
        team_members_list = service.team_members.all()

        ctx = {
            'content': service,
            'services_list': services_list,
            'team_members_list': team_members_list,
        }

        return render(request, 'advisory_services/base_page.html', ctx)
