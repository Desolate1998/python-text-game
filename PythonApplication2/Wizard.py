from Creature import Creature
from math import floor
from random import randrange, choice

class Wizard(Creature):
    def __init__(self, name, max_hp=20,tags=None):
        Creature.__init__(self, name, max_hp=max_hp,tags=tags)
        self.Abilities = {"Attack": 3, "Defense": 5, "Speed": 5,"Arcane":10}
        self.Mana=100

    def attack(self, target):
        self.__addMana(20)
        print(f"{self.Name} attacks {target.Name}.")
        super().attack(target)

    def recharge(self):
        print(f"{self.Name} channels magical energy...")
        self.__addMana(30)
     
    def __addMana(self,amount):
        if(self.Mana ==100):
            print('Mana is full!')
            return

        print(f"Manna: +{amount}!")
        manaToRegain =min(100,self.Mana+amount) 
        self.Mana = manaToRegain

    def __useMana(self,amount):
        if(self.Mana-amount) < 0:
            return False
        self.Mana = max(0,self.Mana-amount)
        print(f'Mana: - {max(0,self.Mana-amount)}')
        return True

    def fire_bolt(self,target):
       print(f'{self.Name} fires a fire bolt at {target.Name}...')
       roll = floor(self.Abilities['Arcane']/2) + randrange(1, 20)
       self.MinDamage = 1
       self.MaxDamage = self.Abilities['Arcane']
       didHit = super().attack(target,roll=roll)
       if didHit:
           self.__addMana(10)

    def heal(self, target):
        if not self.__useMana(20):
            return

        amountToHeal = floor(self.Abilities['Arcane']/2) + randrange(1, 8)
        target.HP = min(target.MaxHP,target.HP+amountToHeal)
        print(f'{self.Name} heals {target.Name} for {min(target.MaxHP,target.HP+amountToHeal)} HP!')


    def mass_heal(self, targets):
        if not self.__useMana(30):
            return
        
        amountToHeal = floor(self.Abilities['Arcane']/2) + randrange(1, 8)
        self.HP = min(self.MaxHP,self.HP+amountToHeal)
        
        for ally in targets:
            print(f'{self.Name} heals {ally.Name} for {amountToHeal}')
            ally.HP = min(ally.MaxHP,ally.HP+amountToHeal)


    def fire_storm(self,enemies):
        if not self.__useMana(50):
            return

        for enemy in enemies:
            half_damage = enemy.Abilities['Speed'] + randrange(1,20) >= self.Abilities['Arcane']
            damage =self.Abilities['Arcane']+randrange(5,20)
            if(half_damage):
                enemy.HP -= floor(damage/2)
                print(f'Fire Storm deals {floor(damage/2)} fire damage to {enemy.Name}!')
            else:
                enemy.HP -= damage
                print(f'Fire Storm deals {damage} fire damage to {enemy.Name}!')

