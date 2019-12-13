# Pokemon entity class

# default name to empty string
name = {
    "english": "",
    "japanese": "",
    "chinese": "",
    "french": ""
}

# default base to 0
base = {
    "HP": 0,
    "Attack": 0,
    "Defense": 0,
    "Sp_Attack": 0,
    "Sp_Defense": 0,
    "Speed": 0
}


class Pokemon:
    # init pokemon with pokemon json data
    def __init__(self, id=0, name=name, type=[], base=base, level=0, age=0, purchase_price=0, sale_price=0):
        # JSON Data
        self.id = id
        self.name = name
        self.type = type
        self.base = base

        # self-set data
        self.level = level
        self.age = age
        self.purchase_price = purchase_price
        self.sale_price = sale_price
