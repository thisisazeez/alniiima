from django.urls import path, include
from . import views
from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('register', views.register, name='register'),
    path('card', views.card, name='card'),
    path('paid', views.paid, name='paid'),
    path('disease', views.disease, name='disease'),
    path('booking', views.booking, name='booking'),
    path('about', views.about, name='about'),
    path('malairia', views.malairia, name='malairia'),
    path('tuberclosis', views.tuberclosis, name='tuberclosis'),
    path('fever', views.fever, name='fever'),
    path('typhoid', views.typhoid, name='typhoid'),
    path('diabetes', views.diabetes, name='diabetes'),
    path('hypertension', views.hypertension, name='hypertension'),
    path('kidney disaese', views.kidney_disease, name='kidney disease'),
    path('heart disease', views.heart_disease, name='heart disease'),
    path('cancer', views.cancer, name='cancer'),
    ]
