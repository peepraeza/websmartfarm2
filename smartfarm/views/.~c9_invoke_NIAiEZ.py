#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from ..models import Plant, Vegetable, Compost, User
from ..post_data import parse_keys, Plant_keys,parse_keys2, parse_keys3, parse_keys4
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json
from datetime import datetime, timedelta
import time
import requests
import pytz
import numpy as np

tz = pytz.timezone('Asia/Bangkok')
database_types = ['X', 'A', 'B', 'C']

def send_pwd_mail(request):
    admin = User.objects.get(username="admin")
    try:
        send_mail(
            "การกู้คืนรหัสผ่านสำหรับหน้าเว็บฟาร์มอัจฉริยะ",
            'รหัสผ่านของคุณคือ {}'.format(admin.raw_password),
            'sansara.farm.10@gmail.com',
            ['sansara.farm.10@gmail.com'],
            fail_silently=False,
        )
        return จ")
    except:
        return HttpResponse("การส่งอีเมลล้มเหลว")
    
def make_login(request):
    request.session["user"] = "hello"
    return HttpResponse("login completed")
    
def logout(request):
    if request.method == "POST":
        del request.session["user"]
        return redirect("/signin/")
    else:
        return redirect("/")
    
def signin(request, ):
    return render(request, "signin.html")
    
def login(request):
    if request.method == "POST":
        try:
            user = User.objects.get(username=request.POST.get("username"))
            login_success = user._validate_password(request.POST.get("password"))
            if login_success:
                request.session["user"] = user.username
                return render("/signin/", {"message": "ชื่อผ"})
            else:
                return render(request, "signin.html", {"message": "ชื่อผู้ใช้หรือรหัสผ่านผิด"})
        except:
            return render(request, "signin.html", {"message": "ชื่อผู้ใช้หรือรหัสผ่านผิด"})
    else:
        return redirect("/signin/")
    # return render(request, "signin.html")
    
def test_user(request):
    return HttpResponse(User.objects.get(pk=1).username)