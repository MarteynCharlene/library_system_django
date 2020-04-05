from django.shortcuts import render, reverse, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth import authenticate
from . models import PasswordResetRequest

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'login_app/register.html', {'form': form})

def request_password_reset(request):
 if request.method == "POST":
     post_user = request.POST['username']
     user = None

     if post_user:
         try:
             user = User.objects.get(username=post_user)
         except:
             print(f"Invalid password request: {post_user}")
     else:
         post_user = request.POST['email']
         try:
             user = User.objects.get(email=post_user)
         except:
             print(f"Invalid password request: {post_user}")
     if user:
         prr = PasswordResetRequest()
         prr.user = user
         prr.save()
         print(prr)
         return redirect('password_reset')

 return render(request, 'login_app/request_password_reset.html')

def password_reset(request):
    if request.method == "POST":
        post_user = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        token = request.POST['token']

        if password == confirm_password:
            try:
                prr = PasswordResetRequest.objects.get(token=token)
                prr.save()
            except:
                print("Invalid password reset attempt.")
                return render(request, 'login_app/password_reset.html')
                
            user = prr.user
            user.set_password(password)
            user.save()
            return redirect('login')


    return render(request, 'login_app/password_reset.html')

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'login_app/profile.html', context)


@login_required
def delete_account(request):
    if request.method == "POST":
        if request.POST['confirm_deletion'] == "DELETE": 
            user = authenticate(request, username=request.user.username, password=request.POST['password']) 
            if user: 
                print(f"Deleting user {user}")
                user.delete()
                return redirect('login')
            else:
                print("fail delete")

    return render(request, 'login_app/delete_account.html')

