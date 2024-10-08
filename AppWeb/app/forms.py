from django import forms
from .models import AsientoContable
from .models import Saldo_Inicial

class AsientoContableForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AsientoContableForm, self).__init__(*args, **kwargs)
        self.add_custom_styles()

    def add_custom_styles(self):
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['style'] = ' border-radius: 10px; display:flex; margin-bottom: 10px; background-color: #f5f5f5; border: 1px solid #ccc; padding: 5px;'
            
            if isinstance(field.widget, forms.TextInput):
                field.widget.attrs['style'] += 'max-width: 200px;'
            if isinstance(field.widget, forms.Textarea):
                field.widget.attrs['style'] += 'height: 100px; width: 100%;'
            if isinstance(field.widget, forms.SelectMultiple):
                field.widget.attrs['style'] += ''
            if isinstance(field.widget, forms.DateInput):
                field.widget.attrs['style'] += ''
    glose = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Ingrese la descripci (opcional)'}), required=False)

    class Meta:
        model = AsientoContable
        fields = ['fecha', 'cuenta', 'tipo_cuenta', 'tipo_monto', 'monto', 'glose']
        
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'cuenta': forms.Select(choices=[
                ('10', '10 EFECTIVO Y EQUIVALENTES DE EFECTIVO'),
                ('11', '11 INVERSIONES FINANCIERAS'),
                ('12', '12 CUENTAS POR COBRAR COMERCIALES TERCEROS'),
                ('13', '13 CUENTAS POR COBRAR COMERCIALES RELACIONADAS'),
                ('14', '14 CUENTAS POR COBRAR AL PERSONAL, A LOS ACCIONISTAS'),
                ('16', '16 CUENTAS POR COBRAR DIVERSAS TERCEROS'),
                ('17', '17 CUENTAS POR COBRAR DIVERSAS RELACIONADAS'),
                ('18', '18 SERVICIOS Y OTROS CONTRATADOS POR ANTICIPADO'),
                ('20', '20 MERCADERÍAS'),
                ('21', '21 PRODUCTOS TERMINADOS'),
                ('22', '22 SUBPRODUCTOS, DESECHOS Y DESPERDICIOS'),
                ('23', '23 PRODUCTOS EN PROCESO'),
                ('24', '24 MATERIAS PRIMAS'),
                ('25', '25 MATERIALES AUXILIARES, SUMINISTROS Y REPUESTO'),
                ('26', '26 ENVASES Y EMBALAJES'),
                ('27', '27 ACTIVOS NO CORRIENTES MANTENIDOS PARA LA VENT'),
                ('28', '28 EXISTENCIAS POR RECIBIR'),
                ('29', '29 DESVALORIZACIÓN DE EXISTENCIAS'),
                ('30', '30 INVERSIONES MOBILIARIAS'),
                ('31', '31 INVERSIONES INMOBILIARIAS'),
                ('32', '32 ACTIVOS ADQUIRIDOS EN ARRENDAMIENTO FINANCIERO'),
                ('33', '33 INMUEBLES, MAQUINARIA Y EQUIPO'),
                ('34', '34 INTANGIBLES'),
                ('35', '35 ACTIVOS BIOLÓGICOS'),
                ('36', '36 DESVALORIZACIÓN DE ACTIVO INMOVILIZADO'),
                ('37', '37 ACTIVO DIFERIDO'),
                ('38', '38 OTROS ACTIVOS'),
                ('39', '39 DEPRECIACIÓN, AMORTIZACIÓN Y AGOTAMIENTO ACUMULADOS'),
                ('40', '40 TRIBUTOS Y APORTES AL SISTEMA DE PENSIONES Y DE SALUD POR PAGAR'),
                ('41', '41 REMUNERACIONES Y PARTICIPACIONES POR PAGAR'),
                ('42', '42 CUENTAS POR PAGAR COMERCIALES TERCEROS'),
                ('43', '43 CUENTAS POR PAGAR COMERCIALES RELACIONADAS'),
                ('44', '44 CUENTAS POR PAGAR A LOS ACCIONISTAS, DIRECTORES Y GERENTES'),
                ('45', '45 OBLIGACIONES FINANCIERAS'),
                ('46', '46 CUENTAS POR PAGAR DIVERSAS TERCEROS'),
                ('47', '47 CUENTAS POR PAGAR DIVERSAS RELACIONADAS'),
                ('48', '48 PROVISIONES'),
                ('49', '49 PASIVO DIFERIDO'),
                ('50', '50 CAPITAL'),
                ('51', '51 ACCIONES DE INVERSIÓN'),
                ('52', '52 CAPITAL ADICIONAL'),
                ('56', '56 RESULTADOS NO REALIZADOS'),
                ('57', '57 EXCEDENTE DE REVALUACIÓN'),
                ('58', '58 RESERVAS'),
                ('60', '60 COMPRAS'),
                ('61', '61 VARIACIÓN DE EXISTENCIAS'),
                ('62', '62 GASTOS DE PERSONAL, DIRECTORES Y GERENTES'),
                ('63', '63 GASTOS DE SERVICIOS PRESTADOS POR TERCEROS'),
                ('64', '64 GASTOS POR TRIBUTOS'),
                ('65', '65 OTROS GASTOS DE GESTIÓN'),
                ('66', '66 PÉRDIDA POR MEDICIÓN DE ACTIVOS NO FINANCIEROS AL VALOR RAZONABLE'),
                ('67', '67 GASTOS FINANCIEROS'),
                ('68', '68 VALUACIÓN Y DETERIORO DE ACTIVOS Y PROVISIONES'),
                ('69', '69 COSTO DE VENTAS'),
                ('81', '81 PRODUCCIÓN DEL EJERCICIO'),
                ('82', '82 VALOR AGREGADO'),
                ('83', '83 EXCEDENTE BRUTO (INSUFICIENCIA BRUTA) DE EXPLOTACIÓN'),
                ('84', '84 RESULTADO DE EXPLOTACIÓN'),
                ('85', '85 RESULTADO ANTES DE PARTICIPACIONES E IMPUESTOS'),
                ('87', '87 PARTICIPACIONES DE LOS TRABAJADORES'),
                ('88', '88 IMPUESTO A LA RENTA'),
                ('89', '89 DETERMINACIÓN DEL RESULTADO DEL EJERCICIO'),
                ('91', '91 COSTOS POR DISTRIBUIR.'),
                ('92', '92 COSTOS DE PRODUCCIÓN'),
                ('93', '93 CENTROS DE COSTOS'),
                ('94', '94 GASTOS ADMINISTRATIVOS.'),
                ('95', '95 GASTOS DE VENTAS'),
                ('96', '96 GASTOS FINANCIEROS'),
                ('70', '70 VENTAS'),
                ('71', '71 VARIACIÓN DE LA PRODUCCIÓN ALMACENADA'),
                ('72', '72 PRODUCCIÓN DE ACTIVO INMOVILIZADO'),
                ('73', '73 DESCUENTOS, REBAJAS Y BONIFICACIONES OBTENIDOS'),
                ('74', '74 DESCUENTOS, REBAJAS Y BONIFICACIONES CONCEDIDOS'),
                ('75', '75 OTROS INGRESOS DE GESTIÓN'),
                ('76', '76 GANANCIA POR MEDICIÓN DE ACTIVOS NO FINANCIEROS AL VALOR RAZONABLE'),
                ('77', '77 INGRESOS FINANCIEROS'),
                ('78', '78 CARGAS CUBIERTAS POR PROVISIONES'),
                ('79', '79 CARGAS IMPUTABLES A CUENTAS DE COSTOS Y GASTOS'),
            ]),
            'tipo_cuenta': forms.Select(choices=[
                ('AC', 'Activo Circulante'), 
                ('ANC', 'Activo No Circulante'), 
                ('P', 'Pasivo'), 
                ('PT', 'Patrimonio'), 
                ('C', 'Costoso gastos'),
                ('I', 'Ingresos'),
                ('CC', 'Cuentas de Cierre'),
                ('CEA', 'Cuentas Analíticas de Explotación')
            ]),
            'tipo_monto': forms.Select(choices=[('Debe', 'Debe'), ('Haber', 'Haber')]),
            'monto': forms.NumberInput(attrs={'placeholder': 'Monto'}),
        }


class SaldoInicialForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SaldoInicialForm, self).__init__(*args, **kwargs)
        self.add_custom_styles()

    def add_custom_styles(self):
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['style'] = ' border-radius: 10px; display:flex; margin-bottom: 10px; background-color: #f5f5f5; border: 1px solid #ccc; padding: 5px;'
            
            if isinstance(field.widget, forms.TextInput):
                field.widget.attrs['style'] += 'max-width: 200px;'
            if isinstance(field.widget, forms.SelectMultiple):
                field.widget.attrs['style'] += ''
    class Meta:
        model = Saldo_Inicial
        fields = ['cuenta', 'saldo_inicial']
        widgets = {
            'cuenta': forms.Select(choices=[
                ('10', '10 EFECTIVO Y EQUIVALENTES DE EFECTIVO'),
                ('11', '11 INVERSIONES FINANCIERAS'),
                ('12', '12 CUENTAS POR COBRAR COMERCIALES TERCEROS'),
                ('13', '13 CUENTAS POR COBRAR COMERCIALES RELACIONADAS'),
                ('14', '14 CUENTAS POR COBRAR AL PERSONAL, A LOS ACCIONISTAS'),
                ('16', '16 CUENTAS POR COBRAR DIVERSAS TERCEROS'),
                ('17', '17 CUENTAS POR COBRAR DIVERSAS RELACIONADAS'),
                ('18', '18 SERVICIOS Y OTROS CONTRATADOS POR ANTICIPADO'),
                ('20', '20 MERCADERÍAS'),
                ('21', '21 PRODUCTOS TERMINADOS'),
                ('22', '22 SUBPRODUCTOS, DESECHOS Y DESPERDICIOS'),
                ('23', '23 PRODUCTOS EN PROCESO'),
                ('24', '24 MATERIAS PRIMAS'),
                ('25', '25 MATERIALES AUXILIARES, SUMINISTROS Y REPUESTO'),
                ('26', '26 ENVASES Y EMBALAJES'),
                ('27', '27 ACTIVOS NO CORRIENTES MANTENIDOS PARA LA VENT'),
                ('28', '28 EXISTENCIAS POR RECIBIR'),
                ('29', '29 DESVALORIZACIÓN DE EXISTENCIAS'),
                ('30', '30 INVERSIONES MOBILIARIAS'),
                ('31', '31 INVERSIONES INMOBILIARIAS'),
                ('32', '32 ACTIVOS ADQUIRIDOS EN ARRENDAMIENTO FINANCIERO'),
                ('33', '33 INMUEBLES, MAQUINARIA Y EQUIPO'),
                ('34', '34 INTANGIBLES'),
                ('35', '35 ACTIVOS BIOLÓGICOS'),
                ('36', '36 DESVALORIZACIÓN DE ACTIVO INMOVILIZADO'),
                ('37', '37 ACTIVO DIFERIDO'),
                ('38', '38 OTROS ACTIVOS'),
                ('39', '39 DEPRECIACIÓN, AMORTIZACIÓN Y AGOTAMIENTO ACUMULADOS'),
                ('40', '40 TRIBUTOS Y APORTES AL SISTEMA DE PENSIONES Y DE SALUD POR PAGAR'),
                ('41', '41 REMUNERACIONES Y PARTICIPACIONES POR PAGAR'),
                ('42', '42 CUENTAS POR PAGAR COMERCIALES TERCEROS'),
                ('43', '43 CUENTAS POR PAGAR COMERCIALES RELACIONADAS'),
                ('44', '44 CUENTAS POR PAGAR A LOS ACCIONISTAS, DIRECTORES Y GERENTES'),
                ('45', '45 OBLIGACIONES FINANCIERAS'),
                ('46', '46 CUENTAS POR PAGAR DIVERSAS TERCEROS'),
                ('47', '47 CUENTAS POR PAGAR DIVERSAS RELACIONADAS'),
                ('48', '48 PROVISIONES'),
                ('49', '49 PASIVO DIFERIDO'),
                ('50', '50 CAPITAL'),
                ('51', '51 ACCIONES DE INVERSIÓN'),
                ('52', '52 CAPITAL ADICIONAL'),
                ('56', '56 RESULTADOS NO REALIZADOS'),
                ('57', '57 EXCEDENTE DE REVALUACIÓN'),
                ('58', '58 RESERVAS'),
                ('60', '60 COMPRAS'),
                ('61', '61 VARIACIÓN DE EXISTENCIAS'),
                ('62', '62 GASTOS DE PERSONAL, DIRECTORES Y GERENTES'),
                ('63', '63 GASTOS DE SERVICIOS PRESTADOS POR TERCEROS'),
                ('64', '64 GASTOS POR TRIBUTOS'),
                ('65', '65 OTROS GASTOS DE GESTIÓN'),
                ('66', '66 PÉRDIDA POR MEDICIÓN DE ACTIVOS NO FINANCIEROS AL VALOR RAZONABLE'),
                ('67', '67 GASTOS FINANCIEROS'),
                ('68', '68 VALUACIÓN Y DETERIORO DE ACTIVOS Y PROVISIONES'),
                ('69', '69 COSTO DE VENTAS'),
                ('81', '81 PRODUCCIÓN DEL EJERCICIO'),
                ('82', '82 VALOR AGREGADO'),
                ('83', '83 EXCEDENTE BRUTO (INSUFICIENCIA BRUTA) DE EXPLOTACIÓN'),
                ('84', '84 RESULTADO DE EXPLOTACIÓN'),
                ('85', '85 RESULTADO ANTES DE PARTICIPACIONES E IMPUESTOS'),
                ('87', '87 PARTICIPACIONES DE LOS TRABAJADORES'),
                ('88', '88 IMPUESTO A LA RENTA'),
                ('89', '89 DETERMINACIÓN DEL RESULTADO DEL EJERCICIO'),
                ('91', '91 COSTOS POR DISTRIBUIR.'),
                ('92', '92 COSTOS DE PRODUCCIÓN'),
                ('93', '93 CENTROS DE COSTOS'),
                ('94', '94 GASTOS ADMINISTRATIVOS.'),
                ('95', '95 GASTOS DE VENTAS'),
                ('96', '96 GASTOS FINANCIEROS'),
                ('70', '70 VENTAS'),
                ('71', '71 VARIACIÓN DE LA PRODUCCIÓN ALMACENADA'),
                ('72', '72 PRODUCCIÓN DE ACTIVO INMOVILIZADO'),
                ('73', '73 DESCUENTOS, REBAJAS Y BONIFICACIONES OBTENIDOS'),
                ('74', '74 DESCUENTOS, REBAJAS Y BONIFICACIONES CONCEDIDOS'),
                ('75', '75 OTROS INGRESOS DE GESTIÓN'),
                ('76', '76 GANANCIA POR MEDICIÓN DE ACTIVOS NO FINANCIEROS AL VALOR RAZONABLE'),
                ('77', '77 INGRESOS FINANCIEROS'),
                ('78', '78 CARGAS CUBIERTAS POR PROVISIONES'),
                ('79', '79 CARGAS IMPUTABLES A CUENTAS DE COSTOS Y GASTOS'),
            ]),
            'saldo_inicial': forms.NumberInput(attrs={'placeholder': 'Saldo Inicial'}),
        }
