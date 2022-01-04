from django.shortcuts import render, get_object_or_404

# Create your views here.
from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product


def user_create(request):
    context = {

    }
    return render(request, '', context)


def users(request):
    context = {
        'object_list': ShopUser.objects.all().order_by('-is_active')
    }
    return render(request, 'adminapp/users.html', context)


def user_update(request):
    context = {

    }
    return render(request, '', context)


def user_delete(request):
    context = {

    }
    return render(request, '', context)


def category_create(request):
    context = {

    }
    return render(request, '', context)


def categories(request):
    context = {
        'object_list': ProductCategory.objects.all().order_by('-is_active')
    }
    return render(request, 'adminapp/categories.html', context)


def category_update(request):
    context = {

    }
    return render(request, '', context)


def category_delete(request):
    context = {

    }
    return render(request, '', context)


def product_create(request):
    context = {

    }
    return render(request, '', context)


def products(request, pk):
    context = {
        'category': get_object_or_404(ProductCategory, pk=pk),
        'object_list': Product.objects.filter(category__pk=pk).order_by('-is_active')
    }
    return render(request, 'adminapp/products.html', context)


def product_update(request):
    context = {

    }
    return render(request, '', context)


def product_delete(request):
    context = {

    }
    return render(request, '', context)


def product_detail(request):
    context = {

    }
    return render(request, '', context)
