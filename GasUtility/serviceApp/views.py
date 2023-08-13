from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

def index(request):
    return HttpResponse("Hello, world. You're at the app index.")

@login_required
def home(request):
    return HttpResponse("Hello, world. You're at the Home index.")
