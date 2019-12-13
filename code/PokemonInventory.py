class PokemonInventory:
    def __init__(self, poke_index, sale_id=0, level=0, age=0, purchase_price=0.00, sale_price=0.00, sale_flag=False):
        # generated at the time of sale
        self.sale_id = sale_id
        self.poke_index = poke_index

        # set data at time of purchase
        self.level = level
        self.age = age
        self.purchase_price = purchase_price
        self.sale_price = sale_price
        self.sale_flag = sale_flag
