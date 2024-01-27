from django.shortcuts import render,redirect
from .models import register

from .forms import registerform

def Sign_in(request):
    form=register(request.POST)
    form.save()

        

    return render(request,'forms.html',{'form':form})


    