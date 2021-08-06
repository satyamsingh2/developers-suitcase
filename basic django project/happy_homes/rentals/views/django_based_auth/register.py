from django.shortcuts import render, redirect
from happy_homes.rentals.serilizers.django_based_auth.register import CreateUserForm
from django.contrib import messages
from django.contrib.auth import login,logout, authenticate


"""func based user auth which is pre-defined in django"""

def register_page(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            messages.success(request, f"Account was successfully created for {user}")
            return redirect('login')
    context = {'form': form}
    return render(request, 'accounts/register.html', context)   # http://127.0.0.1:8000/register/


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('owner-list')
        else:
            messages.info(request, "Username or password is incorrect")

    context = {}
    return render(request, 'accounts/login.html', context)

def logout_page(request):
    logout(request)
    return redirect('login')
