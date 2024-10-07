from django.shortcuts import render, redirect
from .models import AsientoContable
from .forms import AsientoContableForm



valores_cuentas = [
    "10",
"11",
"12",
"13",
"14",
"16",
"17",
"18",
"20",
"21",
"22",
"23",
"24",
"25",
"26",
"27",
"28",
"29",
"30",
"31",
"32",
"33",
"34",
"35",
"36",
"37",
"38",
"39",
"40",
"41",
"42",
"43",
"44",
"45",
"46",
"47",
"48",
"49",
"50",
"51",
"52",
"56",
"57",
"58",
"60",
"61",
"62",
"63",
"64",
"65",
"66",
"67",
"68",
"69",
"81",
"82",
"83",
"84",
"85",
"87",
"88",
"89",
"91",
"92",
"93",
"94",
"95",
"96",
"70",
"71",
"72",
"73",
"74",
"75",
"76",
"77",
"78",
"79",
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
    "P",
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
    "PT",
    "C",
    "C",
    "C",
    "C",
    "C",
    "C",
    "C",
    "C",
    "C",
    "C",
    "CC",
    "CC",
    "CC",
    "CC",
    "CC",
    "CC",
    "CC",
    "CC",
    "CC",
    "CEA",
    "CEA",
    "CEA",
    "CEA",
    "CEA",
    "CEA",
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
            asiento.tipo_cuenta = asiento.cuenta  # Asignar tipo_cuenta basado en cuenta
            asiento.cuenta = get_tipo_cuenta(asiento.cuenta)
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

        libro_diario.append((asiento.fecha, asiento.cuenta, asiento.tipo_cuenta, debe, haber))

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

    # Calcular el Estado de Resultados
    estado_resultados = {
        'ventas': 0,
        'costo_ventas': 0,
        'gastos_administrativos': 0,
        'gastos_ventas': 0,
        'otros_ingresos': 0,
        'otros_gastos': 0,
        'gastos_financieros': 0,
        'impuesto_renta': 0,
    }

    # Sumar las cuentas relevantes
    for asiento in asientos:
        print(f"Cuenta: {asiento.tipo_cuenta}, Monto: {asiento.monto}")  # Para depurar
        if asiento.tipo_cuenta == '70':
            estado_resultados['ventas'] += asiento.monto
        elif asiento.tipo_cuenta == '69':
            estado_resultados['costo_ventas'] += asiento.monto
        elif asiento.tipo_cuenta == '94':
            estado_resultados['gastos_administrativos'] += asiento.monto
        elif asiento.tipo_cuenta == '95':
            estado_resultados['gastos_ventas'] += asiento.monto
        elif asiento.tipo_cuenta == '75':
            estado_resultados['otros_ingresos'] += asiento.monto
        elif asiento.tipo_cuenta == '65':
            estado_resultados['otros_gastos'] += asiento.monto
        elif asiento.tipo_cuenta == '67':
            estado_resultados['gastos_financieros'] += asiento.monto
        elif asiento.tipo_cuenta == '88':
            estado_resultados['impuesto_renta'] += asiento.monto

    # Calcular utilidades
    utilidad_bruta = estado_resultados['ventas'] - estado_resultados['costo_ventas']
    utilidad_operacion = utilidad_bruta - estado_resultados['gastos_administrativos'] - estado_resultados['gastos_ventas']
    utilidad_antes_impuestos = utilidad_operacion + estado_resultados['otros_ingresos'] - estado_resultados['otros_gastos'] - estado_resultados['gastos_financieros']
    utilidad_neta = utilidad_antes_impuestos - estado_resultados['impuesto_renta']


    #Estado Financiero
    activos_corrientes = {}
    pasivos_corrientes = {}
    activos_no_corrientes = {}
    pasivos_no_corrientes = {}
    patrimonio = {}

    valores_cuentas = {
        '10': 0,
        '11': 0,
        '12': 0,
        '13': 0,
        '14': 0,
        '16': 0,
        '17': 0,
        '18': 0,
        '20': 0,
        '21': 0,
        '22': 0,
        '23': 0,
        '24': 0,
        '25': 0,
        '26': 0,
        '27': 0,
        '28': 0,
        '29': 0,
        '30': 0,
        '31': 0,
        '32': 0,
        '33': 0,
        '34': 0,
        '35': 0,
        '36': 0,
        '37': 0,
        '38': 0,
        '39': 0,
        '40': 0,
        '41': 0,
        '42': 0,
        '43': 0,
        '44': 0,
        '45': 0,
        '46': 0,
        '47': 0,
        '48': 0,
        '49': 0,
        '50': 0,
        '51': 0,
        '52': 0,
        '56': 0,
        '57': 0,
        '58': 0,
    }

    for asiento in asientos:
        cuenta = asiento.cuenta
        tipo_cuenta = asiento.tipo_cuenta
        monto = asiento.monto if asiento.tipo_monto == 'Debe' else -asiento.monto
        if tipo_cuenta== 'Desconocido':
            continue

        if cuenta== 'AC':
            if tipo_cuenta not in activos_corrientes:
                activos_corrientes[tipo_cuenta] = 0
            activos_corrientes[tipo_cuenta] += monto
            valores_cuentas[tipo_cuenta] += monto
        elif cuenta== 'ANC':
            if tipo_cuenta not in activos_no_corrientes:
                activos_no_corrientes[tipo_cuenta] = 0
            activos_no_corrientes[tipo_cuenta] += monto
            valores_cuentas[tipo_cuenta] += monto
        elif cuenta== 'P' and  ( tipo_cuenta in ["40", "41", "42", "43", "44", "46", "47", "48"]):
            if tipo_cuenta not in pasivos_corrientes:
                pasivos_corrientes[tipo_cuenta] = 0
            pasivos_corrientes[tipo_cuenta] += monto
            valores_cuentas[tipo_cuenta] += monto
        elif cuenta== 'P' and  ( tipo_cuenta in ["45","49"] ):
            if tipo_cuenta not in pasivos_no_corrientes:
                pasivos_no_corrientes[tipo_cuenta] = 0
            pasivos_no_corrientes[tipo_cuenta] += monto
            valores_cuentas[tipo_cuenta] += monto
        elif cuenta == 'PT':
            if tipo_cuenta not in patrimonio:
                patrimonio[tipo_cuenta] = 0
            patrimonio[tipo_cuenta] += monto
            valores_cuentas[tipo_cuenta] += monto

    total_activo_corriente = sum(activos_corrientes.values())
    total_pasivo_corriente = sum(pasivos_corrientes.values())
    total_activo_no_corriente = sum(activos_no_corrientes.values())
    total_pasivo_no_corriente = sum(pasivos_no_corrientes.values())
    total_patrimonio = sum(patrimonio.values())


    total_activo = total_activo_corriente + total_activo_no_corriente
    total_pasivo = total_pasivo_corriente + total_pasivo_no_corriente
    total_pasivo = total_patrimonio
    total_pasivo_patrimonio=  total_pasivo + total_pasivo


    

    context = {
        'libro_diario': libro_diario,
        'resultados_mayores': resultados_mayores,
        'estado_resultados': {
            'ventas': estado_resultados['ventas'],
            'costo_ventas': estado_resultados['costo_ventas'],
            'utilidad_bruta': utilidad_bruta,
            'gastos_administrativos': estado_resultados['gastos_administrativos'],
            'gastos_ventas': estado_resultados['gastos_ventas'],
            'utilidad_operacion': utilidad_operacion,
            'otros_ingresos': estado_resultados['otros_ingresos'],
            'gastos_financieros': estado_resultados['gastos_financieros'],
            'utilidad_antes_impuestos': utilidad_antes_impuestos,
            'impuesto_renta': estado_resultados['impuesto_renta'],
            'utilidad_neta': utilidad_neta,
        },
        'estado_situacion_financiera': {
        'activos_corrientes': activos_corrientes,
        'pasivos_corrientes': pasivos_corrientes,
        'activos_no_corrientes': activos_no_corrientes,
        'patrimonio': patrimonio,
        'total_activo_corriente': total_activo_corriente,
        'total_activo_no_corriente': total_activo_no_corriente,
        'total_pasivo_corriente': total_pasivo_corriente,
        'total_pasivo_no_corriente': total_pasivo_no_corriente,
        'total_activo': total_activo,
        'total_pasivo': total_pasivo,
        'total_patrimonio': total_patrimonio,
        'total_pasivo_patrimonio': total_pasivo_patrimonio,
        'valores_cuentas' : valores_cuentas
        },
    }

    return render(request, 'resultados.html', context)

    
