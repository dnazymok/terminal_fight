from random import randint
from warrior import Warrior
from user_input import UserInput
from time import sleep


class Fight:
    def __init__(self, player_warrior_name, enemy_warrior_name, health):
        self.player_warrior = Warrior(player_warrior_name, health)
        self.enemy_warrior = Warrior(enemy_warrior_name, health)
        self.max_health = health

    def start(self):
        while True:
            turn = randint(1, 2)  # turn 1 is a player, turn 2 is a enemy
            if turn == 1:
                sleep(2)
                self.player_warrior.do_random_action(self.enemy_warrior)
                if self.enemy_warrior.health <= 0:
                    print(f"{self.player_warrior.name} победил!")
                    break
                elif self.enemy_warrior.health <= self.max_health * 0.35:
                    self.enemy_warrior.increase_heal_chance()
            elif turn == 2:
                sleep(2)
                self.enemy_warrior.do_random_action(self.player_warrior)
                if self.player_warrior.health <= 0:
                    print(f"{self.enemy_warrior.name} победил!")
                    break


player_name = UserInput.get_player_warrior_name()
enemy_name = UserInput.get_enemy_warrior_name()
max_health = UserInput.get_warriors_max_health()

if __name__ == "__main__":
    fight = Fight(player_name, enemy_name, max_health)
    fight.start()
