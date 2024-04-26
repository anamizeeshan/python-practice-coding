# numTuple = (1,4,9,16,25,36,48,64,81,100)#tuple
# x = 16 #find this value in tuple

# i = 0 #counter
# for element in numTuple:
#     if(element == x):
        
#         print("found at this index", i)
#     i+=1        

# i = 0
# for element in numTuple:
#     print("found ",element, " at this index", i)
#     i+=1  

# for i in range(10):#stop
#     print(i)


# for i in range(2,10):#(start,stop)
#     print(i)

# for i in range(2,10,2):#(start?,stop,step?)
#     print(i)
# n=int(input("enter value"))
# for i in range(1,11):
#     print(n*i)

# functions..................................

# def calc_sum(a,b):
#     sum=a+b
#     print(sum)
#     return(sum)



# calc_sum(5,10)
#we can write above  function in this way
# def calc_sum(a,b):
#     print(a+b)# comment this statment after comment out line 41 or 42
#     return a+b
# print(sum)

# sum=calc_sum(2,4)
# def print_hello():
#     print("hello")


# print_hello()

# def print_hello():
#     print("hello")

# # in function no value in return output gives none  
# output=print_hello()
# print(output)
# n=int(input("enter an integer"))
# i=1

# while i<=10:
#     print(n*i)


#     i+=1   

# num=[1,4,9,16,25,36,48,64,81,100]  
# i=0
# while i< len(num):
#     print(num[i])
#     i+=1
# num=(1,4,9,16,25,36,48,64,81,100)
# x=1

# i=0
# while i<len(num):
#    if(num[i] ==x):
#     print("found it" , i)
     
#    i+=1

# num=(1,4,9,16,25,36,48,64,81,100)
# x=25
# i=0
# while i<len(num):
#    if(num[i]  x):
#     print("found it" , i)
    
#    i+=1

# Q) search a next number x using a  loop
# num=[1,4,9,16,25,36,48,64,81,100]
# x= 100
# i=0
# while i<len(num):
#     if(num[i] == x):
#      break
    
#     i+=1 

# if(i==len(num)-1):
#        print("last element")
# else:
#     nextNo=num[i+1]
#     print("after",x,"is",nextNo)
#-------------------------------------------------
     
# i=0
# while i<=10:
#     if i==3:
#         i+=1
#         continue#skip the iteration
#     print(i)
#     i+=1
#----------------------------------------------------------

# i=0
# while i<=5:
#     print(i)
#     if i==3:
#         break
   
#     i+=1

# print("end of loop")
 #----------------------------------------------------------

# sum=0


# i=10
# while i >=0:
#      print ("enter number")
#      num = input()
#      sum=sum+num
     
#      i=i-1
 
#      print("average",sum/10.0)
#----------------------------------------------------------------
#Q  : input = 01100101001; output ==> 00000011111
# x=[1,"1",0,0,0,1,1,1,0,0,1]
# # x.sort()
# # print(x)
# i=0
# j=0
# for num in x:
#     if(num==0):
#         i+=1
#     elif(num==1):
#         j+=1
#     elif(num=="1"):
#         j+=1

# list=[0]*i+[1]*j
# print("list",list) 
      

    

#Q  : input = abacabadda; output ==> a=5, b=2, c=1, d=2
# alp=["a","b","a","c","a","b","a","d","d","a","z"]
# #alp=[1,2,4,5]
# alphabets=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
# freq_alp=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# # print(ord(alphabets[0]))
# for value in alp:
#     for alphabet in alphabets:
#         if (value==alphabet):
#             index = alphabets.index(alphabet)
#             freq_alp[index]+=1
#             break

# print(freq_alp)
#---------------------------------------------------------------------------
# input_string = "abacabadda"
# character_count = {}
# # print(type(character_count))

# for char in input_string:
#     if char in character_count:
#         character_count[char] += 1
#     else:
#         character_count[char] = 1
#     for charx, countx in sorted(character_count.items()):
#         print(f"{charx}={countx}", end=",")
#     print()



#Q1: input = how to remove spaces from sentence;  output==> howtoremovespacesfromsentence 

# sentence = "how to remove spaces from sentence"
# Sentence_Without_Spacing = " "
# for chr in sentence:
#     if chr !=" " :
        
#      Sentence_Without_Spacing +=chr
     
# print( "Sentence_Without_Spacing :",Sentence_Without_Spacing)
     

#Q2:how to find distinct letters from the sentence without spaces(don't considerd spaces)
#input=:how to find distinct letters from the sentence without spaces: output==>howtfindsclermhu

# sentence="how to find distinct letters from the sentence without spaces"
# unique_Sentence_Without_Spacing = ""

# for chr in sentence:
#     if chr !=" " :
#      if chr not in unique_Sentence_Without_Spacing: 
        
#       unique_Sentence_Without_Spacing +=chr
     
# print( "unique_Sentence_Without_Spacing :",unique_Sentence_Without_Spacing)





#Q3:how to separate letters  from words. input= banana; output==> b a n a n a
# word="banana"
# s=""
# for strxx in word:
#   s=strxx + " "
#   print(strxx)

#Q4:input=reverse a word; output==> esrever
# reverse_word="reverse"
# rev=reverse_word[::-1]
# print(rev)
#-----------------------------------------------------------

# reverse_input_word="reverse "
# reverse_word=""

# for char in reverse_input_word:
#     reverse_word=char + reverse_word
# print("reverse_word: ",reverse_word)


#Q5:reverse words in a sentence 
# reverse_word="reverse words in a sentence "
# rev=reverse_word[::-1]
# print(rev)
#---------------------------------------------------------
# reverse_input_sentence="reverse words in a sentence"
# reverse_sentence=""
# for char in reverse_input_sentence:
#     reverse_sentence=char + reverse_sentence
# print("reverse_sentence: ",reverse_sentence)

# #Q6: reverse a number =12345==>54321
123
# reverse_number="12345"
# rev=reverse_number[::-1]
# print(rev)
#-------------------------------------------------------------------------
# reverse_input_number="12345"
# reverse_number=""
# for char in reverse_input_number:
#     reverse_number=char + reverse_number
# print("reverse_number: ",reverse_number)
   


#Q7:reverse words in a sentence and then reverse a sentence

# reverse_word="reverse words in a sentence "
# rev=reverse_word[::-1]
# print(rev)
