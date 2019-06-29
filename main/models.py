from django.db import models
from django.conf import settings

from blog.models import *

User = settings.AUTH_USER_MODEL

class OrderItem(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, blank=True)
    product_tv = models.OneToOneField(Product_TV, on_delete=models.SET_NULL, null=True, blank=True)
    product_phone = models.OneToOneField(Product_Phone, on_delete=models.SET_NULL, null=True, blank=True)
    product_a_laptop = models.OneToOneField(Product_a_laptop, on_delete=models.SET_NULL, null=True, blank=True)
    slug = models.SlugField(blank=True)
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True)

    def __str__(self):
        return '{}'.format(self.product_tv, self.product_phone, self.product_a_laptop)


# class Order(models.Model):
#     ref_code = models.CharField(max_length=15)
#     user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, blank=True)
#     is_ordered = models.BooleanField(default=False)
#     items = models.ManyToManyField(OrderItem)
#     date_ordered = models.DateTimeField(auto_now=True)

#     def get_cart_items(self):
#         return self.items.all()

#     def __str__(self):
#         return self.ref_code




# class Cart(models.Model):
#     user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, blank=True)
#     orderitem = models.ManyToManyField(OrderItem, blank=True)
#     total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
#     updated = models.DateTimeField(auto_now=True)
#     mimestamp = models.DateTimeField(auto_now_add=True)

#     def get_absolute_url(self):
#         return reverse('cart_detail_url', kwargs={'slug': self.slug})

#     def __str__(sefl):
#         return str(sefl.id)