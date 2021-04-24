import random


class Warrior:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.action_list = [self.light_attack, self.heavy_attack, self.heal]
        print("{} призван. Здоровье: {}".format(self.name, self.health))

    def light_attack(self, enemy):
        """Attack with a small range of damage"""
        enemy.health -= random.randrange(18, 26)
        print(
            f"{self.name} нанес лёгкий удар.")

    def heavy_attack(self, enemy):
        """Attack with a big range of damage"""
        enemy.health -= random.randrange(10, 36)
        print(
            f"{self.name} нанес тяжёлый удар.")

    def heal(self):
        """Increases warrior health"""
        self.health += random.randrange(18, 26)
        print(f"{self.name} исцелился.")

    def do_random_action(self, enemy):
        """Randomly chooses an action from Warrior action list"""
        action = random.choice(self.action_list)
        if action == self.heal:
            self.heal()
        elif action == self.light_attack:
            self.light_attack(enemy)
        elif action == self.heavy_attack:
            self.heavy_attack(enemy)

    def increase_heal_chance(self):
        """Increasing heal chance. Maximum chance is 50%"""
        if self.action_list.count(self.heal) < len(self.action_list) / 2:
            self.action_list.append(self.heal)
