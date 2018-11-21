"""BlogProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.Login, name='Login Page'),

    path('login/', views.login, name='login'),

    #path('blog/', views.Home, name='Home Page'),

    path('panel/', views.Panel, name='Panel'),

    path('panel/view/', views.Panel, name='View'),

    path('panel/create/', views.create, name='create post'),

    path('panel/save', views.save_publish_post, name='save or publish post'),

    path('panel/update/', views.update, name='update'),

    path('panel/update/<int:post_id>', views.update_post, name='update post'),

    path('panel/delete/', views.delete_page, name='delete page'),

    path('panel/delete/<int:post_id>', views.delete_post, name='delete post'),

    path('panel/publish/', views.publish, name='publish page'),

    path('panel/publish/<int:post_id>', views.publish_post, name='publish'),

    path('recommended/', views.Show_Recommended, name='Recommended'),

    path('panel/recommend/', views.Recommend, name='Recommend'),

    path('panel/recommend/<int:post_id>', views.recommend_post, name='Recommend'),

    path('panel/add user/', views.Add_User, name='Add User Page'),

    path('panel/add user/submit', views.Submit_Add_User, name='Submit Add User'),

    path('blog/logout/', views.logout, name='logout'),

    path('posts/details/<int:post_id>',views.Show_Post, name='show_post')

]

