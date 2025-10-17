import random

from Enemies import *
class Zombie(Enemies):

    def __init__(self, attack_damage, health_point):
        super().__init__(type_of_enemy = 'Zombie',
        attack_damage = attack_damage,
        health_point = health_point)

    def talk(self):
        print('Grrrrrrrrr')

    def spread_disease(self):
        print('The Zombie is trying to spread infection')

    def special_attack(self):
        health_more = 0
        did_special_attack_work = random.random() < 0.50
        if did_special_attack_work:
            health_more += random.random()*10
            self.health_point +=health_more
            print('Zombie regenerated 4hp')