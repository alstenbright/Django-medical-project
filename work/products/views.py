from django.shortcuts import render, redirect
from .forms import ProductForm
from django.shortcuts import render
from .models import Product
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='/login/')
def create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form =ProductForm()
    return render(request, 'create.html', {'form': form})

@login_required(login_url='/login/')
def read(request):
    product_list=Product.objects.all()
    return render(request,'retrieve.html',{'product_list':product_list})


def  user_check(user):
    return user.username.endswith('@gmail.com')
def update(request, id):
    product = Product.objects.get(pk=id)
    if request.method == 'POST':
        form = ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form =ProductForm(instance=product)           
    return render(request, 'update.html', {'form': form})


from django.shortcuts import render
def  user_check(user):
    return user.username.endswith('@gmail.com')
def delete(request,pk):
    product=Product.objects.get(pk=pk)  
    if request.method == 'POST':
        product.delete()
        return redirect('home')
    
    return render(request,'delete.html',{'product':product})

from django.shortcuts import render
from .models import Product
@login_required(login_url='/login/')
def medical_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
        product_list = Product.objects.filter(medical_name__istartswith=search_query)
    else:
        product_list = Product.objects.all()

    return render(request, 'product_list.html', {'product_list': product_list, 'search_query': search_query})



