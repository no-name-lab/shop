from django.urls import path
from .views import *

urlpatterns = [
    path('', ProductListViewSet.as_view({'get': 'list', 'post': 'create'}), name='product_list'),
    path('<int:pk>/', ProductViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='product_detail'),

    path('category/', CategoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='category_list'),
    path('category/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='category_detail'),

    path('userprofile/', UserProfileViewSet.as_view({'get': 'list', 'post': 'create'}), name='userprofile_list'),
    path('userprofile/<int:pk>/', UserProfileViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='userprofile_detail'),

    path('cart/', CartViewSet.as_view({'get': 'retrieve'}), name='cart_detail'),

    #path('cart_items/', CarItemViewSet.as_view({'get': 'list', 'post': 'create'}), name='cart_item_list'),
    #path('cart_items/<int:pk>/', CarItemViewSet.as_view({'put': 'update', 'delete': 'destroy'})),
]
