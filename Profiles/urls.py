from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    url(r'^student_register/$', views.StudentRegister, name="studentRegister"),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='Profiles/login.html'), name='login'),
]