from django.shortcuts import render,redirect
from .forms import ProductForm
from .models import Product

# Create your views here.

# Home Page
def home_page(request):
    return render(request, template_name='imsApp/home_page.html', context={'title':'Home'})



# Create Product Page
def create_product_page(request):
    create_product_form = ProductForm()
    if request.method == 'POST':
        create_product_form = ProductForm(request.POST)
        if create_product_form.is_valid():
            create_product_form.save()
            return redirect('product_list')
    return render(request, template_name='imsApp/product_form.html', context={'title':'Product Form', 'create_product_form':create_product_form})


# Read Product Page
def read_product_page(request):
    products = Product.objects.all()
    return render(request, template_name='imsApp/product_list.html', context={'title':'Product List', 'products':products})


# Update Product Page
def update_product_page(request, product_id):
    current_product = Product.objects.get(product_id=product_id)
    
    if request.method == 'POST':
        updated_product_form = ProductForm(request.POST, instance=current_product)
        if updated_product_form.is_valid():
            updated_product_form.save()
            return redirect('product_list')
    else:
        product = ProductForm(instance=current_product)
    
    return render(request, template_name='imsApp/product_list.html', context={'title':'Update Product', 'product':product})


# Delete Product
def delete_product_page(request, product_id):
    current_product = Product.objects.get(product_id=product_id)
    
    if request.method == 'POST':
        current_product.delete()
        return redirect('product_list')
    
    return render(request, template_name='imsApp/product_confirm_delete.html', context={'title':'Delete Product'})