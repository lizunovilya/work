from Character import character
from Berserk import berserk
from Paladin import paladin

player1 = character('Vasya', health=100, damage=1)
player2 = berserk('Petya', health=50, damage=2)
player3 = paladin('grisha', health=40, damage=1, defence=1)

print(player1)
print(player2)
print(player3)

while player1.health > 0 and player2.health > 0 and player3.health > 0:
    player1.attack(player2)
    player1.attack(player3)
    Character_damage = player1.damage
    Berserk_damage = player2.damage
    Paladin_damage = player3.damage

    print(f'{player1.name} нанес {Character_damage} урона ')
    print(f'{player2.name} нанес {Berserk_damage} урона ')
    print(f'{player3.name} нанес {Paladin_damage} урона ')
    print(player1)
    print(player2)
    print(player3)