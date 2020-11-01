class Witcher:
    
    def __init__(self, witcher_name, witcher_age,
                 witcher_weight, witcher_school,
                 witcher_adrenaline, witcher_energy,
                 witcher_physical_damage_resistance,
                 witcher_poison_resistance,
                 witcher_magic_resistance,
                 witcher_attack_power, witcher_speed,
                 witcher_health, witcher_intoxication_level):
        self.name = witcher_name
        self.age = witcher_age
        self.weight = witcher_age
        self.school = witcher_school
        self.adrenaline = witcher_adrenaline
        self.energy = witcher_energy
        self.physical_damage_resistance = witcher_physical_damage_resistance
        self.poison_resistance = witcher_poison_resistance
        self.magic_resistance = witcher_magic_resistance
        self.attack_power = witcher_attack_power
        self.speed = witcher_speed
        self.health = witcher_health
        self.intoxication_level = witcher_intoxication_level
    
    def Stop(self):
        self.speed = 0
    
    def Walk(self):
        self.speed = 5
        
    def Run(self):
        self.speed = 15
        self.energy -= 30
        
    def Sleep(self):
        self.speed = 0
        self.energy = 100
        self.adrenaline = 0
        self.weight -= 0.3
        self.intoxication_level = 0
    
    def Meditation(self):
        self.speed = 0
        self.energy = 100
        self.adrenaline = 0
        self.health = 100
        
    def Eat(self, food):
        self.weight += food
        self.energy = 100
        self.health += 20
        self.physical_damage_resistance += 5
    
    def White_Honey_Potion(self):
        self.intoxication_level = 0
        
    def Grey_Owl_Potion(self):
        self.energy = 100
        
    def Raffal_White_Potion(self):
        self.physical_damage_resistance += 20
    
    def RedBird_Potion(self):
        self.poison_resistance += 50
        self.intoxication_level = 0
    
    def Fencing_Learning(self):
        self.attack_power += 10
    
    
# **************************************************

class Silver_Sword:
    
    def __init__(self, silver_sword_name, silver_sword_school, 
                 silver_sword_durability, silver_sword_abrasion,
                 silver_sword_damage, silver_sword_oil_damage,
                 silver_sword_glyphs, silver_sword_oiled_hits):
        self.name = silver_sword_name
        self.school = silver_sword_school
        self.durability = silver_sword_durability
        self.abrasion = silver_sword_abrasion
        self.damage = silver_sword_damage
        self.oil_damage = silver_sword_oil_damage
        self.glyphs = silver_sword_glyphs
        self.oiled_hits = silver_sword_oiled_hits
        
    def Usual_Hit(self):
        self.abrasion += 0.3

    def Power_Hit(self):
        self.abrasion += 0.5
    
    def Sharpening(self):
        self.damage += 25
    
    def Vampire_Oil(self):
        self.oil_damage += 50
        
    def Alchemy_Learning(self):
        self.oiled_hits += 10
    
    def Strength_Glyph(self):
        self.glyphs = Strength_Glyph
        self.durability += 25
        
    




        
        
        
                 
    