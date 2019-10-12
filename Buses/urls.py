from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^areas/$', views.areas_of_chennai,  name = 'areas_of_chennai'),
    url(r'^mtc/$', views.mtc,  name = 'mtc'),
    url(r'^routes/$', views.Bus_route,  name = 'Bus_route'),
    url(r'^$', views.Choose_Location,  name = 'Choose_Location'),
    url(r'^api/$', views.CurrentLocationList.as_view()),
    url(r'^api/(?P<license_plate>[A-Z][A-Z][0-9][0-9][A-Z][A-Z][0-9][0-9][0-9][0-9])/$', views.CurrentLocationDetail.as_view()),
    #send a GET request to get data... an example http://localhost:8000/api/routes/?from=POONAMALLEE&to=GUINDY+R.S
    url(r'^api/routes/$', views.APIRouteGet, name = 'APIRouteGet'),
    url(r'^trial$', views.trial, name = 'trial'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
