# 1. Write a python program to create a function that takes a list and returns a new list
# with the original list's unique elements.
# 2. Write a python program to create a function that takes a number as a parameter and
# checks if the number is prime or not.
# 3. Write a python program to create a function that prints the even numbers from a
# given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 4. Write a python program to create a function that checks whether a passed string is
# palindrome or not.
# 5. Write a python program to create a function to find the Min of three numbers.
# 6. Write a python program to create a function and print a list where the values are
# square of numbers between 1 and 30.
# 7. Write a python program to access a function inside a function.
# 8. Write a python program to create a function that accepts a string and calculate the
# number of upper case letters and lower case letters.
# 9. Write a python program to create a function to check whether a string is a pangram
# or not.
# 10. Write a python program to create a function to check whether a string is an anagram
# or not


# 1) ....................................................
# def new_list1(a):
#     return a
    
# print(new_list1([1,2,34,5]))


# 2) ..................................................
# def prime(a):
#     c=0
#     for i in range(1,a+1):
#         if a%i==0:
#            c+=1
        
#     if c==2:
#         return True
#     else:
#         return False
                  
# while True:
#     ans=input('To continue [y/n] : ')
#     if ans=='y':
#         print(prime(int(input("Enter n : "))))
#     else:
#         break


# 3) ...........................................................
# even=[]
# odd=[]
# def print_even_no(x):
#     for i in x:
#         if i%2==0:
#             even.append(i)
#     print(even)
    
# Sample_List =[1, 2, 3, 4, 5, 6, 7, 8, 9]
# print_even_no(Sample_List)

    
# 4) .....................................
# def pelondromic(x):
#     for i in range(0,len(x)):
#         if str1[i]==str1[len(str1)-1-i]:
#             print("Palondramic")
#             break
#         else:
#             print("Not palondromic")
#             break
    

# str1=input("Enter a string to check palondramic or not : ")
# pelondromic(str1)

# # for i in range(0,len(str1)):
# #     if str1[i]==str1[len(str1)-1-i]:
# #         print("pelondramic")
# #         break
# #     else:
# #         print("not")
# #         break



# 5) ......................................................
# def min_no(a,b,c):
#     # print(min(a,b,c))
#     return min(a,b,c)
      
# print(min_no(int(input("Enter a : ")),int(input("Enter a : ")),int(input("Enter a : "))))


# 6) ...................................................
# def square(a):
#     l=[]
#     for a in range(1,a+1):
#         l.append(pow(a,2))
#     print(l)
           
# square(int(input("Enter n : ")))


# 7) ..................................................
# def f1():
#     print("hello hari")
#     f2()
    
# def f2():
#     print("hiiiii")

# f1()


# 8) .....................................
# def calcute(str1):
#     up=0
#     lo=0
#     for char in str1:
#         if char.islower():
#             lo+=1
#         elif char.isupper():
#             up+=1
#         else:
#             pass
#     return(lo,up)
    
# print(calcute(input("Enter string : ")))


# 9) ..........................................
