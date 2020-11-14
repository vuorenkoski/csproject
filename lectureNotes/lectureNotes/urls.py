from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.loginpage, name='login'),
    path('logout', views.logoutpage, name='logout'),
    path('signup', views.signup, name='signup'),
    path('newnote', views.newnote, name='newnote'),
    path('course/<int:coursekey>/', views.course, name='course'),
    path('share', views.share, name='share'),
#    path('admin', views.admin, name='admin'),
]
