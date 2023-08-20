# expenseDict = {}
# moneySpent = input("Enter the money spent or write quit to ").lower().strip()
# while moneySpent != "quit"

import time

def add_expense():
    expenseList = []
    moneySpent = input("Write the amount or write quit to quit: ").lower().strip()
    while moneySpent != "quit":
        # moneySpent = int(moneySpent)
        item = input("Write the name of the item: ").lower().strip()
        expenseList.append(moneySpent)
        with open("bin/expenses.txt", "a") as f:
            record_time = time.strftime("%H:%M")
            f.write(f"{record_time} : {item} - {moneySpent} \n")
        with open("bin/_sum_expenses.txt", "a") as f:
            f.write(f"{moneySpent}\n")

        moneySpent = input("Write the amount or write quit to quit: ").lower().strip()
    return expenseList

def retrive_expense():
    with open("bin/expenses.txt", "r") as f:
        print(f"\n{f.read()}")

def sum_expense():
    #todo: complete this fuction
    try:
        with open("bin/_sum_expenses.txt", "r") as f:
            expenses = f.readlines()
            sum = 0
            for expense in expenses:
                expense = int(expense)
                sum += expense
            print(f"Your total expense is {sum}")
    except FileNotFoundError:
        print("No Expenses Found!")
    else:
        if sum==0:
            print("Your total expense is 0")

while True:
    try:
        options = int(input("\nWrite 1 to add a new expense \nWrite 2 to retrieve the expenses \nWrite 3 to sum total all the expenses"))
    except ValueError:
        print("Please write a correct number!")

    if options == 1:
        add_expense()
    elif options == 2:
        retrive_expense()
    elif options == 3:
        sum_expense()