from rest_framework import serializers
from .models import Pembeli, Pesanan, ReturBarang, PengembalianDana


class PembeliSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pembeli
        fields = '__all__'


class PesananSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pesanan
        fields = '__all__'


class ReturBarangSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReturBarang
        fields = '__all__'


class PengembalianDanaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PengembalianDana
        fields = '__all__'