import time


class WeaponBreakError(Exception):
    pass
class Gladiator:
    arena_population = 0
    
    class Weapon:
        def __init__(self, name, damage):
            self.name = name
            self.damage = damage
            self.durability = 2
            
    def __init__(self,name,weapon_name,damage):
        self.name = name
        self.hp = 100
        
        self.weapon = self.Weapon(weapon_name,damage)
        Gladiator.arena_population +=1
        
    def attack(self,target):
        if self.weapon.durability <=0:
            raise WeaponBreakError()
        
        time.sleep(2)
        
        print(f" {self.name} attacks {target.name} with {self.weapon.name}!")
        target.hp -= self.weapon.damage
        self.weapon.durability -= 1
        
        print(f"HIT! {target.name} HP {target.hp}")

class Warrior(Gladiator):
    def __init__(self,name,weapon_name,damage):
        super().__init__(name,weapon_name,damage)
        
    def attack(self,target):
        try:
            super().attack(target)
        except WeaponBreakError:
            time.sleep(2)
            print(f" OH NO! {self.weapon.name} has broken!!")
            print(f" {self.name} punches {target.name} (-5 HP)")
            target.hp -=5
            
def run_game():
    hero = Warrior("Hercules", "Spear", 15)
    enemy = Gladiator("Beast", "claws", 10)
    
    
    print(f"  --Battle starts! Fighters: hero: {hero.name}, {enemy.name}-- ")
    print(f" Number of Gladiators in arena: {Gladiator.arena_population}")
    
    
    while hero.hp > 0 and enemy.hp> 0:
        input("\n press Enter to fight... ")
        
        
        hero.attack(enemy)
        
        if enemy.hp > 0:
            try:
                enemy.attack(hero)
            except WeaponBreakError:
                print(f" {enemy.name}'s claws are broken! They run away! ")
                break

    if hero.hp>0:
        print(f" \n hero wins!! ")
    else:
        print("\n Game over")
        
        
run_game()

        
            
            
                
                
        
        