from rest_framework.serializers import ModelSerializer
from .models import Salom3,Salom4,Salom1,Salom2,Salom5
class Salom5Serializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Salom5
class Salom3Sarializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Salom3

class Salom1Sarializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Salom1
class Salom4Sarializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Salom4

class Salom2Sarializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Salom2