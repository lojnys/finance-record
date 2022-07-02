
import pyinputplus as pyip
import csv
from datetime import datetime

from requests import head
from data import *

path_to_csv = "C:\\Users\lojnj_oz39pq5\\OneDrive\\바탕 화면\\yushin\\github\\finance-record\\logs\\" 
# path_to_csv = "/c/Users/lojnj_oz39pq5/OneDrive/바탕 화면/yushin/github/finance-record/logs/"

header = [
    'Amount',
    'Category',
    'Date',
    'Where',
    'Total'
]

def found(name):

    accountlist_path = path_to_csv + "accountlist.txt"

    with open(accountlist_path, 'r', newline="") as f:                         # outputting all the names of accounts as a list
        account_list = f.readlines()

    return name in account_list                                    # checks if the given name is in the list, meaning if it exists already

def update(cad, name):

    if found(name):                                                # "if the account already exists"

        csv_file = path_to_csv + f"{name}.csv"

        with open(csv_file, 'r+', newline="") as file:

            prev_reader = [x for x in csv.reader(file)]
            # print(prev_reader)
            prev_total = float(prev_reader[len(prev_reader)-1][4])        # getting the previous total  /////// NOT WORKING ///// test: make an account and test it by adding/subtracting from beginning balance
            # print(prev_total)

            category = input("What was this for? (category) ")
            date = pyip.inputDate("Please provide the date (ex. 06/10/2022) ")
            where = input("Where did you use/optain money to/from? ")    

            data = [
                cad,
                category,
                date,
                where,
                prev_total + cad
            ]

            csv_writer = csv.writer(file)
            csv_writer.writerow(data)
        
        ending = "\nYou have successfully updated your account! \n"

    else:

        ending = f"\nYou do not have the following account: {name}\n"
    
    
    return print(ending)

def retrieve_transaction(name, filter):                                   # attempted to filter transactions by given month     //////// NOT WORKING/////////////////

    # with open(path_to_csv+f"{name}.csv", 'r') as file:
    #     csv_reader = csv.reader(file)

    if found(name) and not(filter == ""):

        with open(path_to_csv+f"{name}.csv", 'r') as file:
            csv_reader = csv.reader(file)

            date_category = Calender()
            filter_date = date_category.NametoNum(filter)
            # print(filter_date)

            filtered_list = [header] + [x for x in csv_reader if x[2][1] == str(filter_date)]

            print("\n")
            for row in filtered_list:
                print(", ".join(row))
            print("\n")

    elif found(name) and filter == "":

        with open(path_to_csv+f"{name}.csv", 'r') as file:
            csv_reader = csv.reader(file)

            print("\n")
            for row in csv_reader:
                print(", ".join(row))
                # print(row)
            print("\n")
    
    else:

         ending = f"\nYou do not have the following account: {name}\n"
         print(ending)

    return 0


def make_account(cad, name):

    csv_path = path_to_csv + f"{name}.csv"
    list_path = path_to_csv + "accountlist.txt"

    if not(found(name)):

        with open(csv_path, 'w', newline="") as file:                                                               # creating a nonexisting file

            csv_writer = csv.writer(file)
            csv_writer.writerow(header)
            csv_writer.writerow([cad, "None", datetime.now().strftime("%m/%d/%Y"), "None", cad])                # inputting beginning balance
        
        with open(list_path, 'a', newline="") as f:                                                                 # writing the name of the account on the account list to keep track
            f.write(name)

        
        ending = "\nYou have successfully made an account\n"

    else:
        ending = f"\nYou already have an account named {name}\n"

    return print(ending)

def main():

    accountlist_path = path_to_csv + "accountlist.txt"

    with open(accountlist_path, 'r', newline="") as f:                         # outputting all the names of accounts as a list
        account_list = f.readlines()

        repeat = True

        while repeat:

            option = pyip.inputMenu(['Update', 'Transactions', 'Make an account'], numbered=True, blank=False)

            if option == 'Update':

                for line in account_list:
                    print(line)

                account_name = pyip.inputStr("\nWhat is the account name? ", blank=False)

                amount = pyip.inputNum("Provide the amount: ", default='0')

                update(amount, account_name)

                repeat = True if input("Would you like make another action? (y/n) ") == 'y' else False
            
            elif option == "Transactions":

                for line in account_list:
                    print(line)

                account_name = pyip.inputStr("\nWhat is the account name? ", blank=False)
                date_filter = pyip.inputStr("Do you have a specific month that you want to look at? (enter if none) ex. Jun for June: ", blank=True)

                retrieve_transaction(account_name, date_filter)

                repeat = True if input("Would you like make another action? (y/n) ") == 'y' else False

            elif option == 'Make an account':


                name = input('\nPlease provide the name of your account ')
                beginning_balance = pyip.inputNum("What is your beginning balance? ")

                make_account(beginning_balance, name)

                repeat = True if input("Would you like make another action? (y/n) ") == 'y' else False
    return 0




if __name__=="__main__":
    main()