from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Question
from product.models import products
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as login_ , logout 


# Create your views here.
def index(request):
    latest_products_list = products.objects.order_by("-time_placed")[:5]
    context = {
        "latest_products_list": latest_products_list 
    }
    return render(request, "polls/index.html", context)

def register_view(request):
    return render(request, "polls/register.html")

def login_view(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['password']

        user = authenticate(request,username = username,password = password)

        if user:
            login_(request,user)
            return redirect('index')
        else:
            return redirect('login_view')
    return render(request, "polls/login.html")

# Logout
def logout_view(request):
    logout(request)
    return redirect ('index')

def detail(request, question_id):
    return HttpResponse("you're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the result of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
