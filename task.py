import random

print("Welcome to the coffe machine simulator! Let's start!\n")

ingredients = {'Water': 500, 'Milk': 300, 'Coffee': 150, 'Money': 0}
money = 0

def ask_input():
    choice = input("What's your choice? Type espresso/latte/cappuccino\n")
    return choice

def ask_coins(money):
    ask_pennies = int(input("How many pennies? "))
    ask_nickels = int(input("How many nickels? "))
    ask_dimes = int(input("How many dimes? "))
    ask_quarters = int(input("How many quarters? "))

    money += ask_pennies * 0.01 + ask_nickels * 0.05 + ask_dimes * 0.1 + ask_quarters * 0.25

    return money, ask_pennies, ask_nickels, ask_dimes, ask_quarters


def print_report(ingredients):
    print(f"Water: {ingredients['Water']}ml \n")
    print(f"Milk: {ingredients['Milk']}ml \n")
    print(f"Coffee: {ingredients['Coffee']}g\n")
    print(f"... you currently have ${ingredients['Money']}\n")

def check_ingredients(choice, ingredients):
    if choice == 'espresso' and ingredients['Water']>=50 and ingredients['Coffee']>=18 and ingredients['Money']>1.50:
        return True
    elif (choice == 'latte' and ingredients['Water'] >= 200 and ingredients['Milk'] >= 150 and ingredients['Coffee']>=24
          and ingredients['Money']>2.50):
        return True
    elif (choice == 'cappuccino' and ingredients['Water'] >= 250 and ingredients['Milk'] >= 100 and ingredients['Coffee']>=24
          and ingredients['Money']>3.50):
        return True
    else:
        return False

def insert_ingredients(ingredients):
    ingredients['Water']=int(input("Insert water."))
    ingredients['Milk']=int(input("Insert milk."))
    ingredients['Coffee']=int(input("Insert coffee."))

choice = ask_input()
money, pennies, nickels, dimes, quarters = ask_coins(money)
ingredients['Money'] = money
print(f"You currently have ${money}")

while choice != "off":
    if choice == 'espresso':
        print(f'CHOICE: {choice}\n')
        if check_ingredients(choice, ingredients):
            print(f'Drink prepared... here is your {choice}!\n')
            money-=1.50
            ingredients['Water']-=50
            ingredients['Coffee']-=18
        else:
            print("Not enough ingredients! Please contact the provider.\n")
            print_report(ingredients)
    elif choice == 'latte':
        print(f'CHOICE: {choice}\n')
        if check_ingredients(choice, ingredients):
            print(f'Drink prepared... here is your {choice}!\n')
            money-=2.50
            ingredients['Water']-=200
            ingredients['Coffee']-=24
            ingredients['Milk']-=150
        else:
            print("Not enough ingredients! Please contact the provider.\n")
            print_report(ingredients)
    elif choice == 'cappuccino':
        print(f'CHOICE: {choice}\n')
        if check_ingredients(choice, ingredients):
            print(f'Drink prepared... here is your {choice}!\n')
            money-=3.50
            ingredients['Water']-=250
            ingredients['Coffee']-=24
            ingredients['Milk']-=100
        else:
            print("Not enough ingredients! Please contact the provider.\n")
            print_report(ingredients)
    elif choice == 'report':
        print_report(ingredients)
    elif choice == 'insert':
        insert_ingredients(ingredients)
    elif choice == 'off':
        print("\nDeactivating machine . . .\n")
        break

    choice = ask_input()
    money, pennies, nickels, dimes, quarters = ask_coins(money)
    ingredients['Money'] = money
    print(f"You currently have ${money}")
