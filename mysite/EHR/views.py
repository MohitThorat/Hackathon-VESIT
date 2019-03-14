from django.shortcuts import render
from .forms import Signup,Login
# Create your views here.

def Get(request):
    form = Login()
    return render(request,'EHR/Home.html',{'form':form})
def SignUp(request):
    form = Signup()
    return render(request,'EHR/Signup.html',{'form':form})
#def Get(request):
 #   form = HomeForm()
  #  return render(request,'EHR/Home.html',{'form':form})
def HomePage(request):
    form = HomeForm

