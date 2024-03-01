from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Question, Choice, MainNews
from product.models import products
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as login_ , logout 
from django.conf import settings
import os
import json

# Create your views here.
def index(request):
    respose_list = []
    all_main_news = MainNews.objects.values_list("title", "head_text", "description", "created_date", "news_image").order_by("id")[:5]
    for data in all_main_news:
        respose_list.append({
            "title": data[0],
            "head_text": data[1],
            "description": data[2],
            "created_date": data[3],
            "news_image": os.path.join("/" + settings.MEDIA_ROOT, "News/head/" + data[4].split("/")[-1]),
        })
    context = {
        "latest_news_list": respose_list
    }
    return render(request, "polls/index.html", context)

def save_news(request):
    title = request.POST.get("")
    return HttpResponse(json.dumps({"code": 1, "msg": "Successsssssssss"}),content_type = "json")

def dome(request):
    return render(request, "polls/demo.html")