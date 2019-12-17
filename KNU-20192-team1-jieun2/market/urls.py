from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.market, name="market"),
    path('<int:market_id>', views.detail, name="detail"),
    path('new', views.new, name="new"),
    path('market_serach', views.market_search, name="market_search"),
    path('create', views.create, name="create"),
    path('delete/<int:market_id>',views.delete, name="delete"),
    path('menu/create/<int:market_id>', views.menu_create,name="menu_create"),
    path('like/<int:market_id>',views.post_like, name="post_like"), # 즐겨찾기 위한 url
    path('order_check/create/<int:market_id>/<int:menu_id>', views.order_create, name="order_create"),
    path('order_check', views.order_check, name="order_check"),
    path('admin_order_check/<int:market_id>', views.admin_order_check, name="admin_order_check"),
    path('order_delete/<int:order_id>',views.order_delete, name="order_delete"),
    path('admin_order_delete/<int:market_id>/<int:order_id>',views.admin_order_delete, name="admin_order_delete")
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
