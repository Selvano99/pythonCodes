

class Enemies:



    def __init__(self, type_of_enemy, attack_damage, health_point):
        self.__type_of_enemy = type_of_enemy
        self.attack_damage = attack_damage
        self.health_point = health_point

    def talk(self):
        print(f'I am a {self.__type_of_enemy} and i will kill you')

    def get_type_of_enemy(self):
        return self.__type_of_enemy

    def attack(self):
        print(f'{self.__type_of_enemy} attacks for {self.attack_damage} damage')

    def special_attack(self):
        print('enemy has no special attacks')