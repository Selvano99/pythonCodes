from Ogre import *
from Zombie import *
from Enemies import *
from Hero import *
from Weapon import *

zombie = Zombie( 100,500)

dark_wizard = Enemies('Dark Wizard', 100,10)

ogreNero =Ogre(40,1000)

def battle(e1: Enemies,e2: Enemies):
    print('battle starts')
    e1.talk()
    e2.talk()

    while e1.health_point > 0 and e2.health_point > 0:
        e1.special_attack()
        e2.special_attack()
        print(f'{e1.get_type_of_enemy()}: {e1.health_point} HP left ')
        print(f'{e2.get_type_of_enemy()}: {e2.health_point} HP left ')
        e2.attack()
        e1.health_point -= e2.attack_damage
        e1.attack()
        e2.health_point -=e1.attack_damage

    if e1.health_point > 0:
        print(f'{e1.get_type_of_enemy()} wins!')
    else:
        print(f'{e2.get_type_of_enemy()} wins!')



hero = Hero(700,85)
weapon = Weapon('Sword', 15)
hero.weapon = weapon
hero.equip_weapon()


def heroBattle(hero: Hero,enemy: Enemies):
    print('battle starts')

    print(f'Zombie is attacking {enemy.talk()}')

    while hero.health_point > 0 and enemy.health_point > 0:
        enemy.special_attack()
        print(f'hero: {hero.health_point} HP left ')
        print(f'{enemy.get_type_of_enemy()}: {enemy.health_point} HP left ')
        enemy.attack()
        hero.health_point -= enemy.attack_damage
        hero.attack()
        enemy.health_point -=hero.attack_damage

    if hero.health_point > 0:
        print(' hero wins!')
    else:
        print(f'{enemy.get_type_of_enemy()} wins!')


heroBattle(hero,zombie)


