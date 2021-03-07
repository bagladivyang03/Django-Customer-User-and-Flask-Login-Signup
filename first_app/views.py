from django.shortcuts import render
from first_app.forms import CustomerForm
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.
def register(request):
    registered = False
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