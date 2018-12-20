"""smartfarm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^index', views.index),
    url(r'^control/', views.control),
    url(r'^graph/', views.graph),
    url(r'^history/', views.history),
    url(r'^meter/', views.control),
    url(r'^vegetables/view/', views.view_vegetable),
    url(r'^vegetables/new/', views.new_vegetable),
    url(r'^vegetables/add/', views.add_vegetable),
    url(r'^vegetables/delete/', views.del_vegetable),
    url(r'^vegetables/update/', views.update_vegetable),
    url(r'^vegetables/edit/(?P<id>[0-9]+)', views.edit_vegetable),
    url(r'^plant/add/', views.add_plant),
    url(r'^plant/keep/', views.keep_plant),
    url(r'^plant/compost/', views.add_compost),
    url(r'^plant/edit_compost', views.edit_compost),
    url(r'^plant/view_compost/(?P<id>[0-9]+)', views.view_compost),
    url(r'^plant/delete/', views.del_plant),
    url(r'^plant/delete_compost/', views.del_compost),
    url(r'^valve/', views.valve),
    url(r'^valve_state/', views.valve_state),
]
