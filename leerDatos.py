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
    def __iter__(self):
        return iter([self.buying, self.maint, self.doors, self.persons, self.lug_boot, self.safety])
    def __init__(self, buying, maint , doors, persons, lug_boot, safety):
        self.maint = maint
        self.doors = doors
        self.lug_boot = lug_boot
        self.safety = safety
        self.buying = buying
    def __init__(self, args):
        self.maint = args[0]
        self.doors = args[1]
        self.lug_boot = args[2]
        self.safety = args[3]
        self.buying = args[4]


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

extraer10PorcientoDeCarros(cars_info)

def guardarArchivoDiezPorciento(nombreArchivo):
    file_object  = open(nombreArchivo, 'wb')
    wr = csv.writer(file_object, quoting=csv.QUOTE_NONE)
    for car in cars_info:
        wr.writerow(list(car.__iter__()))
    file_object.close()
guardarArchivoDiezPorciento('hola.txt')
