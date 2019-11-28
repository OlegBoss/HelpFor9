"""
HelpFor9 URL Configuration

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

from django.conf.urls import include, url
import helpfor9_hse_ru.views

# Django processes URL patterns in the order they appear in the array
urlpatterns = [
    url(r'^$', helpfor9_hse_ru.views.index, name='index'),
    url(r'^home$', helpfor9_hse_ru.views.index, name='home'),
    url(r'^calendar$', helpfor9_hse_ru.views.calendar, name='calendar'),
    url(r'^calculator$', helpfor9_hse_ru.views.calculator, name='calculator'),
    url(r'^calc_results$', helpfor9_hse_ru.views.calc_results, name='calc_results'),
    url(r'^faculties$', helpfor9_hse_ru.views.faculties, name='faculties'),
    url(r'^info$', helpfor9_hse_ru.views.info, name='info'),
]