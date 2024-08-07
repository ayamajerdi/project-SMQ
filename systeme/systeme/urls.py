"""
URL configuration for systeme project.

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
from django.contrib import admin
from django.urls import path,include,re_path
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls')),
    path('user/',include('user.urls')),
    path('CRM/',include('CRM.urls')),
    path('RH/',include('RH.urls')),    
    path('fournisseur/',include('fournisseur.urls')),
    path('indicateur/',include('indicateur.urls')),
    path('risk/',include('risk.urls')),
    path('action/',include('action.urls')),
    path('doc/',include('doc.urls')),
    path('reunion/',include('reunion.urls')),
    path('audit/',include('audit.urls')),
    path('produit/',include('produit.urls')),
    path('conformite/',include('conformitereglementaire.urls')),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
urlpatterns +=[re_path(r'^.*',TemplateView.as_view(template_name='index.html'))]
