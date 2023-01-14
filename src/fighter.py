class Fighter:
    def __init__(self, name: str, lives: int, power_of_attack: int):
        self.name = name
        self.lives = lives
        self.power_of_attack = power_of_attack

    def __str__(self):
        return str(self.name), int(self.lives), int(self.power_of_attack)

    def verify_life_status(self):
        if self.lives < 1:
            return False

    def attack(self, defender):
        defender.lives -= self.power_of_attack
        print(f"{defender.name} have {defender.lives} lives.")
