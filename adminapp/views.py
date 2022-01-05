from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from adminapp.forms import ShopUserAdminEditForm, ProductCategoryEditForm, ProductEditForm
from authapp.forms import ShopUserRegisterForm
from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product
from mainapp.views import get_same_products


class AccessMixin:

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class UserCreateView(AccessMixin, CreateView):
    model = ShopUser
    template_name = 'adminapp/user_form.html'
    form_class = ShopUserRegisterForm

    def get_success_url(self):
        return reverse('adminapp:user_list')


class UsersListView(AccessMixin, ListView):
    model = ShopUser
    template_name = 'adminapp/users.html'


class UserUpdateView(AccessMixin, UpdateView):
    model = ShopUser
    template_name = 'adminapp/user_form.html'
    form_class = ShopUserAdminEditForm

    def get_success_url(self):
        return reverse('adminapp:user_list')


class UserDelete(AccessMixin, DeleteView):
    model = ShopUser
    template_name = 'adminapp/user_delete.html'

    def get_success_url(self):
        return reverse('adminapp:user_list')


class CategoryCreate(AccessMixin, CreateView):
    model = ProductCategory
    template_name = 'adminapp/category_form.html'
    form_class = ProductCategoryEditForm

    def get_success_url(self):
        return reverse('adminapp:category_list')


class CategoryListView(AccessMixin, ListView):
    model = ProductCategory
    template_name = "adminapp/categories.html"


class CategoryUpdateView(AccessMixin, UpdateView):
    model = ProductCategory
    template_name = "adminapp/category_form.html"
    form_class = ProductCategoryEditForm

    def get_success_url(self):
        return reverse('adminapp:category_list')


class CategoryDeleteView(AccessMixin, DeleteView):
    model = ProductCategory
    template_name = 'adminapp/category_delete.html'

    def get_success_url(self):
        return reverse('adminapp:category_list')


# @user_passes_test(lambda u: u.is_superuser)
# def category_delete(request, pk):
#     current_category = get_object_or_404(ProductCategory, pk=pk)
#
#     if request.method == 'POST':
#         if current_category.is_active:
#             current_category.is_active = False
#         else:
#             current_category.is_active = True
#         current_category.save()
#         return HttpResponseRedirect(reverse('adminapp:category_list'))
#     context = {
#         'object': current_category
#     }
#     return render(request, 'adminapp/category_delete.html', context)


class ProductCreateView(AccessMixin, CreateView):
    model = Product
    template_name = 'adminapp/product_form.html'
    form_class = ProductEditForm

    def get_success_url(self):
        return reverse('adminapp:category_list', args=[self.kwargs.get('pk')])


class ProductsListView(AccessMixin, ListView):
    model = Product
    template_name = 'adminapp/products.html'

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data['category'] = get_object_or_404(ProductCategory, pk=self.kwargs.get('pk'))
        return context_data

    def get_queryset(self):
        return Product.objects.filter(category__pk=self.kwargs.get('pk'))


class ProductUpdateView(AccessMixin, UpdateView):
    model = Product
    template_name = 'adminapp/product_form.html'
    form_class = ProductEditForm

    def get_success_url(self):
        product_item = Product.objects.get(pk=self.kwargs.get('pk'))
        return reverse('adminapp:product_list', args=[product_item.category_id])


class ProductDeleteView(AccessMixin, DeleteView):
    model = Product
    template_name = 'adminapp/product_delete.html'

    def get_success_url(self):
        product_item = Product.objects.get(pk=self.kwargs.get('pk'))
        return reverse('adminapp:product_list', args=[product_item.category_id])


class ProductDetail(AccessMixin, DetailView):
    model = Product
    template_name = 'adminapp/product_detail.html'
