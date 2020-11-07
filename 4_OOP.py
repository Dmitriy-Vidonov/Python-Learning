import random

class Weapon:
    
    def __init__(self, weapon_name, weapon_damage,
                 weapon_price, weapon_abrasion):
        self._name = weapon_name
        self._damage = weapon_damage
        self._price = weapon_price
        self._abrasion = weapon_abrasion
        
    def foo(self, new_price):
        self._price = new_price
        return print("Родитель Weapon. Цена =", self._price)
        
class Steel_Weapon(Weapon):
    
    def __init__(self, steel_weapon_type,
                 weapon_name, weapon_damage,
                 weapon_price, weapon_abrasion):
        super().__init__(weapon_name, weapon_damage,
                 weapon_price, weapon_abrasion)
        self.__type = steel_weapon_type
    
    def foo(self, new_price):
        self.__price = 200
        return print("Потомок Steel_Weapon. Цена =", self.__price)        

class Silver_Weapon(Weapon):
    
    def __init__(self, silver_weapon_type,
                 silver_weapon_ability,
                 weapon_name, weapon_damage,
                 weapon_price, weapon_abrasion):
        super().__init__(weapon_name, weapon_damage,
                 weapon_price, weapon_abrasion)
        self.__type = silver_weapon_type
        self.__ability = silver_weapon_ability
        
    def foo(self, new_price):
        self.__price = 300
        return print("Потомок Silver_Weapon. Цена =", self.__price)
        
grabli = Weapon("Грабли", 100, 50, 87)
grabli.foo(70)

arondit = Silver_Weapon("Реликт", "Накопление урона", "Арондит",
                       750, 2100, 0)
arondit.foo(200)

burning_rose_sword = Steel_Weapon("Предмет мастера",
                                  "Меч рыцарей пылающей розы",
                                  300, 1700, 15)
burning_rose_sword.foo(150)

# *****************

# steel_swords
ard_aenye = Steel_Weapon("Реликт", "Ард Эйн", 320, 500, 15) #1
angivar = Steel_Weapon("Реликт", "Ангивар", 250, 600, 0) #2
bahnshee = Steel_Weapon("Реликт", "Банши", 300, 550, 54) #3
long_claw = Steel_Weapon("Обычный", "Длинный коготь", 420, 650, 10) #4
ancient_elf_sword = Steel_Weapon("Магический", "Древний эльфский меч",
                                 510, 1000, 0) #5

# silver_swords
addan_deit = Silver_Weapon("Реликт", "Повышенное кровотечение",
                           "Аддан Дейт", 500, 800, 72) #1
anaphema = Silver_Weapon("Реликт", "Шанс вызвать горение",
                         "Анафема", 480, 720, 24) #2
mountain_tooth = Silver_Weapon("Мастерский", "Доп. урон при ударе",
                               "Горный зуб", 370, 600, 15) #3
meltyh = Silver_Weapon("Магический", "Шанс критического удара",
                       "Мелтих", 420, 1000, 0) #4
tuneller = Silver_Weapon("Обычный", "Шанс критического удара",
                         "Проходчик", 500, 1550, 0) #5
                         
armory = [ard_aenye, addan_deit, angivar, anaphema,
          bahnshee, mountain_tooth, long_claw, meltyh,
          ancient_elf_sword, tuneller]
          
inventory = []

print()

for i in range(10):
    inventory.append(armory[random.randint(0, 9)])

for Weapon in inventory:
    Weapon.foo(10)
