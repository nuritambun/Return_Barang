from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PembeliViewSet, PesananViewSet,
    ReturBarangViewSet, PengembalianDanaViewSet
)

router = DefaultRouter()
router.register(r'pembeli', PembeliViewSet)
router.register(r'pesanan', PesananViewSet)
router.register(r'retur', ReturBarangViewSet)
router.register(r'pengembalian-dana', PengembalianDanaViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]