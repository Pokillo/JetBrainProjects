# Raw example of how CoffeeMachine would work in life.

class CoffeeMachine:

    def __init__(self, water, milk, coffee, cups, money):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cups = cups
        self.money = money

    def main(self, act):
        print()
        if act == "buy":
            type_coffee = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
            if type_coffee == "back":
                return
            elif int(type_coffee) == 1:
                self.buy_espresso()
            elif int(type_coffee) == 2:
                self.buy_latte()
            elif int(type_coffee) == 3:
                self.buy_cappuccino()

        elif act == "fill":
            self.water_filler()
            self.milk_filler()
            self.coffee_filler()
            self.cups_filler()
        elif act == "take":
            self.money_taker()
        elif act == "remaining":
            self.show_container()
        elif act == "exit":
            exit()

    def show_container(self):
        print('''
    The coffee machine has:
    {} of water
    {} of milk
    {} of coffee beans
    {} of disposable cups
    {} of money
    '''.format(self.water, self.milk, self.coffee, self.cups, self.money))

    def water_filler(self):
        add_water = int(input("Write how many ml of water do you want to add:"))
        self.water = self.water + add_water
        return self.water

    def milk_filler(self):
        add_milk = int(input("Write how many ml of milk do you want to add:"))
        self.milk = self.milk + add_milk
        return self.milk

    def coffee_filler(self):
        add_coffee = int(input("Write how many grams of coffee beans do you want to add:"))
        self.coffee = self.coffee + add_coffee
        return self.coffee

    def cups_filler(self):
        add_cups = int(input("Write how many disposable cups of coffee do you want to add:"))
        self.cups = self.cups + add_cups
        return self.cups

    def money_taker(self):
        print("I gave you ${}".format(self.money))
        self.money = 0
        return

    def buy_espresso(self):
        if self.water >= 250 and self.cups >= 1 and self.coffee >= 16:
            print("I have enough resources, making you a coffee!")
        elif self.water < 250:
            print("Sorry, not enough water!")
            return
        elif self.cups < 1:
            print("Sorry, not enough cups!")
            return
        elif self.coffee < 16:
            print("Sorry, not enough coffee!")
            return
        self.water -= 250
        self.cups -= 1
        self.coffee -= 16
        self.money += 4
        return self.water, self.coffee, self.money, self.cups

    def buy_latte(self):
        if self.water >= 350 and self.cups >= 1 and self.coffee >= 20 and self.milk >= 75:
            print("I have enough resources, making you a coffee!")
        elif self.water < 250:
            print("Sorry, not enough water!")
            return
        elif self.cups < 1:
            print("Sorry, not enough cups!")
            return
        elif self.milk < 75:
            print("Sorry, not enough milk!")
            return
        elif self.coffee < 16:
            print("Sorry, not enough coffee!")
            return

        self.water -= 350
        self.milk -= 75
        self.cups -= 1
        self.coffee -= 20
        self.money += 7
        return self.water, self.coffee, self.money, self.cups, self.milk

    def buy_cappuccino(self):
        if self.water >= 200 and self.cups >= 1 and self.coffee >= 12 and self.milk >= 100:
            print("I have enough resources, making you a coffee!")
        elif self.water < 200:
            print("Sorry, not enough water!")
            return
        elif self.cups < 1:
            print("Sorry, not enough cups!")
            return
        elif self.milk < 100:
            print("Sorry, not enough milk!")
            return
        elif self.coffee < 12:
            print("Sorry, not enough coffee!")
            return
        self.water -= 200
        self.milk -= 100
        self.cups -= 1
        self.coffee -= 12
        self.money += 6
        return self.water, self.coffee, self.money, self.cups, self.milk


coffee1 = CoffeeMachine(400, 540, 120, 9, 550)
while True:
    action = input("Write action (buy, fill, take, remaining, exit):")
    coffee1.main(action)
