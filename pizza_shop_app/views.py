from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .froms import UserForm, PizzaShopForm, UserFormForEdit, PizzaForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Pizza


def home(request):
    return redirect(pizza_shop_home)


@login_required(login_url='/sign-in/')
def pizza_shop_home(request):
    return redirect(pizza_shop_pizza)


@login_required(login_url='/sign-in/')
def pizza_shop_account(request):
    user_form = UserFormForEdit(instance=request.user)
    pizza_shop_form = PizzaShopForm(instance=request.user.pizza_shop)

    if request.method == 'POST':
        user_form = UserFormForEdit(request.POST, instance=request.user)
        pizza_shop_form = PizzaShopForm(request.POST, request.FILES, instance=request.user.pizza_shop)

        if user_form.is_valid() and pizza_shop_form.is_valid():
            user_form.save()
            pizza_shop_form.save()

    return render(request, 'pizzashop/account.html', {
        'user_form':user_form,
        'pizza_shop_form': pizza_shop_form
    })


@login_required(login_url='/sign-in/')
def pizza_shop_pizza(request):
    pizzas = Pizza.objects.filter(pizza_shop = request.user.pizza_shop).order_by('-id')
    return render(request, 'pizzashop/pizza.html', {
        'pizzas' : pizzas,
    })


@login_required(login_url='/sign-in/')
def pizza_shop_add_pizza(request):
    form = PizzaForm()
    if request.method == 'POST':
        form = PizzaForm(request.POST, request.FILES)
        if form.is_valid():
            pizza = form.save(commit=False)
            pizza.pizza_shop = request.user.pizza_shop
            pizza.save()
            return redirect(pizza_shop_pizza)
    return render(request, 'pizzashop/add_pizza.html', {
        'form':form,
    })


@login_required(login_url='/sign-in/')
def pizza_shop_edit_pizza(request, pizza_id):
    form = PizzaForm(instance=Pizza.objects.get(id= pizza_id))
    if request.method == 'POST':
        form = PizzaForm(request.POST, request.FILES,
                         instance=Pizza.objects.get(id=pizza_id))
        if form.is_valid():
            pizza = form.save()
            return redirect(pizza_shop_pizza)
    return render(request, 'pizzashop/edit_pizza.html', {
        'form':form,
    })


def pizza_shop_sing_up(request):
    user_form = UserForm()
    pizza_shop_form = PizzaShopForm()

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        pizza_shop_form = PizzaShopForm(request.POST, request.FILES)

        if user_form.is_valid() and pizza_shop_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)
            new_pizza_shop = pizza_shop_form.save(commit=False)
            new_pizza_shop.owner = new_user
            new_pizza_shop.save()

            login(request, authenticate(
                username = user_form.cleaned_data['username'],
                password = user_form.cleaned_data['password']
            ))

            return redirect(pizza_shop_home)

    return render(request, 'pizzashop/sign_up.html', {
        'user_form': user_form,
        'pizza_shop_form': pizza_shop_form
    })
