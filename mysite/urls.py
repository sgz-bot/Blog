"""
URL configuration for mysite project.

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
from blog import views
from authentication.views import login_page, logout_user, signup_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="home"),
    path('articles/<int:id>/', views.article_detail, name="article_detail"),
    path('apropos/', views.apropos),
    path('contact/', views.contact),
    path('articles/add/', views.article_create, name='article-create'),
    path('article/<int:id>/change', views.article_update, name='article_update'),
    path('article/<int:id>/delete', views.article_delete, name='article_delete'),
    path('login/', login_page, name="login"),
    path('logout/', logout_user, name='logout'),
    path('signup/', signup_page, name='signup'),
]
