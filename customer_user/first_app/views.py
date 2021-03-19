from django.shortcuts import render, redirect
from first_app.forms import CustomerForm
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
def register(request):
    if request.method == "POST":
        custform = CustomerForm(data=request.POST)
        if custform.is_valid():
            cust = custform.save()
            cust.set_password(cust.password)
            cust.save()
            return HttpResponse("Registration Done")
    else:
        custform = CustomerForm()
    return render(request, 'register.html',{'custform':custform})




def user_login(request):
    if request.user.is_authenticated:
        return redirect('logout')
    else:
        if request.method== 'POST':
            email = request.POST.get("email")
            password = request.POST.get("password")

            user = authenticate(request, username=email,password=password)

            if user is not None:
                if user.is_active:
                    request.session['user_id'] = request.user.id
                    login(request, user)
                    return render(request, 'logout.html')
                else:
                    return render(request, 'login.html')
            else:
                return render(request, 'login.html')
        return render(request, 'login.html',{})


@ login_required
def user_logout(request):
    request.session.flush()
    logout(request)
    return HttpResponseRedirect(reverse('first_app:login'))
