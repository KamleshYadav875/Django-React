from django.urls import path
from frontEnd.api.views import register_view

app_name = 'frontEnd'

urlpatterns = [
    path('register', register_view, name="register"),
]
