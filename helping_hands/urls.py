"""
URL configuration for HelpingHands project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import ResetPasswordView
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),

    path('/login/', views.login, name='login'),
    path('/handlelogin/', views.handlelogin, name='handlelogin'),

    path('/signin/', views.signin, name='signin'),
    path('/handleRequest/', views.handleRequest, name='handleRequest'),

    path('/home/', views.home, name='home'),
    path('/aboutus/', views.aboutus, name='aboutus'),
    path('/donee/', views.donee, name='donee'),
    path('/donor/', views.donor, name='donor'),
    path('/partnerships/', views.partnerships, name='partnerships'),
    path('/explore/', views.explore, name='explore'),
    path('/request/', views.request1, name='request1'),
    path('/blogs/', views.blogs, name='blogs'),
    path('/helping/', views.helping, name='helping'),
    path('/donatemonthly/', views.donatemonthly, name='donatemonthly'),

    path('handledonor/', views.handledonor, name='handledonor'),
    path('handledonee/', views.handledonee, name='handledonee'),
    path('handleexplore/', views.handleexplore, name='handleexplore'),
    path('handle_camp/', views.handle_camp, name='handle_camp'),
    path('logout/', views.logoutPage, name='logoutPage'),
    path('password_reset/', ResetPasswordView.as_view(), name='helping_hands'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(post_reset_login=True,template_name='users/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),name='password_reset_complete'),
]


# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)