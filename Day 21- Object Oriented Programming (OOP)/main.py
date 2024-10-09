#Object Oriented Programming for Coffee Machine

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True
while is_on:
    choose_coffee = input("What would you like? (espresso/latte/cappuccino): ")
    if choose_coffee == 'off':
        is_on = False
    elif choose_coffee == 'report':
        money_machine.report()
        coffee_maker.report()
    else:
        drink = (menu.find_drink(choose_coffee))
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

        