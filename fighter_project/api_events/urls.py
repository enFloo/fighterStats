from .views import *
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('', home),
    path('accounts/', include('allauth.urls')),
    path('home/', TemplateView.as_view(template_name='dashboard/home.html'), name = 'home'),
    

]