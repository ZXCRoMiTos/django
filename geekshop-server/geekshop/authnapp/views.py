from django.shortcuts import render, HttpResponseRedirect
from authnapp.forms import ShopUserLoginForm, ShopUserCreationForm, ShopUserChangeForm
from django.contrib import auth
from django.urls import reverse


def login(request):
    title = 'вход'

    login_form = ShopUserLoginForm(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main:index'))
    else:
        login_form = ShopUserLoginForm()

    content = {'title': title, 'login_form': login_form}
    return render(request, 'authnapp/login.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


def register(request):
    title = 'регистрация'

    if request.method == 'POST':
        register_form = ShopUserCreationForm(request.POST, request.FILES)
        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = ShopUserCreationForm()

    content = {'title': title, 'register_form': register_form}
    return render(request, 'authnapp/register.html', content)


def edit(request):
    title = 'редактирование'

    if request.method == 'POST':
        form = ShopUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = ShopUserChangeForm(instance=request.user)

    content = {'title': title, 'form': form}
    return render(request, 'authnapp/update.html', content)