from django.urls import path
from writerapp import views

urlpatterns=[
    path('writer/home',views.WriterHome.as_view(),name="writer_home"),
    path('user/register',views.UserRegisterView.as_view(),name="user_register"),
    path('user/login',views.UserLoginView.as_view(),name="user_login"),
    path('user/create',views.BlogCreateView.as_view(),name="user_create"),
    path('user/logout',views.UserLogoutView.as_view(),name="user_logout"),
    
]