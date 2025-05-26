# 1. Write a program which contains one class named as Demo. 
# Demo class contains two instance variables as no1, по2. 
# That class contains one class variable as Value. 
# There are two instance methods of class as Fun and Gun which displays values of instance variables. 
# Initialise instance variable in init method by accepting the values from user. 

# After creating the class create the two objects of Demo class as 
# Obj1 = Demo(11,21) 
# Obj2 = Demo(51,101) 

# Now call the instance methods as 
# Obj1.Fun() 
# Obj2.Fun() 
# Obj1.Gun() 
# Obj2.Gun() 

class Demo:

    Number3 = 151    # class variable 

    def __init__(self,Number1,Number2):
        self.No1 = Number1      # Instance variable
        self.No2 = Number2

    def Fun(self):
        print("Inside Fun method...")
        print("Value of No1 is : ",self.No1)
        print("Value of No2 is : ",self.No2)


    def Gun(self):
        print("Inside Gun method...")
        print("Value of No1 is : ",self.No1)
        print("Value of No2 is : ",self.No2)

def main():

    print("This is class variable value : ",Demo.Number3)

    obj1 = Demo(11,21)
    obj2 = Demo(51,101)

    obj1.Fun()
    obj2.Fun()

    obj1.Gun()
    obj2.Gun()

if __name__ == "__main__":
    main()

