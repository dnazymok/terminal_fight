from random import randint
from warrior import Warrior
from time import sleep


class Game:
    def __init__(self, player_warrior_name, enemy_warrior_name, health):
        self.player_warrior = Warrior(player_warrior_name, health)
        self.enemy_warrior = Warrior(enemy_warrior_name, health)
        self.max_health = health

    def start(self):
        """Game loop. Breaks if player or enemy turn ends in victory"""
        while True:
            turn = randint(1, 2)  # turn 1 is a player, turn 2 is a enemy
            if turn == 1:
                if self.player_turn() == "Win":
                    break
            elif turn == 2:
                if self.enemy_turn() == "Win":
                    break

    def player_turn(self):
        sleep(2)
        self.player_warrior.do_random_action(self.enemy_warrior)
        self.display_fight_status()
        if self.is_enemy_dead():
            print(f"{self.player_warrior.name} победил!")
            return "Win"
        elif self.is_enemy_health_low():
            self.enemy_warrior.increase_heal_chance()

    def enemy_turn(self):
        sleep(2)
        self.enemy_warrior.do_random_action(self.player_warrior)
        self.display_fight_status()
        if self.is_player_dead():
            print(f"{self.enemy_warrior.name} победил!")
            return "Win"

    def is_player_dead(self):
        return self.player_warrior.health <= 0

    def is_enemy_dead(self):
        return self.enemy_warrior.health <= 0

    def is_enemy_health_low(self):
        """Checks if health is below 35%"""
        return self.enemy_warrior.health <= self.max_health * 0.35

    def display_fight_status(self):
        print(
            f"----- {self.player_warrior.name}: {self.player_warrior.health}, "
            f"{self.enemy_warrior.name}: {self.enemy_warrior.health} -----", "\n")

