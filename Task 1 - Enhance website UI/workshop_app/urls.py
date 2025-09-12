"""workshop_portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  re_path(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  re_path(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import re_path
    2. Add a URL to urlpatterns:  re_path(r'^blog/', include('blog.urls'))
"""
from django.urls import re_path
from workshop_app import views

app_name = "workshop_app"

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^register/$', views.user_register, name="register"),
    re_path(r'^activate_user/(?P<key>.+)$', views.activate_user),
    re_path(r'^activate_user/$', views.activate_user),
    re_path(r'^login/$', views.user_login, name="login"),
    re_path(r'^logout/$', views.user_logout, name="logout"),
    re_path(r'^status$', views.workshop_status_coordinator,
        name='workshop_status_coordinator'),
    re_path(r'^dashboard$', views.workshop_status_instructor,
        name='workshop_status_instructor'),
    re_path(r'^accept_workshop/(?P<workshop_id>\d+)', views.accept_workshop,
        name='accept_workshop'),
    re_path(r'^change_workshop_date/(?P<workshop_id>\d+)$',
        views.change_workshop_date, name='change_workshop_date'),
    re_path(r'^details/(?P<workshop_id>\d+)$', views.workshop_details,
        name='workshop_details'),
    re_path(r'^type_details/(?P<workshop_type_id>\d+)$',
        views.workshop_type_details, name='workshop_type_details'),
    re_path(r'^type_tnc/(?P<workshop_type_id>\d+)$',
        views.workshop_type_tnc, name='workshop_type_tnc'),
    re_path(r'^propose/$', views.propose_workshop,
        name='propose_workshop'),
    re_path(r'^add_workshop_type$', views.add_workshop_type,
        name='add_workshop_type'),
    re_path(r'^delete_attachment_file/(?P<file_id>\d+)$',
        views.delete_attachment_file, name='delete_attachment_file'),
    re_path(r'^types/$', views.workshop_type_list,
        name='workshop_type_list'),
    re_path(r'^view_profile/$', views.view_own_profile,
        name='view_own_profile'),
    re_path(r'^view_profile/(?P<user_id>\d+)$', views.view_profile,
        name='view_profile'),
]
