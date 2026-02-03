from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path("certifications/", views.certifications, name="certifications"),
    path('lead/', views.lead, name='lead'),
]
