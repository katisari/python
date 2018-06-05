# Bike
class Bike:
    def __init__(self, price, max_speed):
        self.miles = 0
        self.price = price
        self.max_speed = max_speed
    def displayInfo(self):
        print('Bike\'s price', self.price)
        print('Maximum speed', self.max_speed)
        print('Total miles', self.miles)
        return self
    def ride(self):
        print('Riding')
        self.miles += 10
        return self
    def reverse(self):
        print('Reversing')
        if (self.miles -5 >= 0):
            self.miles -= 5
        return self

bike1 = Bike(200, "25mph")
bike1.ride().ride().ride().reverse().displayInfo()

bike2 = Bike(100, "50mph")
bike2.ride().ride().reverse().reverse().displayInfo()

bike3 = Bike(10,'50mph')
bike3.reverse().reverse().displayInfo()



# Car
class Car:
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax=.15
        else:
            self.tax=.12

    def display_all(self):
        print("Price:", self.price)
        print("Speed:", self.speed)
        print("Fuel:", self.fuel)
        print("Mileage:", self.mileage)
        print("Tax:", self.tax, "\n")
        return self


car1=Car(2000,"35mph","Full", "15mpg")
car1.display_all()

car2=Car(2000, "5mph", "Not Full", "105mpg")
car2.display_all()

car3=Car(2000,"15mph", "Kind of Full", "95mpg")
car3.display_all()

car4=Car(2000, "25mph", "Full", "25mpg")
car4.display_all()

car5=Car(2000, "45mph", "Empty", "25mpg")
car5.display_all()

car6=Car(20000000, "35mph", "Empty", "15mpg")
car6.display_all()




# Product

class Product:
    def __init__(self, price, item_name, weight, brand):
        self.status = "for sale"
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand

    def sell(self):
        self.status = "sold"
        return self
    def add_tax(self, tax):
        self.price *= (1 + tax)
        return self

    def return_item(self, reason_for_return):
        if reason_for_return == "defective":
            self.status = "defective"
            self.price = 0
        if reason_for_return == "like new":
            self.status = "for sale"
        if reason_for_return == "opened":
            self.status = "used"
            self.price *= 0.8
        return self
    def display_info(self):
        print("Price:", self.price)
        print("Item name:", self.item_name)
        print("Weight:", self.weight)
        print("Brand:", self.brand)
        print("Status:", self.status)
        return self

bottle = Product(3, "water bottle", "150g", "Ice Mountain")
bottle.add_tax(0.2).display_info()
