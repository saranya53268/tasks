 # print("\n" + "="*30)
 # a = int(input("Enter first number: "))
 # b = int(input("Enter second number: "))
 # calc3 = Calculator(a, b)
 # print(f"\nResult for {a} and {b}:")
 # print(f"Add      : {calc3.add()}")
 # print(f"Subtract : {calc3.subtract()}")
 # print(f"Multiply : {calc3.multiply()}")
# print(f"Divide   : {calc3.divide()}")       

# class Calculator:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def add(self):
#         return self.a + self.b



# import random

# number = random.randint(1, 100)
# attempts = 0

# print("Welcome to Number Guessing Game")

# while True:
#     guess = int(input("Enter your guess (1-100): "))
#     attempts += 1

#     if guess < number:
#         print("Too Low")
#     elif guess > number:
#         print("Too High")
#     else:
#         print("Congratulations! You guessed the number.")
#         print("Attempts:", attempts)
#         break

class calculator:
    def __init__(self):
       self.a=int(input("enter first number:"))
       self.b=int(input("enter second number:"))

 def add_number(self):
    return self.a + self.b
   
def sub_number(self):
    return self.a - self.b

def multiply_number(self):
    return self.a * self.b
       
def divide_number(self):
    if self.b !=0:
       return self.a / self.b
    

cal =  calculator()
print(cal.add_number())    
print(cal.sub_number())
print(cal.multiply_number())
print(cal.divide_number())