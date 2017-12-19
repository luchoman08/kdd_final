import csv
"""
   buying       v-high, high, med, low
   maint        v-high, high, med, low
   doors        2, 3, 4, 5-more
   persons      2, 4, more
   lug_boot     small, med, big
   safety       low, med, high
"""
class CarsAcceptance:
    buying = ''
    maint = ''
    doors = ''
    persons = ''
    lug_boot = ''
    safety = ''

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
cars_info = []

def leerArchivo(ubicacionArchivo):
    SPAM_READER = csv.reader(open(ubicacionArchivo), delimiter=',')

    for row in SPAM_READER:
        cars_info.append(CarsAcceptance(row))
        print cars_info.pop().buying
    print len(cars_info)
leerArchivo('car/car.data')