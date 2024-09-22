from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def page_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
    return render(request, 'myapp/pageLogin.html')
  
def forgot_password_view(request):
    return render(request, 'myapp/forgotPassword.html')

def create_account_view(request):
    return render(request, 'myapp/createAccount.html')