# 3. Write a program which contains one class named as Arithmetic. 
# Arithmetic class contains three instance variables as Value1, Value2. 
# Inside init method initialise all instance variables to 0. 
# There are three instance methods inside class as Accept(), Addition(), Subtraction(), Multiplication(), Division(). 
# Accept method will accept value of Value1 and Value2 from user. 
# Addition() method will perform addition of Value1, Value2 and return result. 
# Subtraction() method will perform subtraction of Value1,Value2 and return result. 
# Multiplication() method will perform multiplication of Value1, Value2 and return result. 
# Division() method will perform division of Value1, Value2 and return result. 
# After designing the above class call all instance methods by creating multiple objects.

class Arithmetic:
    def __init__(self):
        self.Ans = 0
        self.Value1 = 0 
        self.Value2 = 0

    def Accept(self):
        try:
            print("Enter the value1 : ")
            self.Value1 = int(input())

            print("Enter the Value2 : ")
            self.Value2 = int(input())
        except ValueError as vobj:
            print("Exception occurs due to : ",vobj)

    def Addition(self):
        self.Ans = self.Value1 + self.Value2
        return self.Ans

    def Subtraction(self):
        self.Ans = self.Value1 - self.Value2
        return self.Ans

    def Multiplication(self):
        self.Ans = self.Value1 * self.Value2
        return self.Ans

    def Division(self):

        try:
            self.Ans = self.Value1 / self.Value2
        except ZeroDivisionError as zobj:
            print("Exception occurs due to : ",zobj)

        return self.Ans

def main():
    obj1 = Arithmetic()
    print("Obj1 called...")

    obj1.Accept()
    ret = obj1.Addition()
    print("Addition is : ",ret)

    ret = obj1.Subtraction()
    print("Subtraction is : ",ret)

    ret = obj1.Multiplication()
    print("Multiplication is : ",ret)

    ret = obj1.Division()
    print("Division is : ",ret)

    obj2 = Arithmetic()
    print("Obj2 called...")

    obj2.Accept()
    ret = obj2.Addition()
    print("Addition is : ",ret)

    ret = obj2.Subtraction()
    print("Subtraction is : ",ret)

    ret = obj2.Multiplication()
    print("Multiplication is : ",ret)

    ret = obj2.Division()
    print("Division is : ",ret)

    obj3 = Arithmetic()
    print("Obj3 called...")

    obj3.Accept()
    ret = obj3.Addition()
    print("Addition is : ",ret)

    ret = obj3.Subtraction()
    print("Subtraction is : ",ret)

    ret = obj3.Multiplication()
    print("Multiplication is : ",ret)

    ret = obj3.Division()
    print("Division is : ",ret)

if __name__ == "__main__":
    main()
