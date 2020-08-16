from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path("", views.index, name="loginPage" ),
    path("register/", views.register),
    path("dashboard/", TemplateView.as_view(template_name='index.html'), name="dashboard"),
    path("logoutPage/", views.logoutPage, name="logoutPage"),
]
