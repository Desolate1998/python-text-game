from Creature import Creature
from random import randrange, choice


class Archer(Creature):
    def __init__(self, name, max_hp=30,tags= None):
        Creature.__init__(self, name, 1, 9, max_hp,tags=tags)
        self.Abilities = {"Attack": 7, "Defense": 8, "Speed": 8}
        self.Stats_Altered = False
        self.Attack_Counter = 1

    def sneak_attack(self, target):
        roll = max(randrange(0, 20), randrange(0, 20))
        if self.Abilities['Speed'] > target.Abilities['Speed']:
            roll += self.Abilities['Speed'] - target.Abilities['Speed']
        
        if not self.Stats_Altered:
            self.Abilities['Defense'] -= 3
            print(f'{self.Name} def lowered')
            self.Abilities['Attack'] += 3
            print(f'{self.Name} attack rised')
            self.Stats_Altered = True

        print(f'{self.Name} sneak attacks {target.Name}... Sneak attack ')
        return super().attack(target,roll=roll)

    def attack(self, target):
        if self.Stats_Altered:
            self.Abilities = {"Attack": 7, "Defense": 8, "Speed": 8}
            self.Stats_Altered = False

        print(f"{self.Name} attacks {target.Name}.")
        return super().attack(target)

    def turn(self, round_num, target):
        if self.Attack_Counter == 1:
            self.attack(target)
        else:
            self.sneak_attack(target)
        if self.Attack_Counter == 4:
            self.Attack_Counter = 1
        else:
            self.Attack_Counter += 1

        return target.check_life() == 0

