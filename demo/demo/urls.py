"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from one import views as one_views



#from one.views import (
    #registration_views,
    #register_view,
    #logout_views,
    #login_views,
    #one_view,
    #must_authenticate_views,
#)

urlpatterns = [
    #path('', home_screen_view, name="home"),
    path('admin/', admin.site.urls),
    #path('one/', one_view, name="one"),
    #path('blog/', include('blog.urls', 'blog')),
    #path('login/', login_views, name="login"),
    #path('logout/', logout_views, name="logout"),
    #path('must_authenticate/', must_authenticate_views, name="must_authenticate"),
    #path('must_authenticate/', auth_views.must_authenticateView.as_view(template_name='one/must_authenticate.html'),name='must_authenticate'),
    #path('register/', registration_views, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='one/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='one/logout.html'), name='logout'),
    path('register/', one_views.register, name='register'),
    #path('register/', register_view, name="register"),
	
	# REST-framework
    #path('api/blog/', include('blog.api.urls', 'blog_api')),
    path('api/one/', include('one.api.urls', 'one_api')),

    # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='registration/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='registration/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='registration/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='registration/password_reset_complete.html'
         ),
         name='password_reset_complete'),
    #path('', include('one.urls')),

         
]
    #path('', include('netmon.urls')),


#if settings.DEBUG:
 #   urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
  #  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


