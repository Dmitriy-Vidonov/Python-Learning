class Silver_Sword:
    
    def __init__(self, silver_sword_name, silver_sword_school, 
                 silver_sword_durability, silver_sword_abrasion,
                 silver_sword_damage, silver_sword_oil_damage,
                 silver_sword_glyphs, silver_sword_oiled_hits):
        self.__name = silver_sword_name  # Предположим, что имя  
                                         # не наследуется
        self._school = silver_sword_school
        self._durability = silver_sword_durability
        self._abrasion = silver_sword_abrasion
        self._damage = silver_sword_damage
        self._oil_damage = silver_sword_oil_damage
        self._glyphs = silver_sword_glyphs
        self._oiled_hits = silver_sword_oiled_hits
        
    def Usual_Hit(self):
        self._abrasion += 0.3

    def Power_Hit(self):
        self._abrasion += 0.5
    
    def Sharpening(self):
        self._damage += 25
        
    def Repair(self):
        self._abrasion = 0
    
    def Vampire_Oil(self):
        self._oil_damage += 50
        
    def Alchemy_Learning(self):
        self._oiled_hits += 10
    
    def Strength_Glyph(self):
        self._glyphs = Strength_Glyph
        self._durability += 25
        
ss_bear_school = Silver_Sword("Серебряный меч школы Медведя",
                              "Школа медведя", 120, 0, 300, 0, 0, 0)

hits = 15 # Нанесли 15 ударов мечом
for i in range(hits):
    ss_bear_school.Usual_Hit()

print("Износ меча после", hits, "обычных ударов -", 
       int(ss_bear_school._abrasion))

power_hits = 5 # Нанесли 10 сильных ударов мечом
for i in range(power_hits):
    ss_bear_school.Power_Hit()
    
print("Износ меча после", hits, "обычных ударов и", power_hits,
      "мощных ударов -", int(ss_bear_school._abrasion))

ss_bear_school.Repair()
print("Износ меча после ремонта -", ss_bear_school._abrasion)

# *************************************************************
class Weapon:
    
    def __init__(self, weapon_damage, weapon_required_level,
                 weapon_weight, weapon_abrasion, 
                 weapon_current_price, weapon_max_price):
        self._damage = weapon_damage
        self._level = weapon_required_level
        self._weight = weapon_weight
        self._abrasion = weapon_abrasion
        self._current_price = weapon_current_price
        self._max_price = weapon_max_price
        
    def Hit(self, new_abrasion):
        self._abrasion += new_abrasion
        self._current_price -= self._current_price / 100 * 0.1 
    
    def Repair(self):
        self._abrasion = 0
        self._current_price = self._max_price
        
class Crossbow(Weapon):
    
    def __init__(self, crossbow_name, weapon_damage,
                 weapon_required_level, weapon_weight, 
                 weapon_abrasion, weapon_current_price,
                 weapon_max_price):
        super().__init__(weapon_damage,
                 weapon_required_level, weapon_weight, 
                 weapon_abrasion, weapon_current_price,
                 weapon_max_price)
        self.__name = crossbow_name
        
bokler_crossbow = Crossbow("Арбалет из Боклера", 
                           120, 35, 2, 78, 300, 450)

class Witcher_Crossbow(Weapon):
    
    def __init__(self, witcher_crossbow_name, witcher_crossbow_school, 
                 weapon_damage, weapon_required_level, 
                 weapon_weight, weapon_abrasion, 
                 weapon_current_price, weapon_max_price):
        super().__init__(weapon_damage,
                 weapon_required_level, weapon_weight, 
                 weapon_abrasion, weapon_current_price,
                 weapon_max_price)
        self.__name = witcher_crossbow_name
        self.__school = witcher_crossbow_school
        
cat_school_crossbow = Witcher_Crossbow("Арбалет школы кота",
                                       "Школа кота", 200, 29,
                                       1.9, 0, 350, 350)

class Auxiliary_Weapon(Weapon):
    
    def __init__(self, aux_weapon_name, aux_w_item_type, weapon_damage, 
                 weapon_required_level, weapon_weight, 
                 weapon_abrasion, weapon_current_price, 
                 weapon_max_price):
        super().__init__(weapon_damage,
                 weapon_required_level, weapon_weight, 
                 weapon_abrasion, weapon_current_price,
                 weapon_max_price)
        self.__name = aux_weapon_name
        self.__item_type = aux_w_item_type
        
    def Power_Hit(self, new_abrasion):
        self._abrasion += new_abrasion
        self._current_price -= self._current_price / 100 * 0.2
        self._weapon_damage *= 1.2
        
small_axe = Auxiliary_Weapon("Топорик", "Обычный предмет",
                             150, 12, 3, 87, 80, 90)
        
class Steel_Weapon(Weapon):
    
    def __init__(self, steel_weapon_name, steel_w_item_type,
                 steel_weapon_oil_damage, steel_weapon_glyphs,
                 steel_weapon_oiled_hits,
                 weapon_damage, weapon_required_level, 
                 weapon_weight, weapon_abrasion, 
                 weapon_current_price, weapon_max_price):
        super().__init__(weapon_damage,
                 weapon_required_level, weapon_weight, 
                 weapon_abrasion, weapon_current_price,
                 weapon_max_price)
        self.__name = steel_weapon_name
        self.__item_type = steel_w_item_type
        self.__oil_damage = steel_weapon_oil_damage
        self.__glyphs = steel_weapon_glyphs
        self.__oiled_hits = steel_weapon_oiled_hits
        
kovir_dirk = Steel_Weapon("Ковирский кортик", "Предмет мастера",
                          0, 0, 0, 280, 10, 2.5, 90, 180, 190)




        
    
