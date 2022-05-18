from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def forms(request):
    if request.method== 'POST':
        username=request.POST['username']

        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return render(request,"forms.html")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email Taken")
                return render(request, "forms.html")


            else:

                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()
                print("N")
                return redirect('login')

        else:
            messages.info(request,"Password Not Match")
            return render(request,"forms.html")



    return render(request,"forms.html")
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')




        else:
            messages.info(request, "incorrect")
            return redirect('login')
    return render(request, "login.html")
def logout(request):
    auth.logout(request)
    return redirect('/')




