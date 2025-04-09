from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('order/', views.order, name='order'),
    path('delivery/', views.delivery, name='delivery'),
    path('catering/', views.catering, name='catering'),
    path('payment/', views.payment, name='payment'),
    path('orders/delivery/', views.delivery_orders, name='delivery_orders'),
    path('orders/catering/', views.catering_orders, name='catering_orders'),
    path('orders/payment/', views.payment_orders, name='payment_orders'),
    path('orders/create/', views.create_order, name='create_order'),
    path('order_success/', views.order_success, name='order_success'),  # Add this line
]
