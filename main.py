from src.warrior import Warrior
from src.arena import Arena

if __name__ == "__main__":
    player_1 = Warrior("Amanda")
    player_2 = Warrior("Bob")
    arena = Arena(player_1, player_2)
    arena.fight(player_1, player_2)
