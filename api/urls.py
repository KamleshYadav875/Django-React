from django.urls import path
from .views import register_view, getData, getCompanyData, UserViewSet
from rest_framework import routers
from django.conf.urls import include

router = routers.DefaultRouter()
router.register('users', UserViewSet)
app_name = 'frontEnd'

urlpatterns = [
    path('', include(router.urls)),
    path('register', register_view, name="register"),
    path('get-data/<str:data>/', getData, name="get-data"),
    path('company-data/<str:data>/', getCompanyData, name="get-company-data"),
    
]
