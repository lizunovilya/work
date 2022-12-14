from Character import character
from Berserk import berserk
player1 = character('Vasya', damage=2)
player2 = berserk('Petya', health=50)

print(player1)
print(player2)

while player1.health > 0 and player2.health > 0:
    player1.attack(player2)
    player2.attack(player1)

    print(player1)
    print(player2)