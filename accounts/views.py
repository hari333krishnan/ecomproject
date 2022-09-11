from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method == 'POST':
        user_name=request.POST['username']
        password1=request.POST['password1']
        password2 = request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=user_name).exists():
                messages.info(request, 'Username already taken!')
                return redirect('registration')
            elif user_name=='' or password1=='' or password2 =='':
                messages.info(request, 'Please enter details!')
                return redirect('registration')
            else:
                user = User.objects.create_user(username=user_name, password=password1,)
                user.save()
                return redirect('/')
        else:
            messages.info(request, 'Password not correct!')
            return redirect('registration')

    else:
        return render(request,'account.html')



def login(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        password1 = request.POST['password1']
        user = auth.authenticate(username=user_name, password=password1,)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials!')
            return redirect('login')
    else:
        return render(request, 'login.html')




def logout(request):
    auth.logout(request)
    return redirect('/')