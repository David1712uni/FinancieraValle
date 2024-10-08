from django.db import models

class AsientoContable(models.Model):
    fecha = models.DateField()
    cuenta = models.CharField(max_length=255)
    tipo_cuenta = models.CharField(max_length=10, choices=[('AC', 'Activo Circulante'), ('ANC', 'Activo No Circulante'), ('P', 'Pasivo'), ('PT', 'Patrimonio'), ('C', 'Costos o gastos'), ('I', 'Ingresos'), ('CC', 'Cuentas de Cierre'), ('CEA', 'Cuentas Analíticas de Explotación')])
    tipo_monto = models.CharField(max_length=5, choices=[('Debe', 'Debe'), ('Haber', 'Haber')])
    monto = models.FloatField()
    glose = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.cuenta} ({self.fecha})"


class Saldo_Inicial(models.Model):
    cuenta = models.CharField(max_length=100)
    saldo_inicial = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"{self.cuenta} - Saldo: {self.saldo_inicial}"
