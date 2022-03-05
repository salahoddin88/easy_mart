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
        cartProducts = Cart.objects.filter(user=request.user)
        carts = {}
        subTotal = 0
        shippingCost = 50
        for key, cartProduct in enumerate(cartProducts):
            productTotal = int(cartProduct.quantity) * int(cartProduct.product.price)
            subTotal += int(productTotal)
            carts[key] = {
                'product_image' : cartProduct.product.cover_image,
                'product_name' : cartProduct.product.name,
                'product_price' : cartProduct.product.price,
                'quantity' : cartProduct.quantity,
                'productTotal' : productTotal,
                'cart_id' : cartProduct.id
            }
        
        total = int(subTotal) + int(shippingCost)
        carts = list(carts.values())
        context = {
            'navigationProductCategories' : navigationProductCategories,
            'carts' : carts,
            'subTotal' : subTotal,
            'shippingCost' : shippingCost,
            'total' : total
        }
        return render(request, self.template_name, context)

    def post(self, request):
        cart_ids = request.POST.getlist('cart_id')
        quantities = request.POST.getlist('quantity')
        
        for key, cartId in enumerate(cart_ids):
            try:
                cart = Cart.objects.get(pk=cartId)
                if int(quantities[key]) == 0:
                    cart.delete()
                else:
                    cart.quantity = quantities[key]
                    cart.save()
            except Cart.DoesNotExist:
                pass
        
        return redirect('CartView')


class CheckoutView(View):
    template_name = 'checkout.html'

    def get(self, request):
        navigationProductCategories = ProductCategory.objects.filter(status=True)
        cartProducts = Cart.objects.filter(user=request.user)
        carts = {}
        subTotal = 0
        shippingCost = 50
        for key, cartProduct in enumerate(cartProducts):
            productTotal = int(cartProduct.quantity) * int(cartProduct.product.price)
            subTotal += int(productTotal)
            carts[key] = {
                'product_name' : cartProduct.product.name,
                'productTotal' : productTotal,
            }
        
        total = int(subTotal) + int(shippingCost)
        carts = list(carts.values())
        context = {
            'navigationProductCategories' : navigationProductCategories,
            'carts' : carts,
            'subTotal' : subTotal,
            'shippingCost' : shippingCost,
            'total' : total
        }
        return render(request, self.template_name, context)