# print("hi")
# print(8+8)
# x = "Python"
# y = "is"
# z = "awesome"
# print(x, y, z)
# x = "Python "
# y = "is "
# z = "awesome"
# print(x + y + z)

# x = "awesome"

# def myfunc():
#   print("Python is " + x)
#   y = "not awesome"
#   print(y)

# myfunc()
#------------------------------------------------------------------------------------------
#practise questions of loop

#Q Write a program that calculates the sum of all numbers from 1 to a given number n.
# n=int(input("Enter a number: "))
# sum=0
# for value in range(1,n,+1):
#     sum += value


# print (f" sum of all numbers from 1 to a given number {n} is: {sum}")
 
 #Q Develop a program that finds all prime numbers within a given range using loops
# n=100
# for i in range(1,n+1):
#     if i<11:
#         if i>1 and i<=3:
#             print(i, end=", ")
#         if i>3 and i<11:
#             if i%2==0 or i%3==0:
#                print()
#             else:
#                 print(i, end=", ")
#     elif i>=11:
#         if i%2==0 or i%3==0 or i%5==0 or i%7==0 :
#             print()
#         else:
#             print(i, end=", ")
# (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
# n=100
# for i in range(1,n+1):
#     if i<11:
#        if i>1 and i<=3:
#            print(i,end=",")
#        if i>3 or i<11:
#         if(i%2==0) or (i%3==0):
#              print()
#         else:
#             print(i,end=",")
#     elif i>=11: 
#         if i%2==0 or i%3==0 or i%5==0 or i%7==0:
#          print()  
#         else:
#             print(i, end=", ")
# import math

# def is_prime(n):
#     if n <= 1:
#         return False
#     elif n <= 3:
#         return True
#     elif n % 2 == 0 or n % 3 == 0:
#         return False
#     i = 5
#     while i * i <= n:
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
#         i += 6
#     return True

# Example usage:
# number = 100
# print(f"{number} is prime: {is_prime(number)}")
# (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
# Q: Write a program to print various patterns (e.g., stars, numbers) using loops.       

# rows = int(input("Enter the number of rows for the pyramid: "))

# for i in range(1, rows + 1):
#     print(" " * (rows - i) + "*" * (2 * i - 1)) 
#---------------------------------------------------------------------------  
# row=5
# for i in range(1,row+1,1):
#     for j in range(1,i+1):
       
#      print(j, end="")
#     print("")



#---------------------------------------------------------------------------------------
#Q :Find the factorial of a given number
#n=int(input("enter number:" ))
# n=5
# result=1
# if(n<0):
#     print("Factorial does not exist for negative numbers")
    
# elif(n==0):
#     print("The factorial of 0 is 1")
# else:

#  for i in range(1,n+1):
#     result*=i
#  print("fictorial of",n,"is:",result)

# n=5
# for i in range(1,n+1):#the step size is implicitly assumed to be 1 range(1,n+1,1) so no need to write 
#     for j in range(1,i+1):
#         print(j,end="")
#     print("")  
#q:reverse number pattrens
# n=5
# for i in range(0,n+1):
#     for j in range(n-i,0,-1):
#         print(j,end="")
#     print("")  
#q:number=[1,-2,3,-4,5,6,-7,-8,9,10] find negative numbers
# number=[1,-2,3,-4,5,6,-7,-8,9,10]

# for n in number:
#     if(n<0):
#         print(n)


#Q:sum of even numbers
# n=int(input("enter a number: "))
# j=0
# for i in range(1,n+1):
#     if (i%2==0):
#        j+=1
# print(j)  
#q: is num even 

# n = int(input("Enter a number: "))

# if n % 2 == 0:
#     print("Even number:", n)
# else:
#     print("Not an even number")

# n=int(input("enter number: "))

# for i in range(1,11):
#     if i==5:
#         continue
#     print(n,"*",i,"=",n*i)
#Q:find first unique character
# word="anam"
# for char in  word:
#     if word.count(char)==1:
#         print("char is : ",char)
#         break
# number=5
# fictorial=1
# while number>0:
#    # fictorial=fictorial*number
#     fictorial*=number
#      # number=number -1
#     number-=1
# print("fictorial value is:",fictorial)
 
# n=int(input("Enter an age:"))
# if n<13:
#     print("child")
# elif (n<20):
#     print("teenage")
# elif(n<60):
#     print("Adult")
# else:
#     print("senior")
# colour=input("enter fruit condition:")
# fruit="banana"


# if fruit == "banana":
#     if colour =="green":
#         c_f="unripe"#print("unripe") we can also write this way
#     elif colour=="yellow":
#         c_f="ripe"
#     elif colour=="brown":
#         c_f="overripe"
#     print(c_f)
#Q:
# oder_coffee=input("Enter a coffee oder: ")
# extra_shot=input("is extra shot in (yes/no): ").lower()
# coffee=""

# if extra_shot== "yes":
#     coffee=  oder_coffee + "coffee with extra shot"
# elif extra_shot=="no":
#     coffee= oder_coffee + "coffee"

# print(coffee)

#--------------------------------------------------------------

# password=input("Enter a password: ")
# password_length=len(password)
# if password_length < 6:
#     print("Weak")
# elif password_length <= 10:
#     print("Medium")
# else:
#     print("Strong")

# password=input("Enter a password: ")

# if len(password) < 6:
#     print("Weak")
# elif len(password) <= 10:
#     print("Medium")
# else:
#     print("Strong")
year=int(input("Enter year:"))
if (year % 400==0)or(year % 4==0 and year%100!=0):
    print("is a leap year")
else:
    print("not a leap year")












    



 

       
              
        
    






















