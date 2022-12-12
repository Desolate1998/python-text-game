from Creature import Creature


class Goblin(Creature):
    def __init__(self, name, max_hp=15,tags=None):
        Creature.__init__(self, name, max_hp=max_hp,tags=tags)
        self.Abilities = {"Attack": 4, "Defense": 6, "Speed": 6}



