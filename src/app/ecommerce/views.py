# app/ecommerce/views.py
from django.shortcuts import render

# Create your views here.
def admin_login(request):
    return render(request,"admin/signin.html")	