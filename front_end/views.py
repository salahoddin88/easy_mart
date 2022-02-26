from django.shortcuts import render
from django.views import View
from product.models import Product, ProductCategory


class HomeView(View):
    template_name = 'home.html'

    def get(self, request):
        navigationProductCategories = ProductCategory.objects.filter(status=True)
        featuredProductCategories = ProductCategory.objects.filter(status=True).order_by('-id')[:4]
        context = {
            'navigationProductCategories' : navigationProductCategories,
            'featuredProductCategories' : featuredProductCategories
        }
        return render(request, self.template_name, context)


class ProductListView(View):
    template_name = 'product-list.html'

    def get(self, request, category_id=None):
        navigationProductCategories = ProductCategory.objects.filter(status=True)
        products = Product.objects.filter(status=True, product_category_id=category_id)
        context = {
            'navigationProductCategories' : navigationProductCategories,
            'products' : products
        }
        return render(request, self.template_name, context)
