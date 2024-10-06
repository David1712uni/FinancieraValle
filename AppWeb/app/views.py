from django.shortcuts import render, redirect
from .models import AsientoContable
from .forms import AsientoContableForm



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

tipo_cuenta_valor = [
    "AC",
    "AC",
    "AC",
    "AC",
    "AC",
    "AC",
    "AC",
    "AC",
    "AC",
    "AC",
    "AC",
    "AC",
    "AC",
    "AC",
    "AC",
    "AC",
    "AC",
    "AC",
    "ANC",
    "ANC",
    "ANC",
    "ANC",
    "ANC",
    "ANC",
    "ANC",
    "ANC",
    "ANC",
    "ANC",
    "P",
    "P",
    "P",
    "P",
    "PA",
    "P",
    "P",
    "P",
    "P",
    "P",
    "PT",
    "PT",
    "PT",
    "PT",
    "PT",
    "PT",
    "G",
    "G",
    "G",
    "G",
    "G",
    "G",
    "G",
    "G",
    "G",
    "C",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "G",
    "G",
    "G",
    "I",
    "I",
    "I",
    "I",
    "I",
    "I",
    "I",
    "I",
    "I",
    "I",
]

valores_tipo_monto = ["Debe", "Haber"]

def get_tipo_cuenta(cuenta):
    """Retorna el tipo de cuenta basado en la cuenta seleccionada."""
    if cuenta in valores_cuentas:
        idx = valores_cuentas.index(cuenta)
        return tipo_cuenta_valor[idx]
    return 'Desconocido'

def index(request):
    if request.method == 'POST':
        form = AsientoContableForm(request.POST)
        if form.is_valid():
            asiento = form.save(commit=False)
            asiento.tipo_cuenta = get_tipo_cuenta(asiento.cuenta)  # Asignar tipo_cuenta basado en cuenta
            asiento.save()  # Guardar los datos en la base de datos
            return redirect('index')  # Redirigir a la vista de resultados
        else:
            print("Errores en el formulario:", form.errors)
    else:
        form = AsientoContableForm()
        form.fields['cuenta'].choices = [(cuenta, cuenta) for cuenta in valores_cuentas]  # Asegurar opciones

    context = {
        'form': form,
        'valores_cuentas': valores_cuentas,
        'valores_tipo_monto': valores_tipo_monto,
        'errors': form.errors if form.errors else None
    }
    return render(request, 'index.html', context)

from django.utils import timezone

def mostrar_resultados(request):
    # Obtener fechas de inicio y fin desde el formulario
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_final = request.GET.get('fecha_final')

    # Filtrar los asientos contables según las fechas, si están disponibles
    if fecha_inicio and fecha_final:
        # Convertir las fechas de cadena a objeto de fecha
        fecha_inicio = timezone.datetime.strptime(fecha_inicio, '%Y-%m-%d')
        fecha_final = timezone.datetime.strptime(fecha_final, '%Y-%m-%d')
        asientos = AsientoContable.objects.filter(fecha__range=(fecha_inicio, fecha_final))
    else:
        asientos = AsientoContable.objects.all()

    # Calcular el libro diario
    libro_diario = []
    for asiento in asientos:
        debe = asiento.monto if asiento.tipo_monto == 'Debe' else 0
        haber = asiento.monto if asiento.tipo_monto == 'Haber' else 0
        libro_diario.append((asiento.fecha, asiento.cuenta, debe, haber))

    # Calcular los mayores
    mayores = {}
    for asiento in asientos:
        if asiento.cuenta not in mayores:
            mayores[asiento.cuenta] = {'fechas_debe_haber': [], 'total_debe': 0, 'total_haber': 0}

        debe = asiento.monto if asiento.tipo_monto == 'Debe' else 0
        haber = asiento.monto if asiento.tipo_monto == 'Haber' else 0

        # Guardar fecha, debe y haber
        mayores[asiento.cuenta]['fechas_debe_haber'].append((asiento.fecha, debe, haber))
        mayores[asiento.cuenta]['total_debe'] += debe
        mayores[asiento.cuenta]['total_haber'] += haber

    # Transformamos los resultados a una lista para pasarlos al contexto
    resultados_mayores = [
        {'cuenta': cuenta, 'fechas_debe_haber': data['fechas_debe_haber'], 'total_debe': data['total_debe'], 'total_haber': data['total_haber']}
        for cuenta, data in mayores.items()
    ]

    context = {
        'libro_diario': libro_diario,  # Lista de tuples con fecha, cuenta, debe, haber
        'resultados_mayores': resultados_mayores,  # Lista de diccionarios para los mayores
    }
    return render(request, 'resultados.html', context)
