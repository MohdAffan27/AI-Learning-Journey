# print the square root of a number
class calculator:
    def __init__(self,n):
        self.n = n

    def square(self):
        print(f"The square is {self.n*self.n}")
    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")
    def squareroot(self):
        print(f"The square root is {self.n**1/2} ")

a = int(input("Enter your number: "))
b = calculator(a)
b.square()
b.cube()
b.squareroot()