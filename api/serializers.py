from rest_framework import serializers
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.exceptions import ValidationError
import pandas as pd
from django.contrib.auth import authenticate, login
from rest_framework.validators import UniqueTogetherValidator
from rest_framework.authtoken.models import Token
import json


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True, 'required':True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password', 'email']
    
    def save(self):
        user = User(
            email = self.validated_data['email'],
            username = self.validated_data['username']
        ) 
        user.set_password(self.validated_data["password"])
        user.save()
        return user


class NSEBSEDataSerializer(serializers.Serializer):
    def getData(self, data):
        loadCsv = None
        if data['data'] == "NSE":
            loadCsv = pd.read_csv("./Data/NSE (Nifty).csv")
        elif data['data'] == "BSE":
            loadCsv = pd.read_csv("./Data/BSE (Sensex).csv")
        # loadCsv.reset_index(drop=True, inplace=True)
        
        loadCsv = loadCsv.iloc[-2:]
        result = loadCsv.to_json(orient="split")
        parsed = json.loads(result)
        return parsed


class CompanyDataSerializer(serializers.Serializer):
    def getData(self, data):
        loadCsv = None
        if data['data'] == "Reliance":
            loadCsv = pd.read_csv("./Data/RELIANCE.NS.csv")
            
        elif data['data'] == "AshokLeyland":
            loadCsv = pd.read_csv("./Data/ASHOKLEY.NS.csv")
        
        elif data['data'] == "Cipla,":
            loadCsv = pd.read_csv("./Data/CIPLA.NS.csv")
        
        elif data['data'] == "TataSteel":
            loadCsv = pd.read_csv("./Data/TATASTEEL.NS.csv")
        
        elif data['data'] == "EicherMotors":
            loadCsv = pd.read_csv("./Data/EICHERMOT.NS.csv")
        
        closePrice = loadCsv["Close"]
        dict  = loadCsv.set_index('Date')['Close'].to_dict()
        cp = json.dumps(dict)
        return cp


    
    