from django.db import models

class AsientoContable(models.Model):
    fecha = models.DateField()
    cuenta = models.CharField(max_length=255)
    tipo_cuenta = models.CharField(max_length=10, choices=[('AC', 'Activo Circulante'), ('ANC', 'Activo No Circulante'), ('P', 'Pasivo'), ('PT', 'Patrimonio'), ('C', 'Costos o gastos'), ('I', 'Ingresos'), ('CC', 'Cuentas de Cierre'), ('CEA', 'Cuentas Analíticas de Explotación')])
    tipo_monto = models.CharField(max_length=5, choices=[('Debe', 'Debe'), ('Haber', 'Haber')])
    monto = models.FloatField()
    
    def __str__(self):
        return f"{self.cuenta} ({self.fecha})"
