import random


class UserInput:
    player_names_list = ['Геральт', 'Иллидан', 'Джонни Кейдж', 'Рейнор', 'Эцио', "Тралл", "Гордон Фримен"]
    enemy_names_list = ['Эредин', 'Шао Кан', 'Артас', 'Джокер', 'Лео Бонарт', "Хедкраб", "Тайкус"]

    @staticmethod
    def get_player_warrior_name():
        """Asks the user for a warrior name and return it"""
        player_warrior_name = input("Дайте имя вашему персонажу: (или random если хотите случайное)").strip()
        if player_warrior_name.strip().lower() == "random":
            player_warrior_name = random.choice(UserInput.player_names_list)
        return player_warrior_name

    @staticmethod
    def get_enemy_warrior_name():
        """Return enemy warrior name from list"""
        return random.choice(UserInput.enemy_names_list)

    @staticmethod
    def get_warriors_max_health():
        """Return warriors health"""
        while True:
            try:
                health = int(input("Сколько у бойцов будет здоровья? (Рекомендуемое значение 50-100)"))
                return health
            except ValueError:
                continue

