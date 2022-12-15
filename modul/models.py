class Player:
    def __init__(self,character):
        self.character=character
    def player_class(self,character):
        if self.character==1:
            return 'Wizard'
        if self.character==2:
            return 'Warrior'
        if self.character==3:
            return 'Rogue'
class Enemy:
    def __init__(self, enemy_character):
        self.enemy_character = enemy_character

    def enemy_class(self, enemy_character):
        if self.enemy_character == 1:
            return 'Wizard'
        if self.enemy_character == 2:
            return 'Warrior'
        if self.enemy_character == 3:
            return 'Rogue'
class Lives:
    def __init__(self,lives,increase):
        self.lives=lives
        self.increace=increase
    def next_level(self,increase,lives):
        if self.lives==0:
            print('You beat him. Nice!')
            self.lives+=self.increace
        return self.lives
class Score:
    def __init__(self,lives,score):
        self.score=score
        self.lives=lives
    def count_score(self,lives,score):
        self.score+=5
        return self.score
class Allowed_attacks:
    def __init__(self,attacks):
        self.attacks=attacks
        # я не понял зачем нужен этот класс