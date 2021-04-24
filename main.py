from game import Game
from user_input import UserInput

player_name = UserInput.get_player_warrior_name()
enemy_name = UserInput.get_enemy_warrior_name()
max_health = UserInput.get_warriors_max_health()

if __name__ == "__main__":
    game = Game(player_name, enemy_name, max_health)
    game.start()
