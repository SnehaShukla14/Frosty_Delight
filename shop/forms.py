# shop/forms.py
from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['order_type', 'customer_name', 'customer_email']
