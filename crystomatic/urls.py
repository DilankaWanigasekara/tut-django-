"""crystomatic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views
from calculator import views as cal

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vehicle/', views.getVehicle),
    path('person/', views.getPerson),
    path('vehicle/<int:id>/', views.getVehiclebyId),
    path('add/<int:num1>/<int:num2>/', views.addNumbers),
    path('ad/<int:num1>/<int:num2>/', cal.addnumber),
    path('substract/<int:num1>/<int:num2>/',cal.reducenumber),
    path('multiply/<int:num1>/<int:num2>/',cal.multiplynumber),
    path('devide/<int:num1>/<int:num2>/',cal.devidenumber)
]
