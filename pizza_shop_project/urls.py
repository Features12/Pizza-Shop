"""pizza_shop_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from pizza_shop_app import views
from django.contrib.auth.views import login, logout
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^sign-in/$', login, {'template_name':'pizza_shop_app/sign_in.html'}, name='sign-in'),
    url(r'^sign-out/$', logout, {'next_page': '/'}, name='sign-out'),
    url(r'^pizza-shop/$', views.pizza_shop_home, name='pizza-shop-home'),
    url(r'^pizza-shop/sign-up/$', views.pizza_shop_sing_up, name='pizza-shop-sign-up'),
    url(r'^pizza-shop/account/$', views.pizza_shop_account, name='pizza-shop-account'),
    url(r'^pizza-shop/pizza/$', views.pizza_shop_pizza, name='pizza-shop-pizza'),
    url(r'^pizza-shop/pizza/add/$', views.pizza_shop_add_pizza, name='pizza-shop-add-pizza'),
    url(r'^pizza-shop/pizza/edit/(?P<pizza_id>\d+)/$', views.pizza_shop_edit_pizza, name='pizza-shop-edit-pizza')
] + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
