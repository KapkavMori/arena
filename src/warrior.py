from fighter import Fighter
import random


class Warrior(Fighter):
	def __init__(self, name: str, lives=150, power_of_attack=20, shield=50):
		super().__init__(name, lives, power_of_attack)
		self.shield = shield

	def __str__(self):
		return int(self.shield)

	def shield_raise(self):
		"""
		:return: randomly determines if the warrior raises his shield
				 0 = no, 1 = yes
		"""
		return random.randint(0, 1)

	def have_shield(self, fighter):
		if self.shield > 0:
			fighter.lives += self.shield
