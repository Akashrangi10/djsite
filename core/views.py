from django.shortcuts import render

# Create your views here.

def core_index_view(request):
    return render(request, "core/core_index.html", {})
