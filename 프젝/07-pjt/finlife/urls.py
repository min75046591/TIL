from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('save-deposit-products/', views.save_deposit_products, name='save_deposit_products'),
    path('deposit-products/', views.deposit_products, name='deposit_products'),
    path('deposit-product-options/<str:fin_prdt_cd>/', views.deposit_products_options, name='deposit_products_options'),
    path('deposit-products/top-rate/', views.top_rate, name='top_rate'),
]
