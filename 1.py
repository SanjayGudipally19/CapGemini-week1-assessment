# 1.atm
# def check_balance(amount):
#     print(f'Balance is {amount}')
# def withdraw(amount):
#     money=int(input("Enter money to be withdrawn: "))
#     if money>amount:
#         print('insufficient balance')
#     else:
#         amount=amount-money
#         print('Money withdrawn')
#     print(f'Balance is {amount}')
#     return amount
# def deposit(amount):
#     money=int(input("Enter money to be deposited: "))
#     amount=amount+money
#     print('Money deposited')
#     print(f'Balance is {amount}')
#     return amount
# def exit():
#     print("Thank You")
#     return None
# def cal(amount):
#     print("1-Check Balance\n2-Withdraw\n3-Deposit\n4-Exit\n")
#     choice=int(input("Enter the option: "))
#     if choice==1:
#         check_balance(amount)
#     elif choice==2:
#         amount=withdraw(amount)
#     elif choice==3:
#         amount=deposit(amount)
#     elif choice==4:
#         return exit()
#     else:
#         print("Please enter correct option")
#     return cal(amount)    
# balance1=int(input("Enter balance: "))
# cal(balance1)
# ----------------------------------------------------------------------------------------
# 2.temperature conversion
# temp=float(input("enter temperature"))
# def ctof(temp):
#     result=(9/5*temp)+32
#     print(result)
# def ctok(temp):
#     result=temp+273.15
#     print(result)
# def ftoc(temp):
#     result=(temp-32)*(5/9)
#     print(result)
# def ftok(temp):
#     result=((temp-32)*(5/9))+273.15
#     print(result)
# def ktoc(temp):
#     result=temp-273.15
#     print(result)
# def ktof(temp):
#     result=((temp-273.15)*(9/5))+32
#     print(result)
# ctof(temp)
# ctok(temp)
# ftoc(temp)
# ftok(temp)
# ktoc(temp)
# ktof(temp)
# ----------------------------------------------------------------------------------------
# 3.numberguessing
# import random
# flag=1
# num=random.randrange(1,100)
# print(num)
# while(flag):
#     guess=int(input("guess the number"))
#     if num==guess:
#         print("perfect, your guess is right")
#         flag=0
#     elif guess>num:
#         print("your guess is high")
#     elif guess<num:
#         print("your guess is low")
# ----------------------------------------------------------------------------------------
# 4.student grade
# name=input("enter your name")
# science=int(input("enter science marks"))
# maths=int(input("enter maths marks"))
# social=int(input("enter social marks"))
# english=int(input("enter english marks"))
# biology=int(input("enter biology marks"))
# total=science+maths+social+english+biology
# print(f"your total marks are {total} ")
# percentage=(float)(total/500)*100
# if percentage>=90:
#     print(f"your percentage is {percentage} and your grade is A")
# elif percentage>=75 and percentage<90:
#         print(f"your percentage is {percentage} and your grade is B")
# elif percentage>=60 and percentage<75:
#         print(f"your percentage is {percentage} and your grade is C")
# elif percentage>=40 and percentage<60:
#         print(f"your percentage is {percentage} and your grade is D")
# else:
#         print(f"your percentage is {percentage} and your grade is F")
# ----------------------------------------------------------------------------------------
# 5.shopping cart
# def add():
#     name=input("Enter the item name: ")
#     price=int(input('Enter the price: '))
#     a.append([name,price]) 
# def view():
#     for i in a:
#         print(i)
# def total():
#     ans=0
#     for i in a:
#         ans+=i[1]
#     return ans
# a=[]
# while True:
#     ch=int(input("1.Add Item\n2.View Cart Items\n3.Total Price\n4.Exit\nEnter the option: "))
#     if(ch==1):
#         add()
#     elif(ch==2):
#         view()
#     elif(ch==3):
#         print(total())
#     else:
#         print("Thank you for shopping")
#         break
# ----------------------------------------------------------------------------------------
# 6.prime numbers in range
# def isprimes(n):
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
# a = int(input("enter first number: "))
# b = int(input("enter second number: "))
# for i in range(a, b):
#     if isprimes(i):
#         print(i, end=' ')
# ----------------------------------------------------------------------------------------
# 7.loaneligibility
# age=int(input("enter your age"))
# salary=int(input("enter your salary"))
# credit_score=int(input("enter your credit score"))
# if age>=18:
#     if salary>300000:
#         if credit_score>1000:
#             print("Loan approved")
#         else:
#             print("Loan rejected because of your low credit score")
#     else:
#          print("Loan rejected because of your low salary")
# else:
#     print("Loan rejected because of underage")
# ----------------------------------------------------------------------------------------
# 8.table generator
# a=int(input("enter any number: "))
# b=int(input("enter range of the table: "))
# for i in range(1,b+1):
#     print(f"{a}*{i}={a*i}")
# ----------------------------------------------------------------------------------------
# 9.analyze string
# a=input("enter the string: ")
# vowel,conso,digit,special=0,0,0,0
# h=a.lower()
# for i in range(0,len(h)):
#     if h[i] in ('a','e','i','o','u'):
#         vowel+=1
#     elif(h[i]>='a' and h[i]<='z'):
#         conso+=1
#     elif(h[i]>='0' and h[i]<='9'):
#         digit+=1
#     else:
#         special+=1
# print(f"number of vowels are {vowel}\nnumber of consonents are {conso}\nnumber of digits are {digit}\nnumber of special characters are {special}\n")
# revers=a[::-1]
# print(revers)
# ----------------------------------------------------------------------------------------
# 10.billsplitter
# bill=float(input("enter bill amount"))
# people=int(input("enter number of people"))
# tip=int(input("enter tip percentage"))
# bill_percentage=float((tip/100)*bill)
# total=bill+bill_percentage
# pay=total/people
# print(f"Amount of money each person has to pay is {pay}")
# ----------------------------------------------------------------------------------------
# 11.passwordchecker
# password=input("Enter the password: ")
# n=len(password)
# up,low,digit,special=0,0,0,0
# if n<8:
#     print("Password must be atleast 8 characters")
# else:
#     for i in password:
#         if i.isalpha():
#             if i.lower()==i:
#                 low+=1
#             else:
#                 up+=1
#         elif i.isdigit():
#             digit+=1
#         else:
#             special+=1
# if(up and low and digit and special):
#     print("strong password")
# else:
#     print("weak password")
# ----------------------------------------------------------------------------------------
# 12.pattern
# a=int(input("Enter a number: "))
# for i in range(1,a+1):
#     print('*'*i)
# n=input("If you want to print the above pattern in reverse please type 'yes' or else please type 'no' \n")
# if n=='yes':
#     for i in range(a):
#         print((a-i)*'*')
# ----------------------------------------------------------------------------------------
# 13.palindrome
# def is_palindrome(value):
#     return str(value) == str(value)[::-1]
# while True:
#     a = input("Enter a string or number to check for palindrome (or type 'exit' to quit): ")
#     if a.lower() == 'exit':
#         break
#     if is_palindrome(a):
#         print(f"'{a}' is a palindrome.")
#     else:
#         print(f"'{a}' is not a palindrome.")
# ----------------------------------------------------------------------------------------
# 14.factorial
# def factorial(n):
#     if n < 0:
#         return "Factorial of a negative number doesn't exist."
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result
# try:
#     num = int(input("Enter a number: "))
#     print(f"The factorial of {num} is {factorial(num)}")
# except ValueError:
#     print(" Please enter a valid integer.")
# ----------------------------------------------------------------------------------------
# 15.leapyear
# def is_leap_year(year):
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         return True
#     else:
#         return False
# while True:
#     year = input("Enter a year (or type 'exit' to quit): ")
#     if year.lower() == 'exit':
#         break
#     year = int(year)
#     if is_leap_year(year):
#      print(f"{year} is a leap year.")
#     else:
#        print(f"{year} is not a leap year.")
# ----------------------------------------------------------------------------------------
# 16.odd and even 
# def separate(numbers):
#     odd_numbers = []
#     even_numbers = []
#     for number in numbers:
#         if number % 2 == 0:
#             even_numbers.append(number)
#         else:
#             odd_numbers.append(number)
#     return odd_numbers, even_numbers
# numbers = list(map(int, input("Enter a list of numbers: ").split()))
# odd_numbers, even_numbers = separate(numbers)
# print(f"Odd numbers: {odd_numbers}")
# print(f"Even numbers: {even_numbers}")
# ----------------------------------------------------------------------------------------
# 17.word counter
# from collections import Counter
# sentence = input("Enter a sentence: ")
# words = sentence.split()
# word_count = Counter(words)
# for word, count in word_count.items():
#     print(f"'{word}': {count}")
# ----------------------------------------------------------------------------------------
# 18.bmi
# def calculate(weight, height):
#     bmi = weight / (height ** 2)
#     return bmi
# def category(bmi):
#     if bmi < 18.5:
#         return "Underweight"
#     elif 18.5 <= bmi < 24.9:
#         return "Normal"
#     elif 25 <= bmi < 29.9:
#         return "Overweight"
#     else:
#         return "Obese"
# weight = float(input("Enter your weight in kg: "))
# height = float(input("Enter your height in meters: "))
# bmi = calculate(weight, height)
# category = category(bmi)
# print(f"Your BMI is {bmi:.2f}, which is {category}.")
# ----------------------------------------------------------------------------------------
# 19.second largest
# a=list(map(int,input("Enter the numbers:").split()))
# s=set(a)
# s=list(s)
# n=len(s)
# s.sort()
# if(n<=1):
#     print('No second largest')
# else:
#     print(s[1])
# ----------------------------------------------------------------------------------------
# 20.FizzBuzz
# for i in range(1,101):
#     if(i%3==0 and i%5==0):
#         print('FizzBuzz')
#     elif(i%3==0):
#         print('Fizz')
#     elif(i%5==0):
#         print('Buzz')
#     else:
#         print(i)