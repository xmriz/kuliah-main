# Membuat class menu item yang berisi method get_total_price()

# KAMUS LOKAL
# name : str
# price : int

# ALGORITMA
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_total_price(self, count):
        total_price = self.price * count

        if count > 3:
            total_price *= 0.9

        return round(total_price)
