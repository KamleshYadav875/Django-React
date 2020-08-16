from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .serializers import RegisterSerializer,NSEBSEDataSerializer,CompanyDataSerializer, UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['POST'])
def register_view(request):

    serialzier = RegisterSerializer(data= request.data)
    data ={}
    if serialzier.is_valid():
        user = serialz
        data['responce'] = "User cier.save()reated successfully"
    else:
        data = serialzier.errors
    return Response(data)


@api_view(["GET"])
def getData(request, data):
    output = None
    d = { "data" : data }
    seri = NSEBSEDataSerializer(data = d)
    if seri.is_valid():
        output = seri.getData(d)
        return Response(output)
    else:
        output = seri.errors
    
    return Response(output)
    
@api_view(["GET"])
def getCompanyData(request, data):
    output = None
    d = { "data" : data }
    seri = CompanyDataSerializer(data = d)
    if seri.is_valid():
        output = seri.getData(d)
        return Response(output)
    else:
        output = seri.errors
    
    return Response(output)
    
