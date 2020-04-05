from google.appengine.ext import ndb
class ElectricVehicles(ndb.Model):
def __init__(self, name, manufacturer, year, batterysize, range, cost, power):
        self.__name  = name
        self.__manufacturer = manufacturer
        self.__year = year
        self.__batterysize = batterysize
        self.__range = range
        self.__cost = cost
        self.__power = power

    def iName(self, name):
        self.__name = name

    def iManufacturer(self, manufacturer):
        self.__manufacturer = manufacturer

    def iYear(self, year):
        self.__year = year

    def iBatterysize(self, batterysize):
        self.__batterysize = batterysize

    def iRange(self, range):
        self.__range = range

    def iCost(self, cost):
            self.__cost = cost

    def iPower(self, power):
                self.__power = power

    def getName(self):
        return self.__name

    def getManufacturer(self):
        return self.__manufacturer

    def getYear(self):
        return self.__year

    def getBatterysize(self):
        return self.__batterysize

    def getRange(self):
        return self.__range

    def getCost(self):
            return self.__cost

    def getPower(self):
                return self.__power

    def Display_Vehicle(self):
        print('Vehicle name: %s' % self.__class__.name)
        print('Manufacturer: ' , self.__manufacturer)
        print('Year: ' , self.__year)
        print('Batterysize: ' , self.__batterysize)
        print('Range: ' , self.__range)
        print('Cost: ', self.__cost)
        print('Power: ', self.__power)

class BMWi3(Vehicle):
    name = 'Car'
    def __init__(self, name, manufacturer, year, batterysize, range, cost, power):
        Vehicle.__init__(self, name, manufacturer, year, batterysize, range, cost, power)
        self.Display_Vehicle()

class BYDe6(Vehicle):
    name = 'BYDe6'
    def __init__(self,name, manufacturer, year, batterysize, range, cost, power):
        Vehicle.__init__(self, name, manufacturer, year, batterysize, range, cost, power)
        self.Display_Vehicle()

class BMWi8(Vehicle):
    name = 'BMWi8'
    def __init__(self, name, manufacturer, year, batterysize, range, cost, power):
        Vehicle.__init__(self, name, manufacturer, year, batterysize, range, cost, power)
        self.Display_Vehicle()

class TeslaS(Vehicle):
    name = 'TeslaS'
    def __init__(self, name, manufacturer, year, batterysize, range, cost, power):
        Vehicle.__init__(self, name, manufacturer, year, batterysize, range, cost, power)
        self.Display_Vehicle()


def main():
    electricvehicles = []
    while True:

        if classType == 'BMWi3':
            name    = print('BMWi3' % ElectricVehicles)
            manufacturer   = print('BMW' % ElectricVehicles)
            year    = print('2013' % ElectricVehicles)
            batterysize = print('33kwh' % ElectricVehicles)
            range   = print('16hr' % ElectricVehicles)
            cost  = print('46280 euros' % ElectricVehicles)
            power = print('33kw' % ElectricVehicles)
        elif classType == 'BYDe6':
            name    = print('BYDe6' % ElectricVehicles)
            manufacturer   = print('BYD' % ElectricVehicles)
            year    = print('2010' % ElectricVehicles)
            batterysize = print('61kwh' % ElectricVehicles)
            range   = print('20hr' % ElectricVehicles)
            cost  = print('$35000' % ElectricVehicles)
            power = print('7.4kw' % ElectricVehicles)
        elif ElectricVehicles == 'BMWi8':
            name    = print('BMWi8' % ElectricVehicles)
            manufacturer   = print('BMW' % ElectricVehicles)
            year    = print('2014' % ElectricVehicles)
            batterysize = print('50kwh' % ElectricVehicles)
            range   = print('15hr ' % ElectricVehicles)
            cost  = print('149290 euros' % ElectricVehicles)
            power = print('7.4kw' % ElectricVehicles)
        elif ElectricVehicles == 'TeslaS':
            name    = print('TeslaS' % ElectricVehicles)
            manufacturer   = print('Tesla' % ElectricVehicles)
            year    = print('2012' % ElectricVehicles)
            batterysize = print('' % ElectricVehicles)
            range   = print(' ' % ElectricVehicles)
            cost  = print('$35000' % ElectricVehicles)
            power = print('100kw' % ElectricVehicles)
        print('\n\n')
            print( electricvehicles )
            break

if __name__ == '__main__':
    main()
