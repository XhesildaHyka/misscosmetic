from django.contrib import admin
from .models import *

admin.site.register(CarouselImage)
admin.site.register(Arrival)
admin.site.register(Contact)
# admin.site.register(Product)
admin.site.register(Marka)
admin.site.register(Makeup)
admin.site.register(Skincare)
admin.site.register(Accessor)
admin.site.register(Offer)
admin.site.register(Video)
admin.site.register(Collection)
# admin.site.register(Cart)



class CartInline(admin.TabularInline):
    model = Order.orderitems.through  # Use the through model for ManyToManyField
    extra = 0  # Do not show extra empty rows



class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'actual_price')
    search_fields = ('name',)
    
admin.site.register(Product, ProductAdmin)

class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'item', 'quantity', 'purchased', 'updated')
    list_filter = ('purchased',)
    search_fields = ('user__username', 'item__name')
    
admin.site.register(Cart, CartAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone', 'created', 'total_price')
    search_fields = ('full_name', 'phone')
    inlines = [CartInline]  # This will display cart items in the order admin

    def total_price(self, obj):
        return obj.get_totals()
    total_price.short_description = 'Total Amount'

admin.site.register(Order, OrderAdmin)
