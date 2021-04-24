import random
from time import sleep


class Warrior:
    def __init__(self, name="Геральт", health=100):
        self.name = name
        self.health = health
        print("{} призван. Здоровье: {}".format(self.name, self.health))

    def light_attack(self, enemy):
        enemy.health -= random.randrange(18, 26)
        print("{} нанес легкий удар противнику. {}: {} единиц здоровья".format(self.name, enemy.name, enemy.health))

    def heavy_attack(self, enemy):
        enemy.health -= random.randrange(10, 36)
        print("{} нанес тяжелый удар противнику. {}: {} единиц здоровья".format(self.name, enemy.name, enemy.health))

    def heal(self):
        self.health += random.randrange(18, 26)
        print("{} исцелился. {}: {} единиц здоровья".format(self.name, self.name, self.health))

    def do_random_action(self, enemy):
        choice_list = [self.light_attack, self.heavy_attack, self.heal]
        action = random.choice(choice_list)
        if action == self.heal:
            self.heal()
        elif action == self.light_attack:
            self.light_attack(enemy)
        elif action == self.heavy_attack:
            self.heavy_attack(enemy)


def main():
    first_warrior_name = input("Дайте имя первому бойцу:")
    second_warrior_name = input("Дайте имя второму бойцу:")
    health = int(input("Сколько у бойцов будет здоровья?"))

    first_warrior = Warrior(first_warrior_name, health)
    second_warrior = Warrior(second_warrior_name, health)

    while True:
        sleep(2)
        first_warrior.do_random_action(second_warrior)
        if second_warrior.health <= 0:
            print("{} победил!".format(first_warrior_name))
            break
        second_warrior.do_random_action(first_warrior)
        if first_warrior.health <= 0:
            print("{} победил!".format(second_warrior_name))
            break


if __name__ == "__main__":
    main()
