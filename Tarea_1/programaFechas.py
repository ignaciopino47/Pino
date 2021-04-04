from fecha import *

fecNac = input("Fecha de nacimiento?: ")
while esFecha(fecNac):
    fecNac = input("Fecha incorrecta, favor ingresar nuevamente: ")
print(escribir(fecNac))
fecHoy = input("Fecha de hoy?: ")
while esFecha(fecHoy):
    fecHoy = input("Fecha incorrecta, favor ingresar nuevamente: ")
print("Fecha de mañana: {}".format(diaSiguiente(fecHoy)))
print("Edad en años mañana: {}".format(añosEntre(diaSiguiente(fecNac), fecHoy)))