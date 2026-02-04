from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import *
from .forms import *
from basket.forms import BasketAddProductForm
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import PermissionRequiredMixin

def first_view(request):
    return render(request, 'first.html')

def second_view(request):
    return render(request, 'second.html')


class ClothesListView(PermissionRequiredMixin, ListView):
    permission_required = 'shop.add_product'
    model = Clothes
    template_name = 'clothes/clothes_list.html'
    context_object_name = 'clothes'


class ClothesDetailView(DetailView):
    model = Clothes
    template_name = 'clothes/clothes_detail.html'
    context_object_name = 'clothes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_basket'] = BasketAddProductForm()
        return context

class ClothesCreateView(CreateView):
    model = Clothes
    form_class = ClothesForm
    template_name = 'clothes/clothes_form.html'
    success_url = reverse_lazy('clothes_list_view')


class ClothesUpdateView(UpdateView):
    model = Clothes
    form_class = ClothesForm
    template_name = 'clothes/clothes_form.html'
    success_url = reverse_lazy('clothes_list_view')

class ClothesDeleteView(DeleteView):
    model = Clothes
    context_object_name = 'clothes'
    template_name = 'clothes/clothes_confirm_delete.html'
    success_url = reverse_lazy('clothes_list_view')

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            return redirect('clothes_list_view')
    else:
        form = LoginForm()
    return render(request, 'auth/login.html', context={'form': form})


def registration_user(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            login(request, form.save())
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            return redirect('clothes_list_view')
    else:
        form = RegistrationForm()
    return render(request, 'auth/registration.html', context={'form': form})

def logout_user(request):
    logout(request)
    return redirect('clothes_list_view')