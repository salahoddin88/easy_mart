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
        search = request.GET.get('search')
        sorting = request.GET.get('sorting')
        minPrice = request.GET.get('min')
        maxPrice = request.GET.get('max')

        searchDict = {
            'status' : True,
        }

        if category_id and category_id != 'None':
            searchDict['product_category_id'] = category_id

        if search:
            searchDict['name__contains'] = search

        if minPrice:
            minPrice = int(minPrice.replace('₹', ''))
            searchDict['price__gte'] = minPrice

        if maxPrice:
            maxPrice = int(maxPrice.replace('₹', ''))
            searchDict['price__lte'] = maxPrice

        if sorting == 'low':
            products = Product.objects.filter(**searchDict).order_by('price')
        elif sorting == 'high':
            products = Product.objects.filter(**searchDict).order_by('-price')
        else:
            products = Product.objects.filter(**searchDict)
        context = {
            'navigationProductCategories' : navigationProductCategories,
            'products' : products,
            'category_id' : category_id
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


