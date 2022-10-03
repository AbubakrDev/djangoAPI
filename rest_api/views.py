from django.shortcuts import render
from .models import *
from .serializers import KrosovkaAPI
from rest_framework.response import Response
from rest_framework.decorators import api_view , permission_classes
from rest_framework import permissions

def home(request):
    return render(request, 'home.html')

@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def krosovkaMakeAPI(request):
    krosovka = Krosovka.objects.all()
    serializer = KrosovkaAPI(krosovka, many=True)
    return Response(serializer.data)

@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def singleAPI(request, pk):
    krosovka = Krosovka.objects.get(id=pk)
    serializer = KrosovkaAPI(krosovka, many=False)
    return Response(serializer.data)