from django.shortcuts import render, redirect
from .forms import OrderForm
from .models import Order
from django.contrib import messages

# Create your views here.

# Home page view
def home(request):
    return render(request, 'shop/home.html')

# Order page view
def order(request):
    return render(request, 'shop/order.html')

# Delivery page view
def delivery(request):
    return render(request, 'shop/delivery.html')

# Catering page view
def catering(request):
    return render(request, 'shop/catering.html')

# Payment page view
def payment(request):
    return render(request, 'shop/payment.html')

# View for Delivery Orders
def delivery_orders(request):
    orders = Order.objects.filter(order_type=Order.DELIVERY)
    return render(request, 'shop/delivery_orders.html', {'orders': orders})

# View for Catering Orders
def catering_orders(request):
    orders = Order.objects.filter(order_type=Order.CATERING)
    return render(request, 'shop/catering_orders.html', {'orders': orders})

# View for Payment Orders
def payment_orders(request):
    orders = Order.objects.filter(order_type=Order.PAYMENT)
    return render(request, 'shop/payment_orders.html', {'orders': orders})

# View to Create a New Order
# def create_order(request):
#     if request.method == 'POST':
#         # Handle the POST request and create an order based on the form
#         order_type = request.POST.get('order_type')
#         customer_name = request.POST.get('customer_name')
#         customer_email = request.POST.get('customer_email')
        
#         # Create and save the order
#         Order.objects.create(
#             order_type=order_type,
#             customer_name=customer_name,
#             customer_email=customer_email,
#         )
        
#         return redirect('order_success')  # Redirect to order_success page

#     return render(request, 'shop/create_order.html')

# # Order Success view (for redirection after order creation)
# def order_success(request):
#     return render(request, 'shop/order_success.html')


# shop/views.py

def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # Save the form data to create a new order
            form.save()
            messages.success(request, "Your message has been sent.")
            return redirect('order_success')  # Redirect to the order success page after saving
    else:
        form = OrderForm()  # Instantiate the form to display it for GET requests
    
    return render(request, 'shop/create_order.html', {'form': form})

# shop/views.py


# Order Success view (for redirection after order creation)
def order_success(request):
    return render(request, 'shop/order_success.html')

