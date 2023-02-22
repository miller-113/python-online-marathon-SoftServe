from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from author.views import AuthorViewSet
from authentication.views import CustomUserViewSet, CustomUserOrderViewSet,\
     UserOrderDetail, UserOrders
from order.views import OrderViewSet
from book.views import BookViewSet


router = routers.DefaultRouter()
router.register(r'authors', AuthorViewSet, basename='authors')
router.register(r'users', CustomUserViewSet, basename='users')
router.register(r'orders', OrderViewSet, basename='Order')
router.register(r'books', BookViewSet, basename='Books')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/', include('book.urls')),
    path('authentication/', include(('authentication.urls', 'authentication'),
         namespace='authentication')),
    path('author/', include(('author.urls', 'author'), namespace='author')),
    path('order/', include(('order.urls', 'order'), namespace='order')),
    path('', include(('authentication.urls', 'main_page'),
         namespace='main_page')),


    path('api-auth/', include('rest_framework.urls',
         namespace='rest_framework')),


    path('api/v1/', include([
        path('', include((router.urls, 'apis'), namespace='apis')),
        path('users/<int:user_id>/orders/', UserOrders.as_view(),
             name='user-orders'),
        path('users/<int:user_id>/orders/<int:order_num>/',
             UserOrderDetail.as_view(),
             name='user-order_detail'),
    ])),
]
