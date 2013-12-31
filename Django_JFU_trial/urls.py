from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from mainApp import views
from django.views.generic import TemplateView


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Django_JFU_trial.views.home', name='home'),
    # url(r'^Django_JFU_trial/', include('Django_JFU_trial.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),


    url(r'^home/$',TemplateView.as_view(template_name='trial.html')),
    url( r'upload/', views.upload, name = 'jfu_upload' ),

    # You may optionally define a delete url as well
    url( r'^delete/(?P<pk>\d+)$', views.upload_delete, name = 'jfu_delete' ),
)
