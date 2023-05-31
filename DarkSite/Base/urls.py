from django.urls import path
from . import views


urlpatterns = [
    path('',views.my_view,name='home'),
    path('cart/', views.cart_view, name='cart'),
    path('<int:pk>/addcart/', views.add_cart, name ='add-cart'),
    path('sach_khoa_hoc/',views.filter_sach_khoa_hoc, name ='sach_khoa_hoc'),
    path('sach_lam_giau/',views.filter_sach_lam_giau, name ='sach_lam_giau'),
    path('sach_thieu_nhi/',views.filter_sach_thieu_nhi, name ='sach_thieu_nhi'),

    path('<int:pk>/', views.detail_product, name ='detail_product'),
    path('search/', views.search_feature, name ='search')
    
    
]
  