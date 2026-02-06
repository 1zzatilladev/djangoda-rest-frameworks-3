from django.urls import path
from .views import Salom1ApiVIew,Salom2ApiVIew,Salom3ApiVIew,Salom4ApiVIew,Salom5ApiVIew , Salom1DetailApiVIew, \
Salom2DetailApiVIew , Salom3DetailApiVIew ,Salom4DetailApiVIew ,Salom5DetailApiVIew
   
urlpatterns = [
    path('salom1/',Salom1ApiVIew.as_view()),
    path('salom2/',Salom2ApiVIew.as_view()),
    path('salom3/',Salom3ApiVIew.as_view()),
    path('salom4/',Salom4ApiVIew.as_view()),
    path('salom5/',Salom5ApiVIew.as_view()),
    path('salom1/<int:pk>/', Salom1DetailApiVIew.as_view()),
    path('salom2/<int:pk>/', Salom2DetailApiVIew.as_view()),
    path('salom3/<int:pk>/', Salom3DetailApiVIew.as_view()),
    path('salom4/<int:pk>/', Salom4DetailApiVIew.as_view()),
    path('salom5/<int:pk>/', Salom5DetailApiVIew.as_view()),
]
