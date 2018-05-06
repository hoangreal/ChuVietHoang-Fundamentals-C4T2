class Rectangle:
    def __init__(self,w,h): #Create a function that allows you to input something
        self.width = w
        self.height = h
    def print_w_h(self):
        print(self.width * self.height)
w = int(input("W: "))
h = int(input("H: "))
a = Rectangle(w,h)
a.print_w_h()