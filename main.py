# Av Onat og August

from monster import Monster, Hoved
import random

level = 0
hovedkarakter = Hoved("kjetil", 130)

m = Monster
print("Velkommen til dungeons and dragons. Jeg er hovedkarakteren,", hovedkarakter.navn, ":)")
print("Vi er i fare og må ut av dette rommet, men Bill Gates, Jeff bezos og Elon Musk har nøkklene!!!!!")
print("Vent jeg hører noen snakker...")
monstere = [0, 0, 0]

monstere[0] = m("Bill Gates", 80, "Jeg kommer til å eliminere deg med min windows AI")
monstere[1] = m("Jeff Bezos", 120, "Jeg bruker steroids og kan kjøpe deg")
monstere[2] = m("Elon Musk", 150, "Jeg kommer til å sende deg til Mars")

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
    ability = ""
    if (ability_counter < 2):
        ability = input("Vil du velge en ability (maks to per runde): heal, shield, extra damage: ")

    input("Klikk enter for å angripe")

    if (ability == "heal"):
        healing = random.randint(10, 20)
        hovedkarakter.heal(healing)
        print("Du healet og har nå", hovedkarakter.hp, "liv")
    elif (ability == "extra damage"):
        extra_damage = 2
        print("Du tar extra damage")
    elif (ability == "shield"):
        protection = 1
        print("Du bruker shield og vil miste mindre liv")
    if (ability != ""):
        ability_counter += 1

    damage = random.randint(15*extra_damage, 25*extra_damage)
    hoved_damage = random.randint(5*protection, 10*protection)
    print("Monsteret mister", damage, "liv")
    print("Du mister", hoved_damage, "liv")
    monstere[level].lose_hp(damage)
    hovedkarakter.lose_hp(hoved_damage)
    
    if (monstere[level].hp <= 0):
        monstere[level].hp = 0
    if (hovedkarakter.hp <= 0):
        hovedkarakter.hp = 0

    print("Din hp:", hovedkarakter.hp, "Monsterets hp:", monstere[level].hp)

    if (monstere[level].hp == 0):
        if (level == 2):
            print("Nice, du vant!")
            exit()
        print("RIP", monstere[level].navn, "døde")
        level += 1
        start_line = False

    if (hovedkarakter.hp == 0):
        print("You dead.", monstere[level].navn+":", "'Noob'")
        exit()

    
