#!/usr/bin/env python
# coding: utf-8

# In[3]:


import shutil
import random
import string
from datetime import datetime
import time

# To get terminal size and print in center of screen
columns = shutil.get_terminal_size().columns

class Library():
    def __init__(self):
        self.Login_check = False
        print("Admin login".center(columns))
        print()
        print("Borrower login".center(columns))
        print("\n\n")
        print("Are you Admin or Borrower? Press 1 for Admin login and Press 2 for Borrower login\n".center(columns))
        try:
            login_Response = int(input())    
        
            if login_Response == 1:
                print("\n\n")
                self.Admin_login()         


            elif login_Response == 2:
                    print("\n\n")
                    self.Borrower_login()

            else:
                print("\n\nWrong Input")
                
        except:
            print("Invalid input")
            
    
    Admins = {'admin':'admin'}
    
    def Admin_login(self):
        self.username = input("Enter username: ")
        self.password = input("Enter password: ")
        if self.username in self.Admins:
            if self.password == self.Admins[self.username]:
                check = True
                while check == True:
                    print("\n\nWelcome {}, Manage your library.\n\nHere are some functions you can perform...Enter the corresponding number ".format(self.username).center(columns))
                    print("\n1. Add Admin\n2. Add a Borrower\n3. Add Books in Library\n4. Edit Book Details")
                    print("5. Delete a Book\n6. View all Borrowers and their borrowing history\n7. Book issue\n8. Accept Book return\n9. Exit the program")
                    self.Response = int(input())


                    if self.Response == 1:
                        self.add_admin()

                    elif self.Response == 2:
                        self.add_borrower()
                        print("\n",self.Borrowers.keys())

                    elif self.Response == 3:
                        self.add_books()

                    elif self.Response == 4:
                        self.edit_books()

                    elif self.Response == 5:
                        self.delete_book()

                    elif self.Response == 6:
                        self.list_all_borrowers()

                    elif self.Response == 7:
                        self.book_issue()

                    elif self.Response == 8:
                        self.book_return()
                        
                    elif self.Response == 9:
                        print("Program has been closed...Hope to see you again")
                        check = False
                        
                    else:
                        print("Wrong input")
                    
            else:
                print("Password is wrong...Please try again")
        else:
            print("You are not admin of this library...Please contact Admin to get access rights")
            
            
            
            
    
    Borrowers = {"student":"student"}
    
    def Borrower_login(self):
        self.B_username = input("Enter username: ")
        self.B_password = input("Enter password: ")
        if self.B_username in self.Borrowers:
            if self.B_password == self.Borrowers[self.B_username]:
                a_check = True
                while a_check == True:
                    print("\n\nWelcome {} You can check below deatails of your account. Enter the corresponding number".format(self.B_username).center(columns))
                    print("\n1. View the details of currently borrowed book\n2. View book details of each borrowed books\n3. View borrowing history\n4. Exit the program\n")
                    self.B_resp = int(input())

                    if self.B_resp == 1:
                        self.view_currently_borrowed()

                    elif self.B_resp == 2:
                        self.view_book_details()

                    elif self.B_resp == 3:
                        self.view_borrowing_history()
                        
                    elif self.B_resp == 4:
                        time.sleep(0.7)
                        print("Program has been closed...Hope to see you again")
                        a_check = False
                        
                    else:
                        print("Wrong input")
                
                
        else:
            time.sleep(0.5)
            print("\nyou are not the member of library\n\nDo you want to register yourself\nPress Y/y for Yes\n Press any key for No")
            time.sleep(0.8)
            resp = input()
            if resp.lower() == "y":
                self.add_borrower()
            else:
                print("Please visit library again ")



    def add_admin(self):
        self.A_username = input("Enter username: ")
        if self.A_username not in self.Admins:
            self.A_password = input("Enter password: ")
            print("\nYou have added a new admin to library")
            self.Admins[self.A_username] = self.A_password
            time.sleep(1)
            print("\nHere is the new admin list:\n\n",self.Admins.keys())
            time.sleep(1)
        else:
            print("Username already exist, Choose another Username")
    
    Student_data = {}
            
    def add_borrower(self):
        self.Full_Name = input("Enter Full Name: ")
        self.DOB = input("Enter Date of Birth: ")
        self.Contact_Number = input("Enter Contact Number: ")
        self.Email_Address = input("Enter Email Address: ")
        self.Password = input("Enter strong Password: ")
        if self.Email_Address not in self.Borrowers:
            time.sleep(1)
            print("\nNow you have become the member of library")
            time.sleep(1)
            self.Borrowers[self.Email_Address] = self.Password
            self.Student_data[self.Email_Address] = {}
            self.Student_data[self.Email_Address]['Name'] = self.Full_Name
            self.Student_data[self.Email_Address]['DOB'] = self.DOB
            self.Student_data[self.Email_Address]['Contact_Number'] = self.Contact_Number

        else:
            print("Email Id is already registered...Please login")
            time.sleep(1)
            
            
    list_of_books = {'ABC417':{'Book Title':'Wings and Fire','Author Name':'A. P. J. Abdul Kalam','Total Pages':228,'copies':5,'ISBN':9788173711466,'Published Year':1999}}        
            
    def add_books(self):
        self.Book_Title = input("Enter the title of book: ")
        list_of_books_2 = {}
        for key in self.list_of_books:
            if self.Book_Title != self.list_of_books[key]['Book Title']:
                self.Author_Name = input("Enter Author Name: ")
                self.Total_Pages = input("Enter Total Pages: ")
                self.number_of_copies = input("Enter number of copies: ")
                self.ISBN = input("Enter ISBN No: ")
                self.Published_Year = input("Enter Published Year: ")
                temp_dict = {}
                temp_dict['Book Title'] = self.Book_Title
                temp_dict['Author Name'] = self.Author_Name
                temp_dict['Total Pages'] = self.Total_Pages
                temp_dict['copies'] = self.number_of_copies
                temp_dict['ISBN'] = self.ISBN
                temp_dict['Published Year'] = self.Published_Year

                result = Library.generate_book_id()
                list_of_books_2[result] = temp_dict

            else:
                print("Book is already available in library with book id {}".format(key))
                time.sleep(1)

        for key2,value in list_of_books_2.items():
            self.list_of_books[key2] = value
            
        time.sleep(1)

        print("\nBook has been added to library...Checkout current list of book\n\n",self.list_of_books)
        time.sleep(1)
        
        
    def edit_books(self):
        self.bookk_id = input("Enter book Id of book for you want to edit the details: ")
        try:
            self.list_of_books[self.bookk_id]['Book Title'] = input("Enter Book Title: ")
            self.list_of_books[self.bookk_id]['Author Name'] = input("Enter Author Name: ")
            self.list_of_books[self.bookk_id]['Total Pages'] = input("Enter Total Pages: ")
            self.list_of_books[self.bookk_id]['copies'] = input("Enter number of copies: ")
            self.list_of_books[self.bookk_id]['ISBN'] = input("Enter ISBN No: ")
            self.list_of_books[self.bookk_id]['Published Year'] = input("Enter Published Year: ")
            time.sleep(1)
            print("The details of has been changed...checkout current list ofbooks\n\n",self.list_of_books)
            time.sleep(1)
        except:
            time.sleep(1)
            print("There is no book in library with this book id")
            time.sleep(1)
            
            
    def delete_book(self):
        self.book_id = input("Enter book Id which you want to delete: ")
        if self.book_id in self.list_of_books:
            del self.list_of_books[self.book_id]
            time.sleep(1)
            print("Book has been deleted...checkout current list of books\n\n",self.list_of_books)
            time.sleep(1)

        else:
            time.sleep(1)
            print("Book is not available in library")
            time.sleep(1)
            
            
    borrowing_history = []
            
    def list_all_borrowers(self):
        for o in self.Student_data:
            print("{}\n\n".format(o))
            print("Name:  {}     DOB:  {}     Contact_Number:  {}\n".format(self.Student_data[o]["Name"],self.Student_data[o]["DOB"],self.Student_data[o]["Contact_Number"]))
            print("Book borrowed by student is: ")
            time.sleep(1)
            for r in self.borrowing_history:
                if r["Email_Id"] == o:
                    print(r["book_id"])

            print("-"*80)
            time.sleep(1)
            
    Current_borrowing_books_list = []
            
            
    def book_issue(self):
        self.email_address = input("Enter the email address of borrower: ")
        if self.email_address in self.Borrowers:
            self.book_id = input("Enter book id which is to be issued: ")
            if self.book_id in self.list_of_books and self.list_of_books[self.book_id]['copies'] >= 0:
                for i in self.Current_borrowing_books_list:
                    if i[book_id]['Email'] == self.email_address:
                        print("You have already borrowed the book")
                        time.sleep(1)
                        break
                else:
                    print("book has been issued to {}".format(self.email_address))
                    issue_now = datetime.now()
                    issue_now_str = issue_now.strftime("%d/%m/%Y %H:%M:%S")
                    self.Current_borrowing_books[self.book_id] = {}
                    self.Current_borrowing_books[self.book_id]["Email"] = self.email_address
                    self.Current_borrowing_books[self.book_id]["Time of issue"] = issue_now_str
                    self.Current_borrowing_books_list.append(self.Current_borrowing_books)
                    d = dict([("book_id",self.book_id),("Email_Id",self.email_address),("Status","Issued")])
                    self.borrowing_history.append(d)
                    self.Current_borrowing_books = {}
                    self.list_of_books[self.book_id]['copies'] -= 1
                    time.sleep(1)
                    print("You can checkout the books currently borrowed by students below:\n\n",self.Current_borrowing_books_list)
                    
            else:
                time.sleep(1)
                print("Book is not available in library")
                time.sleep(1)

        else:
            time.sleep(1)
            print("\n\nYou are not the member of the library...Please sign up for membership")
            time.sleep(1)
            
            
    def book_return(self):
        self.boook_id = input("Enter the book id you want to return: ")
        self.email_id = input("Enter the email id of borrower: ")
        try:
            for p in self.Current_borrowing_books_list:
                if p[self.boook_id]['Email'] == self.email_id:
                    return_now = datetime.now()
                    x = p[self.boook_id]["Time of issue"]
                    issue_then = datetime.strptime(x,"%d/%m/%Y %H:%M:%S")
                    print("issue date: ",issue_then)
                    print("return date: ",return_now)
                    z = return_now - issue_then
                    z_int = z.days
                    time.sleep(0.7)
                    if z_int > 13:
                        print("You kept book for more than 14 days...So, 100 rs fine will be charged")
                    else:
                        print("You kept book for less than 14 days...No fine will be charged")
                    del p[self.boook_id]
                    time.sleep(0.7)
                    print("book returned successfully...You can checkout the currently borrowed books by students below:\n\n",self.Current_borrowing_books_list)
                    break

            else:
                print("You haven't borrowed that book")
                time.sleep(1)

        except:
            print("This book hasn't been issued")
            time.sleep(1)
            
            
    def view_currently_borrowed(self):
        set_flag = False
        for p in self.Current_borrowing_books_list:
            for q in p:
                if p[q]['Email'] == self.B_username:
                    time_now = datetime.now()
                    x1 = p[q]["Time of issue"]
                    time_then = datetime.strptime(x1,"%d/%m/%Y %H:%M:%S")
                    time_left = time_now - time_then
                    time_left_int = time_left.days
                    time.sleep(1)
                    print("book id:  {}    Time left:  {} day".format(q,14 - time_left_int))
                    set_flag = True
        
        if set_flag == False:
            time.sleep(1)
            print("You don't have any books pending")
            time.sleep(1)
            
            
    def view_book_details(self):
        for i in self.borrowing_history:
            if i["Email_Id"] == self.B_username:
                time.sleep(0.8)
                print("Book details of borrowed book id {}:\n\n".format(i["book_id"]))
                print(library.list_of_books[i["book_id"]])
                print()
                time.sleep(0.8)

            else:
                time.sleep(1)
                print("You haven't borrowed any book")
        print("-"*100)
        
        
    def view_borrowing_history(self):
        l = []
        for f in self.borrowing_history:
            if f["Email_Id"] == self.B_username:
                l.append(f["book_id"])
                
        if l:
            time.sleep(1)
            print("List of books borrowed is {}".format(l))
            time.sleep(1)
            
        else:
            time.sleep(1)
            print("You haven't borrowed any book till now")
            time.sleep(1)
            
        
        
    @staticmethod
    def generate_book_id():
        str1 = "".join(random.choices(string.ascii_letters,k=3))
        str2 = "".join(random.choices(string.digits,k=3))
        str3 = str1 + str2
        return str3

