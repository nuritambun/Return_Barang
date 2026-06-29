from django.db import models

class Pembeli(models.Model):
    nama = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    no_hp = models.CharField(max_length=15)

    def __str__(self):
        return self.nama


class Pesanan(models.Model):
    pembeli = models.ForeignKey(Pembeli, on_delete=models.CASCADE)
    no_pesanan = models.CharField(max_length=50, unique=True)
    nama_produk = models.CharField(max_length=200)
    jumlah = models.PositiveIntegerField()
    harga_total = models.DecimalField(max_digits=12, decimal_places=2)
    tanggal_pesanan = models.DateField()

    def __str__(self):
        return self.no_pesanan


class ReturBarang(models.Model):
    STATUS_CHOICES = [
        ('menunggu', 'Menunggu'),
        ('diproses', 'Diproses'),
        ('disetujui', 'Disetujui'),
        ('ditolak', 'Ditolak'),
    ]
    pesanan = models.ForeignKey(Pesanan, on_delete=models.CASCADE)
    alasan_retur = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='menunggu')
    tanggal_retur = models.DateField(auto_now_add=True)
    foto_bukti = models.ImageField(upload_to='bukti_retur/', blank=True, null=True)

    def __str__(self):
        return f"Retur - {self.pesanan.no_pesanan}"


class PengembalianDana(models.Model):
    METODE_CHOICES = [
        ('transfer_bank', 'Transfer Bank'),
        ('dompet_digital', 'Dompet Digital'),
        ('saldo_shopee', 'Saldo Shopee'),
    ]
    STATUS_CHOICES = [
        ('menunggu', 'Menunggu'),
        ('diproses', 'Diproses'),
        ('selesai', 'Selesai'),
        ('gagal', 'Gagal'),
    ]
    retur = models.OneToOneField(ReturBarang, on_delete=models.CASCADE)
    jumlah_dana = models.DecimalField(max_digits=12, decimal_places=2)
    metode_pengembalian = models.CharField(max_length=30, choices=METODE_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='menunggu')
    tanggal_proses = models.DateField(auto_now_add=True)
    no_rekening = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"Dana - {self.retur.pesanan.no_pesanan}"