from rest_framework.viewsets import ModelViewSet
from .serializer import Salom3Sarializer,Salom1Sarializer,Salom2Sarializer,Salom4Sarializer,Salom5Serializer
from .models import Salom3,Salom4,Salom1,Salom2,Salom5



class Salom3ModelViewSet(ModelViewSet):
    queryset = Salom3.objects.all()
    serializer_class = Salom3Sarializer

class Salom4ModelViewSet(ModelViewSet):
    queryset = Salom4.objects.all()
    serializer_class = Salom4Sarializer

class Salom1ModelViewSet(ModelViewSet):
    queryset = Salom1.objects.all()
    serializer_class = Salom1Sarializer


class Salom2ModelViewSet(ModelViewSet):
    queryset = Salom2.objects.all()
    serializer_class = Salom2Sarializer

class Salom5MarketLogModelViewSet(ModelViewSet):
    queryset = Salom5.objects.all()
    serializer_class = Salom5Serializer