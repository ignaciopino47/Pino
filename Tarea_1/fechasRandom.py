from fecha import *
from random import randint

## fechaRandom: None -> int
## función que retorna un int de fecha entre el 1 enero 1900 y el 31 diciembre 2021
## ejemplo: fechaRandom() >= 19000101
## ejemplo: fechaRandom() <= 20211231
def fechaRandom():
    anno = randint(1900, 2021)
    mes = randint(1,12)
    dia = randint(1, diasMes(mes, anno))
    return int("{}{}{}".format(anno, agregarCero(mes), agregarCero(dia)))

## Test
assert fechaRandom() >= 19000101
assert fechaRandom() <= 20211231

## fechasRandom: int ->
## función que escribe en pantalla una N fechas random junto a su dia siguiente
def fechasRandom(N):
    for i in range(N):
        fec = fechaRandom()
        escribir(fec)
        escribir(diaSiguiente(fec))

## formatear: int -> int
## función que formatea un int de fecha (DDMMAAAA) a un int fecha (AAAAMMDD)
## ejemplo: formatear("01011900") == 19000101
## ejemplo: formatear("31122021") == 20211231
def formatear(fecha):
    fecha = str(fecha)
    if len(fecha)<8:
        fecha = "0"+str(fecha)
    anno =  int(fecha[4:])
    mes = int(fecha[2:4])
    dia = int(fecha[:2])
    return int("{}{}{}".format(anno, agregarCero(mes), agregarCero(dia)))

## Test
assert formatear(1011900) == 19000101
assert formatear(31122021) == 20211231

def años(fecha):
    fec = input("Fecha (DDMMAAAA)?: ")
    if fec == "0":
        pass
    else:
        while not esFecha(formatear(fec)):
            fec = input("Fecha incorrecta, favor ingresar nuevamente (DDMMAAAA): ")
        escribir(formatear(fecha))
        print("Diferencia de años: {}".format(añosEntre(formatear(fecha), formatear(fec))))
        años(fecha)
