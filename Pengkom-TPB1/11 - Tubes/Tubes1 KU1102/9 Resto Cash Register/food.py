from menu_item import MenuItem
import fungsimesin as fm

# Membuat class food yang berisi method(fungsi dalam class) info dan calorie count

# KAMUS LOKAL
# name : str
# price, calorie__count : int

# ALGORITMA
class Food(MenuItem):
    def __init__(self, name, price, calorie_count):
        super().__init__(name, price)
        self.calorie_count = calorie_count
    def info(self):
        return self.name + ': ' + str(fm.formatrupiah(self.price)) + ',00' + ' (' + str(self.calorie_count) + 'kkal)'
         