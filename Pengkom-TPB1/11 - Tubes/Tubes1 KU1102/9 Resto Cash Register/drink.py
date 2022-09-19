from menu_item import MenuItem
import fungsimesin as fm

# Membuat class drink yang berisi method(fungsi dalam class) info

# KAMUS LOKAL
# name : str
# price, calorie__count : int

# ALGORITMA
class Drink(MenuItem): 
    def __init__(self, name, price, volume): #timpa juga method __init__
        super().__init__(name, price)
        self.volume = volume
    def info(self):
        return self.name + ': ' + str(fm.formatrupiah(self.price)) + ',00' + ' (' + str(self.volume) + 'mL)'
