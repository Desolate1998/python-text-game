from Creature import Creature


class Fighter(Creature):
    def __init__(self, name, max_hp=50,tags=None):
        Creature.__init__(self, name, max_hp=max_hp,tags=tags)
        self.shield_is_up = False
        self.Abilities = {"Attack": 5, "Defense": 10, "Speed": 3}

    def shield_up(self):
        # if not self.shield:
        self.Abilities['Attack'] -= 5
        self.Abilities['Defense'] += 5
        self.shield_is_up = True
        print(f"{self.Name} takes a defensive stance.")

    def shield_down(self):
        # if self.shield:
        self.Abilities['Attack'] += 5
        self.Abilities['Defense'] -= 5
        self.shield_is_up = False
        print(f"{self.Name} stance returns to normal.")

    def turn(self, round_num, target):

        if round_num % 4 == 0: 
            if self.shield_is_up:
                self.shield_down()
            print(f'{self.Name} attackes {target.Name}')
            self.attack(target)
        else:
            print(f'{self.Name} attackes {target.Name}')
            self.attack(target) 
            if not self.shield_is_up:
                self.shield_up()
        return target.check_life() == 0


