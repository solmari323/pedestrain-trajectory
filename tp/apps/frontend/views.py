from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    response = {
        "datasets": [{'name': "UCY(University)"},
                    {'name': "UCY(Zara)"},
                    {'name': "ETH 1"},
                    {'name': "ETH 2"},
                    {'name':'Stanford Drone'}
                    ]
        }
    return render(request, "index.html", response)
