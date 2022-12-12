from random import randrange, choice
from OrcGeneral import OrcGeneral
from Fighter import Fighter
from Archer import Archer
from GoblinKing import GoblinKing
from Goblin import Goblin
from Orc import Orc
from Wizard import Wizard


def fight(rounds, first_entity, second_entity):
    for current_round in range(1, rounds + 1):
        print(f"Round {current_round}:")
        print("=" * 30)
        if first_entity.turn(current_round, second_entity) or second_entity.turn(current_round, first_entity):
            return
        print("=" * 30)


gandy = Wizard('Gandy')
orcGeneral = OrcGeneral('Orc General')
goblinKing = GoblinKing('Goblin king')

fighter = Fighter('Fighter')
goblin = Goblin('Goblin')

archer = Archer('Archer')
orc = Orc('orc')

gandy.attack(archer)
gandy.fire_bolt(orc)
gandy.fire_storm([archer,orc,goblin,fighter])
gandy.mass_heal([archer,orc,goblin,fighter])
gandy.recharge()
