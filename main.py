from src.fighter import Fighter
from src.arena import Arena

if __name__ == "__main__":
	player_1 = Fighter("Amanda")
	player_2 = Fighter("Bob")
	arena = Arena(player_1, player_2)
	arena.fight(player_1, player_2)
