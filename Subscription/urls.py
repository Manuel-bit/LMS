from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    url(r'^plans/$', views.plan, name="subscriptionPlan"),
    url(r'^checkout/$', views.checkout, name="checkout"),
    url(r'^courses/$', views.courses, name="courses"),
    url(r'^course_single/(?P<pk>\d+)/$', views.courseSingle, name='courseSingle'),
]