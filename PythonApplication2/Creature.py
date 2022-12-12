from random import randrange, choice

class Creature:
    def __init__(self, name, min_damage=1, max_damage=5, max_hp=10,tags=None):
        self.Name = name
        self.HP = max_hp
        self.MaxHP = max_hp
        self.Abilities = {"Attack": 1, "Defense": 5, "Speed": 5}
        self.MinDamage = min_damage
        self.MaxDamage = max_damage
        self.Tags = tags

    def check_life(self):
        print(f'{self.Name} has {self.HP} HP LEFT' )
        if self.HP <= 0:
            self.HP = 0
            print(f"{self.Name} fainted.")
        return self.HP

    def attack(self, target,roll=None):
       is_success = False
       if roll is None:
          roll = randrange(1, 20)
        
       if roll < (target.Abilities['Attack'] + target.Abilities['Speed']):
            print("Attack missed...")
       else:
            damage =self.Abilities['Attack'] + choice(range(self.MinDamage, self.MaxDamage))
            target.HP -=  damage
            print(f"Attack hits for {damage} damage!")
            is_success = True
        
       return is_success

    def turn(self, round_num, target):
        print(f'{self.Name} attackes {target.Name}')
        self.attack(target)
        return target.check_life() == 0


