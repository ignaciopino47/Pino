from fecha import *

fecNac = input("Fecha de nacimiento?: ")
while not esFecha(fecNac):
    fecNac = input("Fecha incorrecta, favor ingresar nuevamente: ")
escribir(fecNac)
fecHoy = input("Fecha de hoy?: ")
while not esFecha(fecHoy):
    fecHoy = input("Fecha incorrecta, favor ingresar nuevamente: ")
escribir(fecHoy)
print("Fecha de mañana: ")
escribir(diaSiguiente(fecHoy))
print("Edad en años mañana: {}".format(añosEntre(fecHoy, diaSiguiente(fecNac))))