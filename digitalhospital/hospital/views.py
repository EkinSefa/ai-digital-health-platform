from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
import requests



def index(request):
    return render(request,"hospital/index.html")

# def home(request):
#     return render(request,"hospital/index.html")
# # Create your views here.

def home(request):
    api_key = "b1911a4a91e14cfea476041a2ee69611"
    url = f"https://newsapi.org/v2/top-headlines?country=us&category=health&apiKey={api_key}"

    haberler = []
    try:
        response = requests.get(url)
        data = response.json()
        if data["status"] == "ok":
            haberler = data["articles"]
    except Exception as e:
        print("Haber API hatası:", e)

    return render(request, "hospital/index.html", {"haberler": haberler})
