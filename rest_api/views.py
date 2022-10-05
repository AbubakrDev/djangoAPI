from django.shortcuts import render
from .models import *
from .serializers import KrosovkaAPI
from rest_framework.response import Response
from rest_framework.decorators import api_view , permission_classes
from rest_framework import permissions

def home(request):
    return render(request, 'home.html')

#Api ni to'liq chiqarish
@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def krosovkaMakeAPI(request):
    krosovka = Krosovka.objects.all()
    serializer = KrosovkaAPI(krosovka, many=True)
    return Response(serializer.data)

#Api ni id orqali chiqarish
@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def singleAPI(request, pk):
    krosovka = Krosovka.objects.get(id=pk)
    serializer = KrosovkaAPI(krosovka, many=False)
    return Response(serializer.data)

#post joylash,(ma'lumot joylash)
@api_view(["POST"])
@permission_classes((permissions.AllowAny, ))
def malumotJoylash(request):
    serializer = KrosovkaAPI(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

#post update qilish,(ma'lumot update qilish)
@api_view(["POST"])
@permission_classes((permissions.AllowAny, ))
def malumotUpdate(request, pk):
    krosovka = Krosovka.objects.get(id=pk)
    serializer = KrosovkaAPI(instance=krosovka, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)