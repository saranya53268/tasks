                      #calculator
# class calculator:
#     def __init__(self):
#        self.a=int(input("enter first number:"))
#        self.b=int(input("enter second number:"))

# def add_number(self):
#     return self.a + self.b
   
# def sub_number(self):
#     return self.a - self.b

# def multiply_number(self):
#     return self.a * self.b
       
# def divide_number(self):
#     if self.b !=0:
#        return self.a / self.b
    

# cal =  calculator()
# print(cal.add_number())    
# print(cal.sub_number())
# print(cal.multiply_number())
# print(cal.divide_number())

               #positive or negative
# number=int(input("Enter a number:"))
# if number>0:
#     print("Positive number")
# else:
#     print("Negative number")
    
# number=int(input("Enter a number:"))
# if number%2==0:
#     print("Even number")
# else:
#     print("Odd number")

          #vowels

# vowels=["a","e","i","o","u"]
# letter=input("enter a letter:")
# if letter in vowels:
#     print(vowels)
# else:
#     print("consonant")
               #single and multiple
# num = int(input("enter a number:"))
# if -9 <= num <= 9:
#     print("single digit number")
# else:
#     print("multi digit number") 
# 

# string = input("Enter a string: ")

# count = 0
# for ch in string.lower():
#     if ch in "aeiou":
#         count += 1

# print("Number of vowels:", count)

# string = input("Enter a string: ")

# count = 0
# for ch in string.lower():
#     if ch.isalpha() and ch not in "aeiou":
#         count += 1

# print("Number of consonants:", count)

# string = input("Enter a string: ")

# reverse = string[::-1]

# print("Reversed string:", reverse)


# string = input("Enter a string: ")

# if string == string[::-1]:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")


# string = input("Enter a string: ")

# frequency = {}

# for ch in string:
#     if ch in frequency:
#         frequency[ch] += 1
#     else:
#         frequency[ch] = 1

# print("Character Frequencies:")
# for key, value in frequency.items():
#     print(key, ":", value)    