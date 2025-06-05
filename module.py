# lab 49

# import json
# import os

# LIBRARY_FILE = 'library_data. json'
# def load_library():
#     if not os.path. exists(LIBRARY_FILE):
#         return {}
#     try:


#       with open (LIBRARY_FILE, 'r') as file:
#         return json.load (file)
    
#     except Exception as e:
#       print (f"error loadding library data: {e}")
#       return{}



# def save_library(library):
#     try:
#          with open (LIBRARY_FILE, 'w') as file:
#             json.dump (library, file)
#     except Exception as e:
#         print (f"Error saving libraray data: {e}")


# def add_book(library, title, author, quantity):
#     if title in library:
#         print("book alreadyexists,updating the quantity.")
#         library[title] ['quantity'] += quantity
#     else:
#        library [title] = {'author' : author, 'quantity' : quantity, 'borrowed_by': None}
#        save_library (library)
#        print (f"book'{title} added successfully!")



# def view_book (library):
#    if not library:
#       print("the library is empty.")
#       return
#    for title, details in library. items():
#       status = f"Available ({details['quantity']})" if not details ['borrowed_by'] else f" Borrowed by {details['borrowed_by']}"
#       print(f"Title: {title},Author: {details['author']}, status:{status}")




# def borrow_book(library,title, borrower_name):
#     if title not in library:
#         print ("book not found in the library.")
#         return
#     if library[title]['quantity'] == 0:
#         print (f"All copies of {title}'are currently borrowed.")
#         return
#     if library [title] ['borrowed_by']:
#         print(f"The book '{title}'is currently borrowed by {library[title]['borrowed_by']}.")
#         return    
#         library [title]['quantity'] -= 1
#         library [title] ['borrowed_by'] = bprrpwer_name
#         save_library (library)
#         print(f"'{title}' has been borrowed by {borrower_name}.")



# def return_book (library , title):
#     if title not in library:
#         print ("Book not found in the libaray.")
#         return
#     if not library [title] ['borrowed_by']:
#         print (f" The book '{title}' was not borrowed.")

        
#         return
#         library [title] ['quantity'] +=1
#         borrower_name = library [title] ['borrowed_by']
#         library [title] ['borrowed_by'] = None
#         save_library (library)
#         print(f"{title}'{title}' has been returned by {borrower_name}.")


# def main ():
#     library = load_library ()
#     while True:
#         print ("\n library Management system")
#         print ("1. Add book")
#         print ("2. View book")
#         print ("3. borrow book")
#         print ("4. Return book")
#         print ("5. Exit")
#         choice = input ("Enter your choice:")
#         if choice == '1':
#             title = input ("enter the book title:")
#             author = input ("enter the book author:")
#             try:

#               quantity = int (input("enter the quantity of the book:"))      
#               add_book (library, title, author, quantity)
#             except ValueError :
#                 print ("Invalid input for quantity . please enter an integer .")   
#         elif choice =='2':
#             view_book (library)
#         elif choice =='3':
#             title = input ("Enter the book title:")
#             borrow_name =input ("enter your name :")
#             borrow_book (library, title, borrow_name)
            
#         elif choice =='4':
#             title = input ("enter the book title:")
#             return_book (library , title)
#         elif choice == '5':
#             print ("exiting the system. goodbye!")
#             break
#         else:
#             print("Invalid choice. please enter number between 1 and 5. ")  
#         if __name__=="__main__":  
#             main()                 

#  lab 48


# import os
# define the directoey path
# directory_path =' new_directory'

# create a new directory 
# os.makedirs (directory_path , exist_ok=True) #exist_ok ture avoides error ifdirectory already exists
# print(f"Directory '{directory_path}' creatrd.")







import os

#Define the current and new directory names 
current_name = 'name_directory'
new_name = 'renamed_directory'


# rename the directory
os. rename (current_name,new_name)
print(f"Directory renamed from'{current_name}' to ' {new_name}'.")



import shutil

#define the directory path to be deleted 
directory_path = 'renamed_directory'

#remove the directory and all its contents 

shutil . rmtree (directory_path)
print (f"directory '{directory_path} ' deleted'")


class BankAccount :
    def __init__ (self , account_number , holder_name,initial_balance=0):


      self .account_number = account_number
      self .holder_name = holder_name
      self .balance = initial_balance



    def deposit (self,amount):

        if amount > 0:
            self .balance += amount
            print(f"Deposited ₹{amount : .2f}.  New balance is ₹ {self .blance : .2f} .")
        else:
            print ("Deposit amount must be positive.")
    def withdraw (self, amount):
        if 0 < amount <= self .blance:
            print(f"withdrew ₹{amount:.2f}. New balance is ₹ {self.balance: .2f} .")
        
        else:              
         print ("Insufficient funds or invalid amount .")

         def get_balance(self):
            return self .balance


    def __str__(self):
        return (f"Account Number {self .account_number}\n"
        f"holder Name :{self .holder_name}\n"
        f"Balance: ₹{self .balance: .2f}")


    if __name__ == "__main__":


     account = BankAccount("12345678" , "Antima" , 1000)
 
    print(account)

    account .deposit (300)
    account .withdraw (400)
    account .withdraw(10000)

    # print (f" Final balance : ₹ { account .get_balance():2f}")



