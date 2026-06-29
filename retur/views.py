from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Pembeli, Pesanan, ReturBarang, PengembalianDana
from .serializers import (
    PembeliSerializer, PesananSerializer,
    ReturBarangSerializer, PengembalianDanaSerializer
)


class PembeliViewSet(viewsets.ModelViewSet):
    queryset = Pembeli.objects.all()
    serializer_class = PembeliSerializer


class PesananViewSet(viewsets.ModelViewSet):
    queryset = Pesanan.objects.all()
    serializer_class = PesananSerializer


class ReturBarangViewSet(viewsets.ModelViewSet):
    queryset = ReturBarang.objects.all()
    serializer_class = ReturBarangSerializer

    @action(detail=True, methods=['patch'])
    def ubah_status(self, request, pk=None):
        retur = self.get_object()
        status_baru = request.data.get('status')
        if status_baru not in ['menunggu', 'diproses', 'disetujui', 'ditolak']:
            return Response({'error': 'Status tidak valid'}, status=status.HTTP_400_BAD_REQUEST)
        retur.status = status_baru
        retur.save()
        return Response(ReturBarangSerializer(retur).data)


class PengembalianDanaViewSet(viewsets.ModelViewSet):
    queryset = PengembalianDana.objects.all()
    serializer_class = PengembalianDanaSerializer

    @action(detail=True, methods=['patch'])
    def ubah_status(self, request, pk=None):
        dana = self.get_object()
        status_baru = request.data.get('status')
        if status_baru not in ['menunggu', 'diproses', 'selesai', 'gagal']:
            return Response({'error': 'Status tidak valid'}, status=status.HTTP_400_BAD_REQUEST)
        dana.status = status_baru
        dana.save()
        return Response(PengembalianDanaSerializer(dana).data)