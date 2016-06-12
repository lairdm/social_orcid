from django.conf.urls import patterns, url
from django.views.generic.base import RedirectView

from social_orcid import views

urlpatterns = patterns('',
                       url(r'^logout/$', views.logout),
                       )
