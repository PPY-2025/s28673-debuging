class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = int(hp)

    def take_damage(self, amount):
        self.hp -= int(amount)
        if self.hp < 0:
            self.hp = 0

class Warrior(Character):
    def __init__(self, name, hp, strength):
        super().__init__(name, hp)
        self.strength = strength

    def attack(self, target):
        damage = int(self.strength * 1.5)
        target.take_damage(damage)

class Mage(Character):
    def __init__(self, name, hp, mana):
        super().__init__(name, hp)
        self.mana = mana

    def attack(self, target):
        if self.mana >= 10:
            target.take_damage(25)
            self.mana -= 10
        else:
            print("Not enough mana!")

def simulate_battle():
    w = Warrior("Thorgal", 100, 10)
    m = Mage("Merlin", 60, 20)

    print("Start:", w.hp, m.hp)
    w.attack(m)
    m.attack(w)
    m.attack(w)
    m.attack(w)
    m.attack(w)
    print("End:", w.hp, m.hp)
#testy
    assert m.hp == 45, "Mage HP should be 45 after one hit"
    assert w.hp == 50, "Warrior HP should be 25 after three hits"
    assert m.mana == 0, "Mage mana should be 0 after 3 attacks"
simulate_battle()

