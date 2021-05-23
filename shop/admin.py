from django.contrib import admin

# Register your models here.
from .models import Product, FeedBack, Orders, OrderUpdate

admin.site.register(Product)
admin.site.register(FeedBack)
admin.site.register(Orders)
admin.site.register(OrderUpdate)
