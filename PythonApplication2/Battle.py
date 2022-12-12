from email.policy import default
from random import randrange, choice
from OrcGeneral import OrcGeneral
from Fighter import Fighter
from Archer import Archer
from GoblinKing import GoblinKing
from Goblin import Goblin
from Orc import Orc
from Wizard import Wizard


class Battle:
   def __init__(self):
       self.Enemies =[
        GoblinKing('GoblinKing',tags=['Enemy']),
        OrcGeneral('OrcGeneral',tags=['Enemy']),
        Goblin('Goblin',tags=['Enemy']),
        Orc('Orc',tags=['Enemy'])
      ]
       self.Allies = [Archer('Archer',tags=['Ally']), Fighter('Fighter',tags=['Ally'])]
       self.Player = Wizard('Thea',tags=['Player'])
       self.entityList = self.Enemies + self.Allies + [self.Player] 

   def auto_select(self,target_list):
       return choice(target_list)


   def select_target(self,target_list):
       for index in range(0,len(target_list)):
           print(f'{index+1}:{target_list[index].Name},HP: {target_list[index].HP}/{target_list[index].MaxHP}')
       selectedItem =  None
       validInput = False
       while not validInput:
            try:
                user_input = input('Enter choice:')
                selectedItem =  target_list[int(user_input)-1]
                validInput = True
            except:
                print('option is not valid')
       return selectedItem
   
   def check_win_condition(self):
       #Instead of using an int counter here a boolean is used here in because it only takes 2 bytes.
       hasEnemy=False 
       hasPlayer=False
       hasAlly=False

       for entity in self.entityList:
            if entity.HP == 0:
                self.entityList.remove(entity)
            elif 'Enemy' in entity.Tags:
                hasEnemy=True
            elif 'Ally' in entity.Tags:
                hasAlly=True
            else:
                hasPlayer = True
            #No need to loop more if we know all entites are present
            if hasPlayer and hasEnemy and hasAlly:
                return True
       
       if not hasEnemy:
           print('Game has ended. All enemies have been defeated, Game won!')
       elif not hasPlayer:
            print('Game has ended, all allies have been lost. Game lost!')
       else:
            print('Game has ended,player has died, Game lost!')
        
       return False

   def start(self):
       self.entityList = sorted(self.entityList,key=lambda x:x.Abilities['Speed'],reverse=True)

       gameActive = True
       currentRound = 1
       while gameActive:
           print('='*30)
           print(f'Round {currentRound}.')
           print('='*30)
           for creature in self.entityList:
                if 'Enemy' in creature.Tags:
                    target = self.auto_select(self.Allies)
                    creatureDied = creature.turn(currentRound,target)
                    if creatureDied:
                        gameActive =self.check_win_condition()
                elif 'Ally' in creature.Tags:
                    creatureDied = creature.turn(currentRound,self.auto_select(self.Enemies))
                    if creatureDied:
                        gameActive =self.check_win_condition()
                else:
                    print(f'Player: {creature.Name} HP:{creature.HP}/{creature.MaxHP} Mana:{creature.Mana}')

                    print('Allies:')
                    for ally in self.Allies:
                       if 'Ally' in ally.Tags:
                           print(f" {ally.Name:<10} {ally.HP}/{ally.MaxHP}")
                    print('='*30)
                    print('Actions. F: Attack R: Recharge Mana')
                    print('Spells. 1: Heal 2:Firebolt 3: Mass Heal 4: Fire Storm')
                    print('To quit the game type quit')
                    validInput = False
                    while not validInput:
                        user_input = input('Enter choice:')
                        validInput = True
                        match user_input.upper():
                            case '1':
                                creature.heal(self.select_target(self.Allies))
                            case '2':creature.fire_bolt(self.select_target(self.Enemies))
                            case '3':creature.mass_heal(self.Allies)
                            case '4':creature.fire_storm(self.Enemies)
                            case 'F':creature.Attack(self.select_target(self.Enemies))
                            case 'R':creature.recharge()
                            case 'QUIT': exit()
                            case _: 
                                print('invalid input')
                                validInput = False

           currentRound+=1
           pass

bat = Battle()
bat.start()