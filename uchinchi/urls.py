from django.urls import path , include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"salom1" , views.Salom1ModelViewSet)
router.register(r"salom2" , views.Salom2ModelViewSet)
router.register(r"salom3" , views.Salom3ModelViewSet)
router.register(r"salom4" , views.Salom4ModelViewSet)
router.register(r"salom5" , views.Salom5MarketLogModelViewSet)


urlpatterns = [
    path("",include(router.urls))
]