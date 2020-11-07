import random

class Weapon:
    
    def __init__(self, w_name, w_weight, w_damage):
        self._name = w_name
        self._weight = w_weight
        self._damage = w_damage
    
    def foo(self, new_damage):
        self._damage -= new_damage
        return print("Родитель Weapon. Урон =", self._damage)

class Main_Weapon(Weapon):
    
    def __init__(self, mw_type, w_name, w_weight, w_damage):
        super().__init__(w_name, w_weight, w_damage)
        self.__type = mw_type
        
    def foo(self, new_damage):
        self.__damage = 888
        return print("Потомок Main_Weapon. Урон =", self.__damage)

class Aux_Weapon(Weapon):
    
    def __init__(self, aux_w_ability, w_name, w_weight, w_damage):
        super().__init__(w_name, w_weight, w_damage)
        self.__type = aux_w_ability
        
    def foo(self, new_damage):
        self.__damage = 555
        return print("Потомок Aux_Weapon. Урон =", self.__damage)

swords = []

for i in range(10):
    if random.randint(1,10) % 2 == 0: 
        main_sword = Main_Weapon(random.randint(1, 10),    # mw_type
                                 random.randint(1, 10),    # w_name
                                 random.randint(1, 5),     # w_weight
                                 random.randint(200, 600)) # w_damage
        swords.append(main_sword)
        
    else:
        aux_sword = Aux_Weapon(random.randint(1, 10),    # aux_w_ability
                               random.randint(1, 10),    # w_name
                               random.randint(1, 5),     # w_weight
                               random.randint(200, 600)) # w_damage
        swords.append(aux_sword)

for Weapon in swords:
    Weapon.foo(10)
