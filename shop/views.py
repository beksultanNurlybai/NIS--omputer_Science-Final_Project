from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import CreateView

from django.contrib.auth.decorators import login_required

from .forms import *
from .models import *


def shop(request):
	goods = Goods.objects.all()
	if request.method == 'GET':
		form = SortFilterForm(request.GET)
		if form.is_valid():
			if request.GET.get('filt') == '0':
				goods = Goods.objects.all().order_by(request.GET.get('sort'))
			else:
				goods = Goods.objects.filter(type_of_goods__title=request.GET.get('filt')).order_by(request.GET.get('sort'))
	else:
		form = SortFilterForm()
	type_of_goods = Type_of_goods.objects.all()
	context = {
		'goods': goods,
		'type_of_goods': type_of_goods,
		'form': form,
	}
	return render(request, 'shop/shop.html', context)


def special(request, pk):
	goods = Goods.objects.filter(type_of_goods__pk=pk)
	if request.method == 'GET':
		form = SortFilterForm(request.GET)
		if form.is_valid():
			if request.GET.get('filt') == '0':
				goods = Goods.objects.all().order_by(request.GET.get('sort'))
			else:
				goods = Goods.objects.filter(type_of_goods__title=request.GET.get('filt')).order_by(request.GET.get('sort'))
	else:
		form = SortFilterForm()
	type_of_goods = Type_of_goods.objects.all()
	context = {
		'goods': goods,
		'type_of_goods': type_of_goods,
		'form': form,
	}
	return render(request, 'shop/shop.html', context)


def detail_of_good(request, pk):
	comments = Comments.objects.filter(good__pk=pk)
	if request.method == 'GET':
		form2 = SortCommentsForm(request.GET)
		if form2.is_valid():
			comments = Comments.objects.filter(good__pk=pk).order_by(request.GET.get('sort'))
	else:
		form2 = SortCommentsForm()

	if request.method == 'POST':
		form = CreateCommentsForm(request.POST)
		if form.is_valid():
			form.instance.user = request.user
			form.instance.good = Goods.objects.get(pk=pk)
			form.save()
	else:
		form = CreateCommentsForm()
	good = Goods.objects.get(pk=pk)
	type_of_goods = Type_of_goods.objects.all()
	context = {
		'form': form,
		'form2': form2,
		'good': good,
		'type_of_goods': type_of_goods,
		'comments': comments,
	}
	return render(request, 'shop/details.html', context)


def index(request):
	goods = Goods.objects.filter(pk__lte=8)
	type_of_goods = Type_of_goods.objects.all()
	context = {
		'goods': goods,
		'type_of_goods': type_of_goods,
	}
	return render(request, 'shop/index.html', context)

@login_required(login_url='login')
def account(request):
	return render(request, 'users/account.html')


def logoutPage(request):
	logout(request)
	return redirect('login')


def loginPage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Имя пользователья или пароль не правильны!')
	return render(request, 'users/login.html')


def registerPage(request):
	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, user + ' успешно был зарегистрирован!')
			return redirect('home')

	context = {'form': form}
	return render(request, 'users/register.html', context)
