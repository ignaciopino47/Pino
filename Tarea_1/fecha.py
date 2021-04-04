#%%
def es_bisiesto(anno: int) -> bool:
    return anno % 4 == 0 and (anno % 100 != 0 or anno % 400 == 0)

def diasMes(mes: int, anno: int) -> int:
    # Abril, junio, septiembre y noviembre tienen 30
    if mes in [4, 6, 9, 11]:
        return 30
    # Febrero depende de si es o no bisiesto
    elif mes == 2:
        if es_bisiesto(anno):
            return 29
        else:
            return 28
    else:
        # En caso contrario, tiene 31 días
        return 31

def esFecha(fecha: int) -> bool:
    anno =  int(str(fecha)[:4])
    mes = int(str(fecha)[4:6])
    dia = int(str(fecha)[6:])
    ## año no puede ser negativo
    if anno<0:
        return False
    ## el dia no puede ser mayor a los dias que tenga el mes
    elif dia>diasMes(mes, anno):
        return False
    ## El mes no puede ser mayor a 12
    elif mes>12:
        return False
    else:
        return True

def añosEntre(fecha1: int, fecha2: int) -> int:
    anno1 =  int(str(fecha1)[:4])
    anno2 =  int(str(fecha2)[:4])
    return anno1-anno2

def agregarCero(num: int) -> str:
    if num>=9:
        return "0{}".format(num)
    else:
        return str(num)

def diaSiguiente(fecha: int) -> int:
    anno =  int(str(fecha)[:4])
    mes = int(str(fecha)[4:6])
    dia = int(str(fecha)[6:])
    ## caso ultimo dia del año
    if (dia == diasMes(mes, anno)) & (mes==12):
        return int("{}0101".format(anno+1))
    ## Caso ultimo dia del mes
    elif (dia == diasMes(mes, anno)) & (mes<12):
        return int("{}{}01".format(anno, agregarCero(mes+1)))
    ## otros casos
    else:
        return int("{}{}{}".format(anno, str(fecha)[4:6], agregarCero(dia+1)))

def aTex(mes: int) -> str:
    if mes==1:
        return "Enero"
    elif mes==2:
        return "Febrero"
    elif mes==3:
        return "Marzo"
    elif mes==4:
        return "Abril"
    elif mes==5:
        return "Mayo"
    elif mes==6:
        return "Junio"
    elif mes==7:
        return "Julio"
    elif mes==8:
        return "Agosto"
    elif mes==9:
        return "Septiembre"
    elif mes==10:
        return "Octubre"
    elif mes==11:
        return "Noviembre"
    else:
        return "Diciembre"

def escribir(fecha:int) -> str:
    anno =  int(str(fecha)[:4])
    mes = int(str(fecha)[4:6])
    dia = int(str(fecha)[6:])
    return "{} {} {}".format(dia, aTex(mes), anno)
            
#%%
