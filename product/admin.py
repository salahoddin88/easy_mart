from django.contrib import admin, messages
from product.models import ProductCategory, Product, ProductImages


def active_status(modelAdmin, request, queryset):
    try:
        queryset.update(status=True)
        messages.success(request, 'Selected record(s) marked as active....')
    except Exception as e:
        messages.error(request, str(e))


def inactive_status(modelAdmin, request, queryset):
    try:
        queryset.update(status=False)
        messages.success(request, 'Selected record(s) marked as inactive....')
    except Exception as e:
        messages.error(request, str(e))



class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'status']
    list_filter = ('status', )
    search_fields = ('name', )
    actions = [active_status, inactive_status]

admin.site.register(ProductCategory, ProductCategoryAdmin)



class ProductImagesInline(admin.TabularInline):
    model = ProductImages

# class ProductImagesInline(admin.StackedInline):
#     model = ProductImages


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'product_category', 'price', 'stock', 'status')
    list_filter = ('status', 'product_category')
    search_fields = ('name', 'sku')
    actions = [active_status, inactive_status]
    inlines = (ProductImagesInline, )


admin.site.register(Product, ProductAdmin)



