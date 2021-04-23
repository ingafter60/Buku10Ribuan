# app/ecommerce/AdminViews.py
from django.shortcuts import render

def admin_home(request):
    return render(request,"admin/home.html")