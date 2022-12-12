from Creature import Creature

class Orc(Creature):
    def __init__(self, name, max_hp=50,tags=None):
        Creature.__init__(self, name, max_hp=max_hp,tags=tags)
        self.Abilities = {"Attack": 10, "Defense": 6, "Speed": 2}
        self.Stats_Altered = False
        self.Attack_Counter = 1

    def heavy_attack(self,target):
        if not self.Stats_Altered:
            self.Abilities['Attack'] += 5
            self.Abilities['Defense'] -= 3
            self.Stats_Altered = True

        print(f"{self.Name} uses heavy attack on {target.Name}.")
        super().attack(target)

    def attack(self, target):
        if self.Stats_Altered:
            self.Abilities = {"Attack": 10, "Defense": 6, "Speed": 2}

        print(f"{self.Name} attacks {target.Name}.")
        super().attack(target)

    def turn(self, round_num, target):
        if self.Attack_Counter == 4:
            self.heavy_attack(target)
        else:
            self.attack(target)
        if self.Attack_Counter == 4:
            self.Attack_Counter = 1
        else:
            self.Attack_Counter += 1

        return target.check_life() == 0
