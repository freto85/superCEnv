"""superC URL Configuration

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
from django.urls import path,include
from django.contrib.auth import views
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomePage.as_view(),name='homepage'),
    path('thanks/', views.ThanksPage.as_view(),name='thanks'),
    path('accounts/', include(('accounts.urls','accounts'),namespace='accounts')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('merits/', include(('badges.urls','badges'), namespace='badges')),
    path('news/', include(("news.urls",'news'), namespace="news")),
    path('resources/', include(('resources.urls','resources'), namespace='resources')),
    path('roadmap/', include(('rewards.urls','rewards'), namespace='rewards')),
    path('special/', include(('special.urls','special'), namespace='special')),
    path('station/', include(('station.urls','station'), namespace='station')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
