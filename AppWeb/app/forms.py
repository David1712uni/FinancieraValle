valores_cuentas = [
    "10 EFECTIVO Y EQUIVALENTES DE EFECTIVO",
    "11 INVERSIONES FINANCIERAS",
    "12 CUENTAS POR COBRAR COMERCIALES TERCEROS",
    "13 CUENTAS POR COBRAR COMERCIALES RELACIONADAS",
    "14 CUENTAS POR COBRAR AL PERSONAL, A LOS ACCIONISTAS",
    "16 CUENTAS POR COBRAR DIVERSAS TERCEROS",
    "17 CUENTAS POR COBRAR DIVERSAS RELACIONADAS",
    "18 SERVICIOS Y OTROS CONTRATADOS POR ANTICIPADO",
    "20 MERCADERÍAS",
    "21 PRODUCTOS TERMINADOS",
    "22 SUBPRODUCTOS, DESECHOS Y DESPERDICIOS",
    "23 PRODUCTOS EN PROCESO",
    "24 MATERIAS PRIMAS",
    "25 MATERIALES AUXILIARES, SUMINISTROS Y REPUESTO",
    "26 ENVASES Y EMBALAJES",
    "27 ACTIVOS NO CORRIENTES MANTENIDOS PARA LA VENT",
    "28 EXISTENCIAS POR RECIBIR",
    "29 DESVALORIZACIÓN DE EXISTENCIAS",
    "30 INVERSIONES MOBILIARIAS",
    "31 INVERSIONES INMOBILIARIAS",
    "32 ACTIVOS ADQUIRIDOS EN ARRENDAMIENTO FINANCIERO",
    "33 INMUEBLES, MAQUINARIA Y EQUIPO",
    "34 INTANGIBLES",
    "35 ACTIVOS BIOLÓGICOS",
    "36 DESVALORIZACIÓN DE ACTIVO INMOVILIZADO",
    "37 ACTIVO DIFERIDO",
    "38 OTROS ACTIVOS",
    "39 DEPRECIACIÓN, AMORTIZACIÓN Y AGOTAMIENTO ACUMULADOS",
    "40 TRIBUTOS Y APORTES AL SISTEMA DE PENSIONES Y DE SALUD POR PAGAR",
    "41 REMUNERACIONES Y PARTICIPACIONES POR PAGAR",
    "42 CUENTAS POR PAGAR COMERCIALES TERCEROS",
    "43 CUENTAS POR PAGAR COMERCIALES RELACIONADAS",
    "44 CUENTAS POR PAGAR A LOS ACCIONISTAS, DIRECTORES Y GERENTES",
    "45 OBLIGACIONES FINANCIERAS",
    "46 CUENTAS POR PAGAR DIVERSAS TERCEROS",
    "47 CUENTAS POR PAGAR DIVERSAS RELACIONADAS",
    "48 PROVISIONES",
    "49 PASIVO DIFERIDO",
    "50 CAPITAL",
    "51 ACCIONES DE INVERSIÓN",
    "52 CAPITAL ADICIONAL",
    "56 RESULTADOS NO REALIZADOS",
    "57 EXCEDENTE DE REVALUACIÓN",
    "58 RESERVAS",
    "60 COMPRAS",
    "61 VARIACIÓN DE EXISTENCIAS",
    "62 GASTOS DE PERSONAL, DIRECTORES Y GERENTES",
    "63 GASTOS DE SERVICIOS PRESTADOS POR TERCEROS",
    "64 GASTOS POR TRIBUTOS",
    "65 OTROS GASTOS DE GESTIÓN",
    "66 PÉRDIDA POR MEDICIÓN DE ACTIVOS NO FINANCIEROS AL VALOR RAZONABLE",
    "67 GASTOS FINANCIEROS",
    "68 VALUACIÓN Y DETERIORO DE ACTIVOS Y PROVISIONES",
    "69 COSTO DE VENTAS",
    "81 PRODUCCIÓN DEL EJERCICIO",
    "82 VALOR AGREGADO",
    "83 EXCEDENTE BRUTO (INSUFICIENCIA BRUTA) DE EXPLOTACIÓN",
    "84 RESULTADO DE EXPLOTACIÓN",
    "85 RESULTADO ANTES DE PARTICIPACIONES E IMPUESTOS",
    "87 PARTICIPACIONES DE LOS TRABAJADORES",
    "88 IMPUESTO A LA RENTA",
    "89 DETERMINACIÓN DEL RESULTADO DEL EJERCICIO",
    "91 COSTOS POR DISTRIBUIR.",
    "92 COSTOS DE PRODUCCIÓN",
    "93 CENTROS DE COSTOS",
    "94 GASTOS ADMINISTRATIVOS.",
    "95 GASTOS DE VENTAS",
    "96 GASTOS FINANCIEROS",
    "70 VENTAS",
    "71 VARIACIÓN DE LA PRODUCCIÓN ALMACENADA",
    "72 PRODUCCIÓN DE ACTIVO INMOVILIZADO",
    "73 DESCUENTOS, REBAJAS Y BONIFICACIONES OBTENIDOS",
    "74 DESCUENTOS, REBAJAS Y BONIFICACIONES CONCEDIDOS",
    "75 OTROS INGRESOS DE GESTIÓN",
    "76 GANANCIA POR MEDICIÓN DE ACTIVOS NO FINANCIEROS AL VALOR RAZONABLE",
    "77 INGRESOS FINANCIEROS",
    "78 CARGAS CUBIERTAS POR PROVISIONES",
    "79 CARGAS IMPUTABLES A CUENTAS DE COSTOS Y GASTOS",
]
from django import forms
from .models import AsientoContable



class AsientoContableForm(forms.ModelForm):
    class Meta:
        model = AsientoContable
        fields = ['fecha', 'cuenta', 'tipo_cuenta', 'tipo_monto', 'monto']
        
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'cuenta': forms.Select(choices=[
                ('AC', '10 EFECTIVO Y EQUIVALENTES DE EFECTIVO'),
    ('AC', '11 INVERSIONES FINANCIERAS'),
    ('AC', '12 CUENTAS POR COBRAR COMERCIALES TERCEROS'),
    ('AC', '13 CUENTAS POR COBRAR COMERCIALES RELACIONADAS'),
    ('AC', '14 CUENTAS POR COBRAR AL PERSONAL, A LOS ACCIONISTAS'),
    ('AC', '16 CUENTAS POR COBRAR DIVERSAS TERCEROS'),
    ('AC', '17 CUENTAS POR COBRAR DIVERSAS RELACIONADAS'),
    ('AC', '18 SERVICIOS Y OTROS CONTRATADOS POR ANTICIPADO'),
    ('AC', '20 MERCADERÍAS'),
    ('AC', '21 PRODUCTOS TERMINADOS'),
    ('AC', '22 SUBPRODUCTOS, DESECHOS Y DESPERDICIOS'),
    ('AC', '23 PRODUCTOS EN PROCESO'),
    ('AC', '24 MATERIAS PRIMAS'),
    ('AC', '25 MATERIALES AUXILIARES, SUMINISTROS Y REPUESTO'),
    ('AC', '26 ENVASES Y EMBALAJES'),
    ('AC', '27 ACTIVOS NO CORRIENTES MANTENIDOS PARA LA VENT'),
    ('AC', '28 EXISTENCIAS POR RECIBIR'),
    ('AC', '29 DESVALORIZACIÓN DE EXISTENCIAS'),
    ('ANC', '30 INVERSIONES MOBILIARIAS'),
    ('ANC', '31 INVERSIONES INMOBILIARIAS'),
    ('ANC', '32 ACTIVOS ADQUIRIDOS EN ARRENDAMIENTO FINANCIERO'),
    ('ANC', '33 INMUEBLES, MAQUINARIA Y EQUIPO'),
    ('ANC', '34 INTANGIBLES'),
    ('ANC', '35 ACTIVOS BIOLÓGICOS'),
    ('ANC', '36 DESVALORIZACIÓN DE ACTIVO INMOVILIZADO'),
    ('ANC', '37 ACTIVO DIFERIDO'),
    ('ANC', '38 OTROS ACTIVOS'),
    ('ANC', '39 DEPRECIACIÓN, AMORTIZACIÓN Y AGOTAMIENTO ACUMULADOS'),
    ('P', '40 TRIBUTOS Y APORTES AL SISTEMA DE PENSIONES Y DE SALUD POR PAGAR'),
    ('P', '41 REMUNERACIONES Y PARTICIPACIONES POR PAGAR'),
    ('P', '42 CUENTAS POR PAGAR COMERCIALES TERCEROS'),
    ('P', '43 CUENTAS POR PAGAR COMERCIALES RELACIONADAS'),
    ('P', '44 CUENTAS POR PAGAR A LOS ACCIONISTAS, DIRECTORES Y GERENTES'),
    ('P', '45 OBLIGACIONES FINANCIERAS'),
    ('P', '46 CUENTAS POR PAGAR DIVERSAS TERCEROS'),
    ('P', '47 CUENTAS POR PAGAR DIVERSAS RELACIONADAS'),
    ('P', '48 PROVISIONES'),
    ('P', '49 PASIVO DIFERIDO'),
    ('PT', '50 CAPITAL'),
    ('PT', '51 ACCIONES DE INVERSIÓN'),
    ('PT', '52 CAPITAL ADICIONAL'),
    ('PT', '56 RESULTADOS NO REALIZADOS'),
    ('PT', '57 EXCEDENTE DE REVALUACIÓN'),
    ('PT', '58 RESERVAS'),
    ('G', '60 COMPRAS'),
    ('G', '61 VARIACIÓN DE EXISTENCIAS'),
    ('G', '62 GASTOS DE PERSONAL, DIRECTORES Y GERENTES'),
    ('G', '63 GASTOS DE SERVICIOS PRESTADOS POR TERCEROS'),
    ('G', '64 GASTOS POR TRIBUTOS'),
    ('G', '65 OTROS GASTOS DE GESTIÓN'),
    ('G', '66 PÉRDIDA POR MEDICIÓN DE ACTIVOS NO FINANCIEROS AL VALOR RAZONABLE'),
    ('G', '67 GASTOS FINANCIEROS'),
    ('G', '68 VALUACIÓN Y DETERIORO DE ACTIVOS Y PROVISIONES'),
    ('G', '69 COSTO DE VENTAS'),
    ('CC', '81 PRODUCCIÓN DEL EJERCICIO'),
    ('CC', '82 VALOR AGREGADO'),
    ('CC', '83 EXCEDENTE BRUTO (INSUFICIENCIA BRUTA) DE EXPLOTACIÓN'),
    ('CC', '84 RESULTADO DE EXPLOTACIÓN'),
    ('CC', '85 RESULTADO ANTES DE PARTICIPACIONES E IMPUESTOS'),
    ('CC', '87 PARTICIPACIONES DE LOS TRABAJADORES'),
    ('CC', '88 IMPUESTO A LA RENTA'),
    ('CC', '89 DETERMINACIÓN DEL RESULTADO DEL EJERCICIO'),
    ('CEA', '91 COSTOS POR DISTRIBUIR.'),
    ('CEA', '92 COSTOS DE PRODUCCIÓN'),
    ('CEA', '93 CENTROS DE COSTOS'),
    ('CEA', '94 GASTOS ADMINISTRATIVOS.'),
    ('CEA', '95 GASTOS DE VENTAS'),
    ('CEA', '96 GASTOS FINANCIEROS'),
    ('I', '70 VENTAS'),
    ('I', '71 VARIACIÓN DE LA PRODUCCIÓN ALMACENADA'),
    ('I', '72 PRODUCCIÓN DE ACTIVO INMOVILIZADO'),
    ('I', '73 DESCUENTOS, REBAJAS Y BONIFICACIONES OBTENIDOS'),
    ('I', '74 DESCUENTOS, REBAJAS Y BONIFICACIONES CONCEDIDOS'),
    ('I', '75 OTROS INGRESOS DE GESTIÓN'),
    ('I', '76 GANANCIA POR MEDICIÓN DE ACTIVOS NO FINANCIEROS AL VALOR RAZONABLE'),
    ('I', '77 INGRESOS FINANCIEROS'),
    ('I', '78 CARGAS CUBIERTAS POR PROVISIONES'),
    ('I', '79 CARGAS IMPUTABLES A CUENTAS DE COSTOS Y GASTOS'),]),  # Retirar choices por defecto
            'tipo_cuenta': forms.Select(choices=[
                ('AC', 'Activo Circulante'), 
                ('ANC', 'Activo No Circulante'), 
                ('P', 'Pasivo'), 
                ('PT', 'Patrimonio'), 
                ('G', 'Gastos'), 
                ('C', 'Costo'),
                ('I', 'Ingresos'),
                ('CC', 'Cuentas de Cierre'),
                ('CEA', 'Cuentas Analíticas de Explotación')]),
            'tipo_monto': forms.Select(choices=[('Debe', 'Debe'), ('Haber', 'Haber')]),
            'monto': forms.NumberInput(attrs={'placeholder': 'Monto'}),
        }
