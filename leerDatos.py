import csv
import math
import random
"""
    buying       v-high, high, med, low
    maint        v-high, high, med, low
    doors        2, 3, 4, 5-more
    persons      2, 4, more
    lug_boot     small, med, big
    safety       low, med, high
 """
cars_info = []
DiezPorcientoCarros = []

class CarsAcceptance:
    buying = ''
    maint = ''
    doors = ''
    persons = ''
    lug_boot = ''
    safety = ''
    acceptance = ''
    def __iter__(self):
        return iter([self.buying, self.maint, self.doors, self.persons, self.lug_boot, self.safety, self.acceptance])
    def __init__(self, buying, maint , doors, persons, lug_boot, safety, acceptance):
        self.maint = maint
        self.doors = doors
        self.lug_boot = lug_boot
        self.safety = safety
        self.buying = buying
        self.acceptance = acceptance
    def __init__(self, args):
        self.buying = args[0]
        self.maint = args[1]
        self.doors = args[2]
        self.persons = args[3]
        self.lug_boot = args[4]
        self.safety = args[5]
        self.acceptance = args[6]

def escribirEncabezados(wr):
    wr.writerow(list(car.__iter__()))

def leerArchivo(ubicacionArchivo):
    SPAM_READER = csv.reader(open(ubicacionArchivo), delimiter=',')

    for row in SPAM_READER:
        cars_info.append(CarsAcceptance(row))
    print len(cars_info)

leerArchivo('car/car.data') 

def extraer10PorcientoDeCarros(carros):
    DiezPorciento = int(math.ceil(len(carros) * 0.10 ))
    for i in range (0, DiezPorciento):
        DiezPorcientoCarros.append(carros[i])
        carros.pop(i)
print (list(cars_info[0].__iter__()))
extraer10PorcientoDeCarros(cars_info)


def guardarCarros(nombreArchivo, listaCarros, incognita=None):
    file_object  = open(nombreArchivo, 'wb')
    wr = csv.writer(file_object, quoting=csv.QUOTE_NONE)
    for car in listaCarros:
        if(incognita != None):
            car.acceptance = '?'
        wr.writerow(list(car.__iter__()))
    file_object.close()

guardarCarros('cars.entrenamiento.data', cars_info)
guardarCarros('cars.pruebas.data', DiezPorcientoCarros)
guardarCarros('cars.pruebas.incognita.data', DiezPorcientoCarros, '?')
