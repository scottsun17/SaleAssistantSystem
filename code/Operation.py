import json
import os
import random
import sys
import time

import pandas as pd
import requests
from prettytable import PrettyTable


from Pokemon import Pokemon
from PokemonInventory import PokemonInventory


def get_pokemon_index():
    response = requests.get("https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/pokedex.json")
    pokemon_index = json.loads(response.text)
    pokemon_index_df = pd.DataFrame.from_records(pokemon_index)
    pokemon_index_df.set_index('id', inplace=True)

    # this part update the name column to only includes english names
    names = pokemon_index_df['name']
    names_df = pd.DataFrame(names.values.tolist(), index=names.index)
    pokemon_index_df = pokemon_index_df.drop('name', axis=1)
    pokemon_index_df['name'] = names_df['english']

    # covert types into two columns. if no second type, store as NaN
    types = pokemon_index_df['type']
    types_df = pd.DataFrame(types.values.tolist(), columns=['type1', 'type2'], index=types.index)
    pokemon_index_df = pokemon_index_df.drop('type', axis=1)
    pokemon_index_df['type1'], pokemon_index_df['type2'] = types_df['type1'], types_df['type2']

    # covert base into six columns
    base = pokemon_index_df['base']
    base_df = pd.DataFrame(base.values.tolist(),
                           columns=['HP', 'Attack', 'Defense', 'Sp. Attack', 'Sp. Defense', 'Speed'], index=base.index)
    pokemon_index_df = pokemon_index_df.drop('base', axis=1)
    pokemon_index_df['HP'] = base_df['HP']
    pokemon_index_df['Attack'] = base_df['Attack']
    pokemon_index_df['Defense'] = base_df['Defense']
    pokemon_index_df['Sp_Attack'] = base_df['Sp. Attack']
    pokemon_index_df['Sp_Defense'] = base_df['Sp. Defense']
    pokemon_index_df['Speed'] = base_df['Speed']

    return pokemon_index_df


# return pokemon info as DataFrame series
def get_pokemon_info(pokemon_index_df, pokemon_index):
    return pokemon_index_df.loc[pokemon_index]


def input_price():
    while True:
        try:
            purchase_price = float(input("Input Purchase Price: "))
            sale_price = float(input("Input Sale Price: "))
            if sale_price < purchase_price:
                print("Cannot purchase Pokemon at a price higher than its' sale price")
            else:
                return "{:.2f}".format(purchase_price), "{:.2f}".format(sale_price)
        except ValueError:
            print("Invalid price input. Please try again.")


def input_sale_price(purchase_price):
    while True:
        try:
            sale_price = float(input("Input actual Sale Price: "))
            if sale_price <= purchase_price:
                print("Cannot sell a Pokemon at a price less than its' purchase price")
            else:
                return sale_price
        except ValueError:
            print("Invalid price input. Please try again.")


# function to validate level input
def input_level():
    while True:
        try:
            level = int(input("Input purchasing Pokemon's Level (1 ~ 100)"))
            if level > 100 or level < 1:
                print("Invalid Pokemon level. Please make sure the level is correct")
            else:
                return level
        except ValueError:
            print("Invalid level input. Please try again.")


# function to validate age input
def input_age():
    while True:
        try:
            age = int(input("Input purchasing Pokemon's age (1 ~ 100)"))
            if age > 100 or age < 1:
                print("Invalid Pokemon age. Please make sure the age is correct")
            else:
                return age
        except ValueError:
            print("Invalid age input. Please try again.")


# purchase pokemon operation
def purchase_pokemon(pokemon_index_df, sale_record):
    poke_index = get_poke_index()
    print("Checking Pokemon Information...\n\n")

    for item in sale_record:
        if item['poke_index'] == poke_index:
            print("You cannot purchase a pokemon already exist in the inventory.")
            return sale_record

    pokemon = get_pokemon_info(pokemon_index_df, poke_index)
    print_pokemon_info(pokemon)
    print("\n")
    pokemon_inventory = PokemonInventory(poke_index)
    pokemon_inventory.purchase_price, pokemon_inventory.sale_price = input_price()
    pokemon_inventory.level = input_level()
    pokemon_inventory.age = input_age()
    # Sale Flag is defaulted to false - pokemon purchased not sold yet
    sale_record.append(pokemon_inventory.__dict__)
    return sale_record


# pokemon generator - generate a random pokemon from the pokemon index
def generate_pokemon(pokemon_index):
    index = random.randint(0, 808)
    # print(index)
    pokemon = Pokemon()
    pokemon.__dict__ = pokemon_index[index]
    return pokemon


# print detail Pokemon information
def print_pokemon_info(pokemon):
    # print("Pokemon ID: ", pokemon.index)
    print("Pokemon Name: ", pokemon['name'])
    print("Pokemon Type: ", pokemon.type1)
    if pokemon.type2 is not None:
        print("Pokemon Second Type: ", pokemon.type2)
    print("Pokemon Bases: ")
    print("\tHP: ", pokemon.HP)
    print("\tAttack: ", pokemon.Attack)
    print("\tDefense: ", pokemon.Defense)
    print("\tSpecial Attack: ", pokemon.Sp_Attack)
    print("\tSpecial Defense: ", pokemon.Sp_Defense)
    print("\tSpeed: ", pokemon.Speed)


# get pokemon index input
def get_poke_index():
    while True:
        try:
            pokeIndex = int(input("Please input the pokemon Index: 1 ~ 809: "))
            if 1 <= pokeIndex <= 809:
                return pokeIndex
            else:
                print("Invalid PokeIndex, please try again!")
        except ValueError:
            print("Invalid PokeIndex, please try again!")


# display pokemon inventory
def display_pokemon_inventory(sale_record):
    inventory = []
    for item in sale_record:
        if item['sale_flag'] is False:
            inventory.append(item)

    inventory_table = PrettyTable()
    inventory_table.field_names = ["Inventory ID",
                                   "Pokemon Index", "Pokemon Level", "Pokemon Age", "Purchase Price", "Sale Price"]
    for item in inventory:
        inventory_table.add_row([inventory.index(item), item['poke_index'],
                                 item['level'], item['age'], item['purchase_price'], item['sale_price']])
    print(inventory_table)
    return inventory


def get_inventory_id(sale_record):
    count = len(sale_record) - 1
    while True:
        try:
            inventory_id = int(input("Please input the Inventory ID of selling pokemon: "))
            if inventory_id > count or inventory_id < 0:
                print("Invalid inventory ID. Please make sure the ID is correct")
            else:
                return inventory_id
        except ValueError:
            print("Invalid ID input. Please try again.")


# Sale Pokemon Operation
def sell_pokemon(sale_record, sale_id):
    inventory = display_pokemon_inventory(sale_record)
    inventory_id = get_inventory_id(sale_record)
    pokemon_record = inventory[inventory_id]
    sale_record_index = sale_record.index(pokemon_record)
    purchase_price = float(sale_record[sale_record_index]['purchase_price'])
    sale_price = input_sale_price(purchase_price)
    sale_record[sale_record_index]['sale_id'] = sale_id
    sale_record[sale_record_index]['sale_flag'] = True
    sale_record[sale_record_index]['sale_price'] = sale_price
    profit = sale_price - purchase_price
    print("Profit of the sell: ", profit)


# Business operation options
def print_operation_options():
    print("Please choose what you wish do - input numbers to operate:\n\t"
          "1 - Purchase a new Pokemon\n\t"
          "2 - Sell a Pokemon\n\t"
          "3 - Check Pokemon Inventory\n\t"
          "4 - Check Pokemon Information by PokeIndex\n\t"
          "5 - Clear Screen\n\t"
          "6 - Save to Record and Log Out\n\t"
          )


def get_accounting_record(file_name):
    with open(file_name) as json_file:
        data = json.load(json_file)
    return data


def record_account_record(data, file_name):
    with open(file_name, "w") as jsonFile:
        json.dump(data, jsonFile)


def login(account_info, pokemon_index_df, sale_record):
    username = input("Input Username: ").lower()
    password = input("Input Password: ")
    for account in account_info:
        if account['username'] == username and account['password'] == password:
            if username == 'teamrocket':
                clear()
                print("Manager Login Successful")
                manager_operation(sale_record, account_info)
            else:
                clear()
                print("Sale Assistant Login Successful")
                sale_assist_operation(pokemon_index_df, sale_record, username)
    print("Username not found or incorrect password, please try again")
    login(account_info, pokemon_index_df, sale_record)


def add_new_account(account_info, pokemon_index_df, sale_record):
    while True:
        username = input("Input a New Username with at least 6 characters: ")
        if len(username) >= 6:
            break
        else:
            print("Username less than 6 characters, please try again")

    while True:
        password = input("Input a New Password with at least 6 characters: ")
        if len(password) >= 6:
            re_entry = input("Please re-enter the password: ")
            if re_entry == password:
                break
            else:
                print("Your passwords did not match, please try again")
    account_info.append({"username": username, "password": password})
    record_account_record(account_info, 'data/account.json')
    sale_assist_operation(pokemon_index_df, sale_record, username)


def login_menu(account_info, pokemon_index_df, sale_record):
    print()
    while True:
        try:
            opt = int(input("To Login, input 1 \nTo Add a New Assistant Account, input 2\n "))
            if opt == 1:
                login(account_info, pokemon_index_df, sale_record)
            elif opt == 2:
                add_new_account(account_info, pokemon_index_df, sale_record)
            else:
                print("Invalid operation input. Please try again.")
        except ValueError:
            print("Invalid operation input. Please try again.")


# function to clear the screen based on different operating system
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_screen_cutter():
    print("_______________________________________________________________________")


def sale_assist_operation(pokemon_index_df, sale_record, sale_id):
    while True:
        print_screen_cutter()
        print_operation_options()
        operation = str(input()).strip()

        # record all operations to a json file and exit the program
        if operation == "6":
            record_account_record(sale_record, 'data/record.json')
            print("Program Terminated")
            clear()
            sys.exit()
        # clear screen
        elif operation == "5":
            clear()
        # check pokemon information by pokeIndex
        elif operation == "4":
            poke_index = get_poke_index()
            pokemon = get_pokemon_info(pokemon_index_df, poke_index)
            print_pokemon_info(pokemon)
            print_screen_cutter()
        # check pokemon inventory
        elif operation == "3":
            display_pokemon_inventory(sale_record)
        # sell a pokemon
        elif operation == "2":
            sell_pokemon(sale_record, sale_id)
            print("Sell Operation completed")
            print_screen_cutter()
        # purchase a new pokemon
        elif operation == "1":
            sale_record = purchase_pokemon(pokemon_index_df, sale_record)
            print("Purchase Operation completed")
            print_screen_cutter()
        else:
            print("Invalid Operation! Please try again")


# Manager Utilities
def print_manager_options():
    print("Please choose what you wish do - input numbers to operate:\n\t"
          "1 - Check Profit by Sale Representative\n\t"
          "2 - Check Total Profit\n\t"
          "3 - Check Pokemon Inventory\n\t"
          "4 - List All Sale Representatives\n\t"
          "5 - Clear Screen\n\t"
          "6 - Log Out\n\t"
          )


def manager_operation(sale_record, account_info):
    while True:
        print_screen_cutter()
        print_manager_options()
        operation = str(input()).strip()

        # record all operations to a json file and exit the program
        if operation == "6":
            print("Program Terminated")
            time.sleep(1)
            clear()
            sys.exit()
        # clear screen
        elif operation == "5":
            clear()
        # List All Sale Representatives
        elif operation == "4":
            list_all_rep(account_info)
            print_screen_cutter()
        # check pokemon inventory
        elif operation == "3":
            display_pokemon_inventory(sale_record)
        # Check Total Profit
        elif operation == "2":
            report_total_profit(sale_record)
        # Check Profit by Sale Representative
        elif operation == "1":
            report_profit_by_sale_rep(sale_record, account_info)
        else:
            print("Invalid Operation! Please try again")


def report_profit_by_sale_rep(sale_record, account_info):
    rep = {}
    for item in account_info:
        rep[item['username']] = 0

    for record in sale_record:
        if record['sale_flag'] is True:
            profit = float(record['sale_price']) - float(record['purchase_price'])

            rep[record['sale_id']] += profit

    table = PrettyTable()
    table.field_names = ['Sale Rep', 'Total Profit']

    for item in rep:
        table.add_row([item, rep[item]])

    print(table)


def list_all_rep(account_info):
    rep_table = PrettyTable()
    rep_table.field_names = ["Index", "Sale ID"]
    count = 1
    for rep in account_info:
        rep_table.add_row([count, rep['username']])
        count += 1
    print(rep_table)


def report_total_profit(sale_record):
    profit = 0
    for item in sale_record:
        if item['sale_flag'] is True:
            profit += float(item['sale_price']) - float(item['purchase_price'])
    print("The Total Profit is: $", profit)
    print_screen_cutter()
