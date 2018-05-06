class String:
    def get_string(self):
        self.s = input("Enter your string: ")
    def print_string(self):
        print(self.s.upper()) #Print uppercase letter
a = String()
a.get_string()
a.print_string()