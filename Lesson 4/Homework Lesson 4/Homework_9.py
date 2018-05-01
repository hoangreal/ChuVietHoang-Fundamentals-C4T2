class Lunch:
    def __init__(self):  # make/embed Customer and Employee
        self.customer = Customer()
        self.employee = Employee()
    def order(self, foodName):  # start a Customer order simulation
        self.customer.placeOrder(foodName, self.employee)
    def result(self):  # ask the Customer about its Food
        self.customer.printFood()

class Customer:
    def __init__(self):  # initialize my food to None
        self.food = None
    def placeOrder(self, foodName, employee):  # place order with Employee
        self.food = employee.takeOrder(foodName)
    def printFood(self):  # print the name of my food
        print(self.food.store)

class Employee:
    def takeOrder(self, foodName):  # return a Food, with requested name
        return Food(foodName)

class Food:
    def __init__(self, name):  # store food name
        self.store= name

# Quy trình chạy:
# Nhập món ăn -> hàm order -> hàm placeOrder -> hàm takeOrder -> class Food -> Hàm printFood -> hàm result
Name = input("Enter your food: ")
Lunch = Lunch()
Lunch.order(Name)
Lunch.result()