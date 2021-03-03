from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^plans/$', views.plan, name="subscriptionPlan"),
    url(r'^checkout/$', views.checkout, name="checkout"),
]