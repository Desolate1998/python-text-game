from Orc import Orc
from Fighter import Fighter



class OrcGeneral(Orc,Fighter):
    def __init__(self, name, max_hp=100,tags=None):
       Fighter.__init__(self,name)
       Orc.__init__(self,name,max_hp=max_hp,tags=tags)

    def turn(self, round_num, target):
        if self.Attack_Counter == 1:
            self.attack(target)
            if not self.shield_is_up:
                self.shield_up()
        elif self.Attack_Counter == 2:
            self.attack(target)
        elif self.Attack_Counter == 3:
            if self.shield_is_up:
                self.shield_down()
            self.attack(target)
        else:
            self.heavy_attack(target)
        
        if self.Attack_Counter == 4:
            self.Attack_Counter = 1
        else:
            self.Attack_Counter += 1

        return target.check_life() == 0
