from Enemies import *
import random

class Ogre(Enemies):
    def __init__(self, attack_damage, health_point):
        super().__init__(type_of_enemy = 'Ogre',
        attack_damage = attack_damage,
        health_point = health_point)

    def talk(self):
        print('Bubububuuu')

    def special_attack(self):
        dmg_more =0
        did_special_attack_work = random.random() < 0.50
        if did_special_attack_work:
            dmg_more += random.random()*10
            self.attack_damage +=dmg_more
            print(f'Ogre gets angry and deals {self.attack_damage} dmg')