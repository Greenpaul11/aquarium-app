"""
URL configuration for aquarium project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from .views import (
    home_view
)
from accounts.views import (
    login_view,
    logout_view,
    register_view
)
from articles.views import (
    articles_view,
    article_view
)
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('accounts/login/', login_view,),
    path('accounts/logout/', logout_view),
    path('accounts/register/', register_view),
    path('articles/', articles_view),
    path('articles/<int:id>/', article_view)
]

#if settings.DEBUG:
    #urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    

