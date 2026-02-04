from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from shop.models import Clothes, Order, Pos_order
from django.contrib.auth.decorators import login_required, permission_required
from .basket import Basket
from .forms import *

def basket_detail(request):
    basket = Basket(request)
    return render(request, 'basket/basket_detail.html', context={'basket': basket})

@permission_required(['shop.add_pos_order', 'shop.add_pos_order'])
def basket_remove(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Clothes, pk=product_id)
    basket.remove(product)
    return redirect('basket_detail')

def basket_clear(request):
    basket = Basket(request)
    basket.clear()
    return redirect('basket_detail')

@require_POST
def basket_add(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Clothes, pk=product_id)
    form = BasketAddProductForm(request.POST)
    if form.is_valid():
        basket.add(
            product=product,
            count=form.cleaned_data['count'],
            update_count=form.cleaned_data['reload']
        )
    return redirect('basket_detail')

@login_required
def basket_buy(request):
    basket = Basket(request)
    if basket.__len__() <= 0:
        return redirect('basket_detail')
    form = OrderForm(request.POST)
    if form.is_valid():
        order = Order.objects.create(
            buyer_firstname=form.cleaned_data['buyer_firstname'],
            buyer_name=form.cleaned_data['buyer_name'],
            buyer_surname=form.cleaned_data['buyer_surname'],
            comment=form.cleaned_data['comment'],
            delivery_address=form.cleaned_data['delivery_address'],
            delivery_type=form.cleaned_data['delivery_type']
        )

        for item in basket:
            pos_order = Pos_order.objects.create(
                clothes=item['product'],
                count=item['count'],
                order=order
            )
        basket.clear()
    return redirect('basket_detail')

@login_required
def open_order(request):
    return render(request, 'order/order_form.html', context={'form_order': OrderForm})