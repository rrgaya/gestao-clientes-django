from django.contrib import admin
from django.urls import path, include
from vendas import urls as vendas_urls
from home import urls as home_urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth import urls as url_auth


urlpatterns = [
    path('', include("clientes.urls"), name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls'), name="api_urls"),
    path('accounts/', include('allauth.urls')),
    path('clientes/', include("clientes.urls", namespace="clientes")),
    path('produtos/', include("produtos.urls"), name='produtos_urls'),
    path('vendas/', include(vendas_urls), name='vendas_urls'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('conta/', include(url_auth)),
    path('contas/', include("accounts.urls"), name="accounts"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



admin.site.site_header = "Gestão de Clientes"
admin.site.index_title = "Administração"
admin.site.site_title = "Seja bem vindo ao Gestao de Clientes"