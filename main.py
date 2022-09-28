from asyncio import shield
from monster import Monster, Hoved
import random

level = 0

m = Monster
print("Welcome to dungeons and dragons")

monstere = [0, 0, 0]

monstere[0] = m("bill gates", 80, "Jeg kommer til å eliminere deg med min windows AI")
monstere[1] = m("jeff bezos", 120, "Jeg bruker steroids og kan kjøpe deg")
monstere[2] = m("elon musk", 150, "Jeg kommer til å sende deg til Mars")

hovedkarakter = Hoved("kjetil", 100)

protection = 0
extra_damage = 1
ability_counter = 0
start_line = False

while True:
    if (start_line == False):
        print("Hei, jeg er", monstere[level].navn+".", monstere[level].line)
        ability_counter = 0
        start_line = True

    extra_damage = 1
    protection = 2
    if (ability_counter < 2):
        ability = input("Vil du velge en ability (maks to per runde): heal, shield, extra damage: ")

    input("Klikk enter for å angripe")

    if (ability == "heal"):
        healing = random.randint(10, 20)
        hovedkarakter.heal(healing)
        print("Du healet og har nå", hovedkarakter.hp, "liv")
    elif (ability == "extra damage"):
        extra_damage = 2
    elif (ability == "shield"):
        protection = 1
    if (ability != ""):
        ability_counter += 1

    damage = random.randint(15*extra_damage, 25*extra_damage)
    hoved_damage = random.randint(5*protection, 10*protection)
    print("Monsteret mister", damage, "liv")
    print("Du mister", hoved_damage, "liv")
    monstere[level].lose_hp(damage)
    hovedkarakter.lose_hp(hoved_damage)
    
    if (monstere[level].hp <= 0):
        if (level == 2):
            print("Nice, du vant!")
            exit()
        print(monstere[level].navn, "døde")
        level += 1
        start_line = False
        continue

    if (hovedkarakter.hp <= 0):
        print("You dead", monstere[level].navn+":", "din noob")
        exit()

    print("Din hp:", hovedkarakter.hp, "Monsterets hp:", monstere[level].hp)
