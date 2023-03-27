from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from user_app.models import UserCurrency
from user_app.forms import LoginForm, UserCreateForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User


class DemoPageView(View):  # This class-based view returns a demo page to the client.

    def get(self, request):
        return render(request, 'demo_page.html')


class MainView(LoginRequiredMixin, View):  # This view is responsible for handling requests to the main page.
    login_url = reverse_lazy('login')

    def get(self, request):

        return render(request, 'main.html')


class LoginView(View):  # This class-based view handles requests for the login page.
    def get(self, request): # The GET method returns the login form.
        form = LoginForm()

        return render(request, 'login.html', context={
                'form': form
            }
        )

    def post(self, request):  # The POST method authenticates the user and redirect to hero list page.
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
                return redirect(reverse('login'))


class LogoutView(View):  # This view logs the user out of the application and returns a logout page to the client.
    def get(self, request):
        logout(request)

        return render(
            request,
            'logout.html'
        )


class UserCreateView(View):  # This view is responsible for handling user registration requests.

    def get(self, request):  # The GET method returns the form to create a new user.
        form = UserCreateForm()

        return render(
            request,
            'create_user.html',
            context={
                'form': form,
            }
        )

    def post(self, request):  # The POST method creates a new user if the form is valid.
        form = UserCreateForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            if User.objects.get(username=data.get('login')):
                return redirect(reverse('register'))

            user = User.objects.create_user(
                username=data.get('login'),
                password=data.get('password'),
                first_name=data.get('first_name'),
                last_name=data.get('last_name'),
                email=data.get('email')
            )

            # The user's currency information is also created in the process.
            UserCurrency.objects.create(
                user=user
            )

            return redirect(reverse('login'))


class AboutView(View):

    def get(self, request):
        return redirect(reverse('main_site'))


class TeamView(View):

    def get(self, request):
        return redirect(reverse('main_site'))


class BankAccountView(View):

    def get(self, request):
        return redirect(reverse('main_site'))


class SettingsView(View):

    def get(self, request):
        return redirect(reverse('main_site'))
