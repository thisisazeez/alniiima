from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.views.generic import TemplateView
# Create your views here.


class HomePageView(TemplateView):
    template_name = 'home.html'

def register(request):

    return render(request, 'register.html')

def card(request):
    return render(request, 'card.html')

def paid(request):
    return render(request, 'paid.html')

# def consultant(request):
#     return render(request, 'con.html')

def booking(request):
    return render(request, 'booking.html')

def disease(request):
    return render(request, 'de.html')

def about(request):
    return render(request, 'about.html')

def malairia(request):
    return render(request, 'ma.html')

def tuberclosis(request):
    return render(request, 'tu.html')

def fever(request):
    return render(request, 'fe.html')

def typhoid(request):
    return render(request, 'ty.html')

def diabetes(request):
    return render(request, 'di.html')

def hypertension(request):
    return render(request, 'hy.html')

def kidney_disease(request):
    return render(request, 'kid.html')

def heart_disease(request):
    return render(request, 'her.html')

def cancer(request):
    return render(request, 'can.html')
