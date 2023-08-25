from Menu import menu
from coffee_makers import coffee_makers
from moeny_machine import MoneyMachine
from time import sleep



def welcome():
    print('''\033[33m
            
         
          WELCOME TO THE COFFEE MACHINE!
          

          ------ MENU ------ 
          Espresso ($1.50)
          Latte ($2.50)
          Cappuccino ($3.00)
          ------------------

          PS: Type "report" at any moment
          to check our resources available.
          Type "off" to log out from the machine.\033[m
        ''')

item_menu = menu()
coffee_machine = coffee_makers()
money_machine = MoneyMachine()
is_on = True

while is_on:
    welcome()
    options = item_menu.get_items()
    user_choice = str(input(f'What would you like?\nOptions ({options}): ')).strip().lower()
    if user_choice == 'off':
        print('\033[31m<<THE END>>\033[m')
        is_on = False
    elif user_choice == 'report':
        coffee_machine.report()  # Changed to 'coffee_machine'
        money_machine.report()  # Changed to 'money_machine'
    elif item_menu.find_drink(user_choice) is None:
        print('\033[31mError. Please choose an available option.\033[m')
    else:
        beverage = item_menu.find_drink(user_choice)  # Encapsulates the result
        sufficient_resources = coffee_machine.is_resource_sufficient(beverage)  # TrueFalse result
        sufficient_money = money_machine.make_payment(beverage.cost)
        if sufficient_resources and sufficient_money:
            print('Thank you! Allow us to make your beverage now...')
            coffee_machine.make_coffee(beverage)  # Changed to 'coffee_machine'
            sleep(5)

