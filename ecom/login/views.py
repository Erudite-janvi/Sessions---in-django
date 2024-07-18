from .models import User
from .forms  import UserForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def user_create(request):
    form = UserForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return HttpResponse('logged in successfully')
    else:
        form = UserForm()
    return render(request,'loginform.html',{'form':form})    