"""
URL configuration for proj project.

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
from django.urls import path, include
from main import views as main_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', main_views.test),
    path('posts/', main_views.posts, name="posts"),
    path('', main_views.posts, name="main"),
    # path('posts/<str:post_id>', main_views.post),
    path('posts/<int:post_id>', main_views.post, name="post"),
    path('posts/add/free', main_views.add_free, name="add_free"),
    path('posts/add/model', main_views.add_model, name="add_model"),
]

urlpatterns += [path('accounts/', include('django.contrib.auth.urls'))]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)