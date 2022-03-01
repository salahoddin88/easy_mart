from django.shortcuts import render, redirect
from django.views import View

from product.models import ProductCategory
from cart.models import Cart


class AddToCartView(View):
    def post(self, request):
        quantity = request.POST.get('quantity')
        product_id = request.POST.get('product_id')

        cart, isCreated = Cart.objects.get_or_create(product_id=product_id, user=request.user)
        if isCreated:
            cart.quantity = quantity
        else:
            cart.quantity = int(cart.quantity) + int(quantity)
        cart.save()
        # try:
        #     cart = Cart.objects.get(product_id=product_id, user=request.user)
        #     cart.quantity = int(cart.quantity) + int(quantity)
        #     cart.save()
        # except Cart.DoesNotExist:
        #     Cart.objects.create(
        #         quantity=quantity,
        #         product_id=product_id,
        #         user=request.user
        #     )
        return redirect('ProductDetailsView', product_id=product_id)


class CartView(View):
    template_name = 'cart.html'

    def get(self, request):
        navigationProductCategories = ProductCategory.objects.filter(status=True)
        carts = Cart.objects.filter(user=request.user)
        context = {
            'navigationProductCategories' : navigationProductCategories,
            'carts' : carts
        }
        return render(request, self.template_name, context)