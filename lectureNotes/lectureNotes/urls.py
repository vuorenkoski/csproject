from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.loginpage, name='login'),
    path('logout', views.logoutpage, name='logout'),
    path('signup', views.signup, name='signup'),
    path('newnote', views.newnote, name='newnote'),
    path('course/<str:coursekey>/', views.courseview, name='courseview'),
    path('share', views.share, name='share'),
#    path('admin', views.admin, name='admin'),
]
