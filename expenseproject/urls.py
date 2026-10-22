"""
URL configuration for expenseproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from expenceApp import views
from rest_framework.authtoken import views as auth_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user',views.UserCreationView.as_view(),name="user_view"),
    path('expense',views.ExpenceCreateListView.as_view(),name="expense_view"),
    path('expense/<int:pk>',views.ExpenceRetrieveUpdateDeleteView.as_view(),name='expense_rud'),
    path('token',auth_view.obtain_auth_token),

]
