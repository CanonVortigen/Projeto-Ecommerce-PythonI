"""djangoEcommerce URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from core import views
from catalog import views as views_catalog
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^contato/$', views.contact, name="contact"), 
    url(r'^entrar/$', LoginView.as_view(template_name='login.html'), name='login'), 
    url(r'^sair/$', LogoutView.as_view(next_page = 'index'), name='logout'),  
    url(r'^conta/', include('accounts.urls', namespace='accounts')), 
    url(r'^catalogo/', include('catalog.urls', namespace='catalog')), 
    url(r'^compras/', include('checkout.urls', namespace='checkout')),         
    url(r'^paypal/', include('paypal.standard.ipn.urls')),        
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
