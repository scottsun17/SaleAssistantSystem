import Operation


# Software Welcome Page
print("Welcome to Pokemon Accounting System\n\n")

account_info = Operation.get_accounting_record('data/account.json')
pokemon_index_df = Operation.get_pokemon_index()
sale_record = Operation.get_accounting_record('data/record.json')

print("A pokemon system created by Team Rocket Senior Software Engineer pokemon, Porygon2")
print("Porygon2 is monitoring everything you do online")


# Login
sale_id = Operation.login_menu(account_info, pokemon_index_df, sale_record)


