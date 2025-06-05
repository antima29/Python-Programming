# lab 41


# def add (x,y):
#     return x + y

# def subtract (x,y):
#     return x-y

# def multiply (x,y):
#     return x*y

# def divide (x,y):
#     return x / y

# import hello


# x = 10
# y = 5

# print ("Addition" ,hello.add( x, y) )
# print ("subtraction:" , hello .subtract(x, y))
# print ("multiplication:" , hello .multiply ( x,y))
# print  ("dividion:" , hello .divide(x,y))


#  lab 42


# import math

# # Square root
# print ("Square root of 25:" , math.sqrt(25))
# print ("factorial of 5:" , math.factorial(5))
# print ("Value of pi:", math .pi)
# print ("Cosine of 45 degrees:" , math .cos(math. radians(45)))


# lab 47

# file = open ('example.txt' , 'w')
# file.write ("hello, antima \n i am from up.")
# file . close

# file = open('example.txt', 'r')
# content = file. read()
# print ("full content:")
# print(content)

# file = open ('example.txt' ,'r')
# print ("reading all line at once:")
# lines = file .readlines()
# for line in lines:
#     print(line, end='')


# file = open('example.txt','a')
# print(file.tell())
# file.write("\nAppending a new line to the file.")
# print(file.tell())
# file.close()

# lab 21
# x , y = map(int , input("Enter two number separated by space:").split())
# print(f"sum of {x} and {y} is: {x + y}")


# lab 22

# temperature = int(input("Enter temperature"))
# if temperature <0:
#     print("it,s freezing!")

# lab 23

# num1 = int (input("Enter the first integer:"))
# num2 = int (input("Enter the second integer:"))


# sum_of_numbers = num1+ num2

# if 10 <= sum_of_numbers <= 20:
#     print(15)
# else:
#     print(0)

# lab 24

# bool1 = True
# bool2 = False

# if bool1 and bool2:
#     print("both condition are true.")
# else:

#     print("At least one condition is False.")


#  lab 25

# temp = input ("Input the temperature you like to  convert? (e.g, 45F , 102c etc.):")
# degree = int(temp[: -1])

# i_convention = temp[-1]

# if i_convention. upper() == "C":
#     result = int(round((9* degree) / 5+ 32))
#     o_convention ="Fahrenheit" 

# elif i_convention.upper () == "F":
#     result = int(round((degree -32)* 5 / 9))
#     o_convention = "Celsius"

# else:
#     print("Input proper convention.")
    # quit()

# print ("The temperature in", o_convention, "is" , result, "degress.")       

# lab 26:
# month_name = input ("Enter the month name:"). lower() 
# if month_name == "january" or month_name == "march" or month_name == "may" or \
#    month_name =="july" or month_name =="august" or month_name == "october" or month_name =="december":
#     days=31
# elif month_name == "april" or month_name =="june" or month_name == "september" or month_name =="novermber":
#     days = 30
# elif month_name == "febuary":
#     days= 28
# else:
#     days = "Invalid month name" 




# lab 27

# word = "Antima jaiswal"

# for letter in word:
#     print(letter)


# lab 28

# counter = 1

# while counter <= 5:
#     print(counter)
#     counter += 1

# lab 30

# start_num = int(input("Enter the starting number:"))
# end_num = int(input("Enter the ending number:"))
# a,b =0,1

# fibonacci_series = []

# while a <= end_num:
#     if a >= start_num:
#         fibonacci_series.append(a)
#         a,b = b,a +b
        
# if fibonacci_series:
#     print(f"fibonacciseries between {start_num} and {end_num} is :")  
#     print (fibonacci_series)
# else:
#     print (f"No fibonacci number found between {start_num} and {end_num}")
             

# number = int(input("Enter a number to create its  multication table:"))
# print(f"Multication table for {number}:")

# for i in range (1, 11):
#     result = number *i
#     print(f"{number}x {i} = {result}")


# class BankAccount:
#     def __init__(self ,account_number, holder_name,intial_balance=0):
#         self.__account_number = account_number
#         self.__holder_nume = holder_name
#         self. __balance = intial_balance

#     def deposit (self , amount):
#         if amount > 0:
#             self__balance +=amount
#             print(f"Deposited ₹")   


# from abc import ABC, abstractmethod

# class BillingRecord(ABC):
#     @abstractmethod
#     def get_bill(self):
#         pass


#     def update_bill(self , amount):

#         pass

# class PatientBilling(BillingRecord):

#     def __init__(self , patient_id , patient_name , billing_amount =0):    

#         self. patient_id = patient_id
#         self. patient_name = patient_name
#         self. billing_amount = billing_amount

#     def get_bill(self):
#         return {
#             'Patient Id' : self. patient_id,
#             'Patient Name': self.patient_name,
#             'billing Amount' : f"₹{self. billing_amount:.2f}"
#         }   
#     def update_bill(self, amount):
#         if amount > 0:
#             self . billing_amount += amount 
#             print(f"Billing amount update by ₹{amount:.2f}. New amount is ₹{self.billing_amount:.2f}.")
#         else:
#             print ("Amount to updater must be positive.")

# if __name__  == "__main__":

#     patient_bill = PatientBilling(
#             patient_id="P001",
#             patient_name= "Antima Jaiswal",    
#             billing_amount=150.00
#          )


#     print("Initial Bill Details:")
#     print(patient_bill.get_bill())


#     patient_bill.update_bill(50.00)

#     print("\nUpdated Bill Details:")
#     print(patient_bill.get_bill())     

# lab 54

# class Person:

#     def __init__(self , name):

#      self .name = name
#     def greet (self):

#         return f"Hello, I,m{self .name}" 

# class Employee:
#     def __init__(self , employee_id):

#      self .employee_id = employee_id

#     def get_employee_id(self):

#       return self .employee_id

# class Manager(Person, Employee):


#     def __init__(self , name, employee_id):

#         Person. __init__(self , name)
#         Employee. __init__(self, employee_id)



# if __name__ == "__main__":  

#     manager = Manager ("Antima Jaiswal" , "E12345")

#     print (manager .greet())

#     print (f"Employee ID : {manager .get_employee_id()}")


# lab 54 c

# class Person:
#     def __init__(self , name , age):

#         self .name = name
#         self .age = age

#     def display_personal_details(self):
#         return f"Name:{self .name} , Age: {self .age}"

# class Employess(Person):

#     def __init__(self , name , age , employess_id , salary):


#         super().__init__(name, age) 
#         self .employess_id =employess_id
#         self .salary = salary

#     def display_employess_details(self):
#         personal_details = self .display_personal_details()
#         return f"{personal_details}, Employess ID: {self.employess_id}, Salary: ₹{self.salary:.2f}"



# class Manager(Employess):

#     def __init__(self, name ,age, employess_id , salary, departement , team_size):


#         super(). __init__(name , age , employess_id ,salary)
#         self .department = departement
#         self .team_size = team_size

#     def display_manager_details(self):



#         employess_details = self .display_employess_details()


#         return f"{employess_details} , Department: {self .department} , Team Size: {self .team_size}"      

# if __name__ == "__main__":

#     manager = Manager ("Antima Jaiswal" , 20, "M1046" , 95000,"sales", 10)
#     print ("Manager Details:")
#     print(manager .display_manager_details())  



# lab55 A

# class Printer:
#     def print_messge(self , message, times=1):
#         for _ in range (times):
#             print(message)

# if __name__ == "__main__":
#     printer = Printer()

#     printer .print_messge ("Hello")
#     printer .print_messge("Hello" , 3)


# lab 55B

# class Animal:
#     def speak (self):
#         return "Animal speaks"
# class Dog (Animal):
#     def speak (self):
#         return "Woof!"


# class Cat (Animal):
#     def speak(self):
#         return "Meow!"


# def make_animal_speak(animal):
#         print (animal .speak())

# if __name__ == "__main__":
#     dog = Dog ()
#     cat = Cat ()

#     make_animal_speak(dog)
#     make_animal_speak (cat)                  

        
# class Bird:
#     def fly(self):
#         return "Flying high"

# class Airplane:
#     def fly(self):
#         return "Flying through the skies"

# def let_it_fly(entity):
#     print(entity.fly())

# if __name__ == "__main__":
#     bird = Bird()
#     airplane = Airplane()

#     let_it_fly(bird)
#     let_it_fly(airplane)  
# 
import mysql.connector
conn=mysql .connector.connect(
    host='localhost',
    user='root',
    password='@AIPA123',
    database='studb'
)

if conn .is_connected():
    print("connected to database")
    
    cursor=conn.cursor()

    cursor.execute("create database AI_ALD")
    print("Database created")

    cursor.close()
    conn.close()


                           
cursor.execute ("studb")

# insert = 'Insert into ai_std(name,phone_no,trade) values (%s,%s,%s,)'
# data = [('Shailesh, 7510022289, AI_traniner'),('Antima',987653210,'EM'),('Ankita',9936681102,'COPA')]

# cursor.execmany(insert,data)
# conn.comit()

# cursor.close()
# conn.close()
