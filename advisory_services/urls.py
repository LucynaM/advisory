"""advisory_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.utils.translation import gettext_lazy as __

from .views import DepartmentPage, ServicePage, EventPage, TeamPage

app_name = 'advisory_services'

urlpatterns = [
    path('<int:pk>/<slug:slug>/', DepartmentPage.as_view(), name='department'),
    path(__('services') + '/<int:dept_pk>/<slug:dept_slug>/<int:pk>/<slug:slug>/', ServicePage.as_view(), name='service'),
    path(__('events') + '/<int:dept_pk>/<slug:dept_slug>/<int:pk>/<slug:slug>/', EventPage.as_view(), name='event'),
    path(__('team') + '/<int:dept_pk>/<slug:dept_slug>/', TeamPage.as_view(), name='team'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



