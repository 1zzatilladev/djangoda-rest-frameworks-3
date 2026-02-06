from django.shortcuts import render
from .models import Salom3,Salom4,Salom1,Salom2,Salom5
from .serializer import Salom1Sarializer,Salom2Sarializer,Salom3Sarializer,Salom4Sarializer,Salom5Serializer
from rest_framework.generics import  ListCreateAPIView, \
     RetrieveUpdateDestroyAPIView

#---------------------------
class Salom1ApiVIew(ListCreateAPIView):
    serializer_class = Salom1Sarializer
    queryset = Salom1.objects.all()


class Salom1DetailApiVIew(RetrieveUpdateDestroyAPIView):
    serializer_class = Salom1Sarializer
    queryset = Salom1.objects.all()

#---------------------------
class Salom2ApiVIew(ListCreateAPIView):
    serializer_class = Salom2Sarializer
    queryset = Salom2.objects.all()


class Salom2DetailApiVIew(RetrieveUpdateDestroyAPIView):
    serializer_class = Salom2Sarializer
    queryset = Salom2.objects.all()
#----------------------

class Salom3ApiVIew(ListCreateAPIView):
    serializer_class = Salom3Sarializer
    queryset = Salom3.objects.all()


class Salom3DetailApiVIew(RetrieveUpdateDestroyAPIView):
    serializer_class = Salom3Sarializer
    queryset = Salom3.objects.all()

#-------------------------
class Salom4ApiVIew(ListCreateAPIView):
    serializer_class = Salom4Sarializer
    queryset = Salom4.objects.all()


class Salom4DetailApiVIew(RetrieveUpdateDestroyAPIView):
    serializer_class = Salom4Sarializer
    queryset = Salom4.objects.all()

#---------------------------------
class Salom5ApiVIew(ListCreateAPIView):
    serializer_class = Salom5Serializer
    queryset = Salom5.objects.all()


class Salom5DetailApiVIew(RetrieveUpdateDestroyAPIView):
    serializer_class = Salom5Serializer
    queryset = Salom5.objects.all()