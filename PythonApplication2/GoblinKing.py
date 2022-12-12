from Archer import Archer
from Goblin import Goblin

class GoblinKing(Goblin,Archer):
    def __init__(self, name, max_hp=50,tags=None):
        Archer.__init__(self,name)
        Goblin.__init__(self,name,max_hp=max_hp,tags=tags)

    def turn(self, round_num, target):
       return Archer.turn(self,round_num,target)
        