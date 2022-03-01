from django.shortcuts import render, redirect
from django.views import View
from product.models import Product, ProductCategory, ProductImages


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



class ProductDetailsView(View):
    template_name = 'product-details.html'

    def get(self, request, product_id=None):
        navigationProductCategories = ProductCategory.objects.filter(status=True)
        try:
            product = Product.objects.get(id=product_id)

        except Product.DoesNotExist:
            return redirect('HomeView')

        productImages = ProductImages.objects.filter(product_id=product_id)
        relatedProducts = Product.objects.filter(product_category_id=product.product_category_id).exclude(id=product_id)
        context = {
            'navigationProductCategories' : navigationProductCategories,
            'product' : product,
            'productImages' : productImages,
            'relatedProducts' : relatedProducts
        }
        return render(request, self.template_name, context)