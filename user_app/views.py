from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from user_app.models import UserCurrency
from user_app.forms import LoginForm, UserCreateForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User


class DemoPageView(View):

    def get(self, request):
        return render(request, 'demo_page.html')


class MainView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request):

        return render(request, 'main.html')


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', context={
                'form': form
            }
        )

    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            username = data.get('username')
            password = data.get('password')

            # authentication
            user = authenticate(
                username=username,
                password=password,
            )

            if user:
                # log in
                login(request, user)
                return redirect(reverse('hero_list'))
            else:
                return HttpResponse(f"Błąd uwierzytelnienia. Podano nieprawidłowe poświadczenia.")


class LogoutView(View):
    def get(self, request):
        logout(request)
        return render(
            request,
            'logout.html'
        )


class UserCreateView(View):

    def get(self, request):
        form = UserCreateForm()
        return render(
            request,
            'create_user.html',
            context={
                'form': form,
            }
        )

    def post(self, request):
        form = UserCreateForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            user = User.objects.create_user(
                username=data.get('login'),
                password=data.get('password'),
                first_name=data.get('first_name'),
                last_name=data.get('last_name'),
                email=data.get('email')
            )
            UserCurrency.objects.create(
                user=user
            )
            return redirect(reverse('login'))


class AboutView(View):
    pass


class TeamView(View):
    pass


class BankAccountView(View):
    pass


class SettingsView(View):
    pass