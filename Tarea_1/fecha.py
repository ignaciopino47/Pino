## es_bisiesto: int -> bool
## Función que entrega True en caso de que el año sea bisiesto
## ejemplo: es_bisiesto(2000) == True
def es_bisiesto(anno):
    return anno % 4 == 0 and (anno % 100 != 0 or anno % 400 == 0)

## Test
assert es_bisiesto(2000) == True

## diasMes: int, int -> int
## función que retorna los días que tiene un mes en un respectivo año
## ejemplo: diasMes(2,2021) == 28
## ejemplo: diasMes(2,2020) == 29
def diasMes(mes, anno):
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
        # En caso contrario, tiene 31 dias
        return 31

## Test
assert diasMes(2,2021) == 28
assert diasMes(2,2020) == 29

## esFecha: int -> bool
## función que retorna verdadero si el entero ingresado corresponde a una fecha
## ejemplo: esFecha(20210331) == True
## ejemplo: esFecha(18100931) == False
def esFecha(fecha):
    anno =  int(str(fecha)[:4])
    mes = int(str(fecha)[4:6])
    dia = int(str(fecha)[6:])
    ## el dia no puede ser mayor a los dias que tenga el mes
    if dia>diasMes(mes, anno):
        return False
    ## El mes no puede ser mayor a 12
    elif mes>12:
        return False
    else:
        return True

## Test
assert esFecha(20210331) == True
assert esFecha(18100931) == False

## añosEntre: int, int -> int
## función que retorna los años entre dos fechas
## ejemplo: añosEntre(20210330,18100918) == 210
## ejemplo: añosEntre(18100918,20210918) == 211
def añosEntre(fecha1, fecha2):
    mesdia1 = int(str(fecha1)[4:])
    mesdia2 = int(str(fecha2)[4:])
    anno1 =  int(str(fecha1)[:4])
    anno2 =  int(str(fecha2)[:4])
    if mesdia1 >= mesdia2:
        return abs(anno1-anno2)
    else:
        return abs(anno1-anno2-1)

## Test
assert añosEntre(20210330,18100918) == 210
assert añosEntre(18100918,20210918) == 211

## agregarCero: int -> str
## función que retorna un string con el numero mas un cero si el numero es menor a 10
## ejemplo: agregarCero(0) == "09"
def agregarCero(num):
    if num<=9:
        return "0{}".format(num)
    else:
        return str(num)

## Test
assert agregarCero(9) == "09"

## diaSiguiente: int -> int
## función que retorna un int que corresponde al dia siguiente del int ingresado
## ejemplo: diaSiguiente(20210330) == 20210331
## ejemplo: diaSiguiente(20201231) == 20210101
def diaSiguiente(fecha):
    anno =  int(str(fecha)[:4])
    mes = int(str(fecha)[4:6])
    dia = int(str(fecha)[6:])
    ## caso ultimo dia del anno
    if (dia == diasMes(mes, anno)) & (mes==12):
        return int("{}0101".format(anno+1))
    ## Caso ultimo dia del mes
    elif (dia == diasMes(mes, anno)) & (mes<12):
        return int("{}{}01".format(anno, agregarCero(mes+1)))
    ## otros casos
    else:
        return int("{}{}{}".format(anno, str(fecha)[4:6], agregarCero(dia+1)))

## Test
assert diaSiguiente(20210330) == 20210331
assert diaSiguiente(20201231) == 20210101

## aTex: int -> str
## función que retorna un string con el nombre del mes correspondiente al int ingresado
## ejemplo: aTex(1) == "Enero"
def aTex(mes):
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

## Test
assert aTex(1) == "Enero"

## escribir: int ->
## función que retorna la fecha escrita para un int ingresado
## ejemplo: escribir(20210330) == "30 Marzo 2021"
## ejemplo: escribir(20210501) == "1 Mayo 2021"
def escribir(fecha):
    anno =  int(str(fecha)[:4])
    mes = int(str(fecha)[4:6])
    dia = int(str(fecha)[6:])
    print("{} {} {}".format(dia, aTex(mes), anno))