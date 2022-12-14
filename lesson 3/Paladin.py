from Character import character

class paladin (character):

    def __init__(self, name, health=100, damage=1, defence=1):
        character.__init__(self, name, health, damage, defence)

    def take_damage(self, damage):
        taken_damage = (self.damage - self.defence)

