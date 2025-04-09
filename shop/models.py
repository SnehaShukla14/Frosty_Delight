from django.db import models

# Create your models here.

class Order(models.Model):
    DELIVERY = 'delivery'
    CATERING = 'catering'
    PAYMENT = 'payment'
    
    ORDER_TYPES = [
        (DELIVERY, 'Delivery'),
        (CATERING, 'Catering'),
        (PAYMENT, 'Payment'),
    ]
    
    order_type = models.CharField(
        max_length=20,
        choices=ORDER_TYPES,
        default=DELIVERY,
    )
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')
    
    def __str__(self):
        return f"{self.customer_name} - {self.order_type} - {self.status}"

