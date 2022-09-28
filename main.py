from monster import Monster, Hoved

level = 0

m = Monster()
main_hp = 20
print("Welcome to dungeons and dragons")

monster1 = m("bill gates", 80, "hack")
monster2 = m("jeff bezos", 120, "steal")
monster3 = m("elon musk", 150, "flamethrower")

while True:
    if (level == 0):
        print("Jeg er", monster1.navn, "Jeg kommer til å eliminere deg med min windows AI")
    
    angrep = input("Velg angrep: attack, heal")
    if (angrep == "attack"):
        monster1.lose_hp(20)
    elif (angrep == "heal"):
        hovedkarakter.heal(15)
    if (hovedkarakter.hp <= 0)
        print("You dead")
        exit()