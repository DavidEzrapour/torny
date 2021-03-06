"""tornyapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^create_tournament/$', csrf_exempt(views.CreateTournament.as_view())),
    url(r'^tournaments/$', csrf_exempt(views.Tournaments.as_view())),
    url(r'^tournaments/(?P<id>[0-9]+)/$', csrf_exempt(views.Tournaments.as_view())),
    url(r'^register/$', csrf_exempt(views.RegisterUser.as_view())),
    url(r'^login/$', csrf_exempt(views.AuthenticateUser.as_view())),
    url(r'^tournament_signup/$', csrf_exempt(views.RegisterUserInTournament.as_view())),
    url(r'^seeding/$', csrf_exempt(views.Seeding.as_view())),
    url(r'^CreateTourn/$', csrf_exempt(views.CreateTourn.as_view())),
    url(r'^ListTourns/$', csrf_exempt(views.ListTourns.as_view())),
    url(r'^next_bout/$', csrf_exempt(views.NextBout.as_view())),
]
