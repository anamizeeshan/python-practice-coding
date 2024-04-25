
"""
x=6
y=8.9
print(type(x))
print(type(y))
................
fruits=["orange","banana","apple"]
x,y,z=fruits
print(x)
print(y) 
................
a=input("enter first number:" )
b=input("enter  secound number:" )

print(a<=b)
"""
#a="ayesha Zeeshan"
#print(a[1:5])
#print(a.endswith("ay"))
#a=(a.capitalize())
#print(a)
#print(a.replace("ayesha","anam"))
#print(a.find("e"))
#print(a.count("e"))


#x=input("enter first name: ")
#print(len(x))

#a="this $ is going up $ $"
#print(a.count("$") )

#light = "green"

#if(light=="red"):
   # print("stop")
#elif(light=="green"):
    #print("go")
#elif(light=="yellow"):
 #   print("look")


#a = int(input("enter odd or an even number : ") )
#rem = a % 2
#if(rem==0):
#    print("its even number")
#else:
 #   print("its odd number")    

#a = int(input("enter first  number : ") )
#b = int(input("enter secound number : ") )
#c = int(input("enter third number : ") )

#if(a>=b and a>=c):
 #   print("first number is largest " , a)
#elif(b>=c):
 #    print("secound number is largest " , b)
#else:
 #     print("third  number is largest " , c)

#a = int(input("enter a  number : ") )
#if(a%7==0):
   # print("multiple of 7")
#else:
 #   print("not a multiple")

# degree=[]
# a=degree.append(input("enter frist degree names: "))
# b=degree.append(input("enter secound degree names: "))
# c=degree.append(input("enter third degree names: "))
# print(degreeab
# )
# list1=[1,2,3]
# list2=[1,2,3]
# copy_list1=list1.copy()
# copy_list1.reverse()

# if(copy_list1==list1):
#     print("palindrom")
# else:
#     print("not palindrom")  
# a=["C","D","A","A","B","B","A"] 
# a.sort()
# print(a)

# 

# student ={
#     "name": "sahar",
#     "subject" : {
#         "phy" : 98,
#         "chem" : 96 ,
#         "maths" : 100 ,

#     }
    
# }

# new_dic={"name": "alian ","semester" : 3,"age": 18 ,}
# student.update(new_dic)
# print(student)

# collection=set()
# collection.add(1)
# collection.add(2)
# collection.add("ayesha")
# collection.add((1,2,3))
# collection.clear()
# print(len(collection))

# collection={"hello","world","amna","python"}
# print(collection.pop())
# print(collection.pop())
# print(collection.pop())

# set1={1,2,3}
# set2={2,3,4}
# print(set1.intersection(set2))

# dic={
#     "table": "a piace of furniture" ,
#     "cat": "a small animal",

    
# }
# print(dic)

# i=100
# while i >= 1 :
#     print(i)
#     i -=1
# n = int (input ("enter a number : "))
# i=1
# while  i<= 10 :
#    print(n*i)
#    i+=1
# num=[1,4,9,16,25,36,48,64,81,100]  
# i=0
# while i< len(num):
#     print(num[i])
#     i+=1

num=(1,4,9,16,25,36,48,64,81,100)
x=16

i=0
while i<len(num):
   if(num[i]==x):
    print("found it" , i)
    break
   else:
     print("finding..")
   i+=1
   print("end of loop")
        
# num=(1,4,9,16,25,36,48,64,81,100)
# x=64
# i=0
# for el in num:
#     if(el==x):
#         print(" found" , i)
    #i+=1
    
   