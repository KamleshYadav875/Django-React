from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from frontEnd.api.serializers import RegisterSerializer

@api_view(['POST'])
def register_view(request):
    if request.method == "POST":
        serialzier = RegisterSerializer(data= request.data)
        data ={}
        if serialzier.is_valid():
            user = serialzier.save()
            data['responce'] = "User created successfully"
        else:
            data = serialzier.errors
        return Response(data)