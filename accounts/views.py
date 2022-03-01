from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

from product.models import ProductCategory


class LoginView(View):

    template_name = 'login.html'
    form_class = AuthenticationForm
    navigationProductCategories = ProductCategory.objects.filter(status=True)

    def get(self, request):

        form = self.form_class()
        context = {
            'navigationProductCategories' : self.navigationProductCategories,
            'form' : form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('HomeView')
        
        context = {
            'navigationProductCategories' : self.navigationProductCategories,
            'form' : form
        }
        return render(request, self.template_name, context)


def LogoutView(request):
    logout(request)
    return redirect('HomeView')

# class LogoutView(View):
#     def get(self, request):
#         logout(request)
#         print('Hello')
#         return redirect('HomeView')