"""neros URL Configuration

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
from email.mime import image
from unicodedata import name
from django.conf.urls import url
from users import views
from django.urls import path
from django.contrib.auth import views as auth_views
from users import views as user_views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


#from .views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', user_views.home, name='home'),
    path('register/', user_views.register, name='register'),
    path('index/', user_views.register, name='index'),
  
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    # Profiilitiedot

    path('edit_details', user_views.edit_details, name = 'edit_details'),

    # Asetukset

    path('settings', user_views.settings, name = 'settings'),

    # Imagehomma

    path('picture_images', user_views.display_picture_images, name = 'picture_images'),
    path('picture_images', user_views.display_picture_images, name = 'edit'),
    url(r'^$', user_views.display_picture_images, name = 'home'),
    path('image_upload', user_views.picture_image_view, name = 'image_upload'),
    path('success', user_views.success, name = 'success'),
    url(r'^deleteProduct/(?P<pk>.*)', views.deleteProduct, name="image-delete"),
    path('edit-product/<str:pk>', views.editProduct, name="edit-prod"),
    url('change_password', user_views.change_password, name='change_password'),
    path('edit', user_views.edit, name = 'edit') 
]


  
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
