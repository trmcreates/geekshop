from django.urls import path
from adminapp import views as admin_views

app_name = 'adminapp'

urlpatterns = [
    path('users/create/', admin_views.UserCreateView.as_view(), name='user_create'),
    path('users/', admin_views.UsersListView.as_view(), name='user_list'),
    path('users/update/<int:pk>/', admin_views.UserUpdateView.as_view(), name='user_update'),
    path('users/delete/<int:pk>/', admin_views.UserDelete.as_view(), name='user_delete'),

    path('categories/create/', admin_views.CategoryCreate.as_view(), name='category_create'),
    path('categories/', admin_views.CategoryListView.as_view(), name='category_list'),
    path('categories/update/<int:pk>/', admin_views.CategoryUpdateView.as_view(), name='category_update'),
    path('categories/delete/<int:pk>/', admin_views.CategoryDeleteView.as_view(), name='category_delete'),

    path('products/create/<int:pk>/', admin_views.ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/', admin_views.ProductsListView.as_view(), name='product_list'),
    path('products/update/<int:pk>/', admin_views.ProductUpdateView.as_view(), name='product_update'),
    path('products/delete/<int:pk>/', admin_views.ProductDeleteView.as_view(), name='product_delete'),
    path('products/detail/<int:pk>/', admin_views.ProductDetail.as_view(), name='product_detail'),
]