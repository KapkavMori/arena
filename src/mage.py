from .fighter import Fighter


class Mage(Fighter):
	def __init__(self, name: str, lives=50, power_of_attack=20, mana=100):
		super().__init__(name, lives, power_of_attack)
		self.mana = mana

	def __str__(self):
		return int(self.mana)
