import random


class Arena:
	def __init__(self, fighter1, fighter2):
		self.fighter1 = fighter1
		self.fighter2 = fighter2

	def __str__(self):
		return str(self.fighter1), str(self.fighter2)

	def select_defender(self):
		"""
		:return: randomly select a defender
		"""
		fighters = (self.fighter1, self.fighter2)
		return random.choice(fighters)

	def fight(self, first_fighter, second_fighter):
		while first_fighter.lives > 0 and second_fighter.lives > 0:
			defender = self.select_defender()
			print(f"Defender is: {defender.name}")
			if first_fighter == defender:
				second_fighter.attack(first_fighter)
			else:
				first_fighter.attack(second_fighter)
