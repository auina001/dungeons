main_hp = 100

class Hoved():
    def __init__(self,navn,hp,ab1,ab2):
        self.navn=navn
        self.hp=hp
    
    def heal(self):
        self.hp += 10

    def lose_hp(self, damage):
        self.hp -= damage

hovedkarakter = Hoved("kjetil", 100)

class Monster():
    def __init__(self,navn,hp,ab1):
        self.navn=navn
        self.hp=hp
        self.ab1=ab1

    def abilities(self):
        if (self.ab1 == "steal"):
            hovedkarakter.lose_hp(20)
        elif (self.ab1 == "hack"):
            hovedkarakter.lose_hp(15)
        elif (self.ab1 == "flamethrower"):
            hovedkarakter.lose_hp(25)

    def lose_hp(self, damage):
        self.hp -= damage





