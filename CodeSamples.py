# Comments to have code snippets
a=10
b=20
print("The value of the sum of variables is: {}".format(a+b))

class Calculator() :
    def __init__(self):
        self.var1 = 10
        self.var2 = 20

    def __str__(self):
        return f"The sum of variables is: {self.var1+self.var2}"

c = Calculator()
print(c)


