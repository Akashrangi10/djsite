from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from product.models import products
from django.template import loader

# Create your views here.
def index(request):
    latest_products_list = products.objects.order_by("-time_placed")[:5]
    context = {
        "latest_products_list": latest_products_list 
    }
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    return HttpResponse("you're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the result of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
