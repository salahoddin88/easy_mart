from django.contrib import admin
from . models import Order, OrderDetails


class OrderDetailsInline(admin.TabularInline):
    model = OrderDetails
    extra = 1
    classes = ['collapse']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'date_time', 'payment', 'status']
    list_filter = ['payment', 'status']
    search_fields = ['id', 'name']
    date_hierarchy = 'date_time'
    inlines = [OrderDetailsInline]


admin.site.register(Order, OrderAdmin)