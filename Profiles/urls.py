from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    url(r'^student_register/$', views.StudentRegister, name="studentRegister"),
    url(r'^tutor_register/$', views.TutorRegister, name="tutorRegister"),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='Profiles/login.html'), name='login'),
    url(r'^log_out/$', views.logoutUser, name="logout"),
    url(r'^student_profile/$', views.StudentProfile, name="studentProfile"),
    url(r'^tutor_profile/$', views.TutoProfile, name="tutorProfile"),
    url(r'^student_update/$', views.StudentUpdate, name="studentUpdate"),
]