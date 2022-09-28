class Hoved():
    def __init__(self,navn,hp):
        self.navn = navn
        self.hp = hp
    
    def heal(self, healing):
        self.hp += healing

    def lose_hp(self, damage):
        self.hp -= damage


class Monster():
    def __init__(self,navn,hp,line):
        self.navn = navn
        self.hp = hp
        self.line = line

    def lose_hp(self, damage):
        self.hp -= damage





