from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method == 'POST':
        if request.POST['pass'] == request.POST['repass']:
            try:
                user = User.objects.get(username = request.POST['username'])
                return render(request, 'account/signup.html', {'error' : 'Username not available'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password = request.POST['pass'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request, 'account/signup.html', {'error' : 'Passwords should be same.'})
    else:
        #Reenter
        return render(request, 'account/signup.html')

def signin(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['pass'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'account/signin.html',{'error' : 'Invalid details!'})
    else:
        return render(request, 'account/signin.html')

def signout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
