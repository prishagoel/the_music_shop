from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from .models import UserInfo, Guitar, Piano, Drums, Violin
from .serializers import UserInfoserializer, Guitarserializer, Pianoserializer, Drumsserializer, Violinserializer
# Create your views here.

def music1(request):

    recs = UserInfo.objects.all
    #records = UserInfoserializer(recs, many = True)
    return render(request, "login.html", {'records':recs})

def home(request):
    return render(request, "page1.html")

def signup(request):
    print("signup() called, method: ", request.method)
    print(request.POST)
    if request.method == "POST":
        name = request.POST.get('username', False)
        passw = request.POST.get('password', False)
        em = request.POST.get('email', False)
        num = request.POST.get('phone', False)
        record = UserInfo(Name = name, Phoneno = num, Email = em, Passwd = passw)
        record.save()
    return render(request, "signup.html")

def drums(request):
    return render(request, "drums.html")