import random

class Monster:
    def __init__(self, name, hp, dmg):
        self.__name = name
        self.__hp = hp
        self.__dmg = dmg

    def get_name(self):
        return self.__name

    def get_hp(self):
        return self.__hp

    def get_dmg(self):
        return self.__dmg

    def set_hp(self, value):
        if value < 0:
            self.__hp = 0
        else:
            self.__hp = value

    def is_alive(self):
        return self.__hp > 0

    def show_status(self):
        print('Имя:', self.get_name())
        print('HP: ', self.get_hp())

    def take_damage(self, damage):
        self.set_hp(self.get_hp() - damage)
        print(f'HP: {self.get_hp()}')

    def attack_hunter(self, hunter):
        hunter.set_hp(hunter.get_hp() - self.__dmg)
        print(f'{self.__name} атакует охотника и наносит {self.__dmg} урона!')


class Zombie(Monster):
    def __init__(self, name):
        super().__init__(name, 120, 10)

    def take_damage(self, damage):
        print(f'{self.get_name()} теряет конечность! Получено: {damage}. ', end='')
        super().take_damage(damage)


class Vampire(Monster):
    def __init__(self, name):
        super().__init__(name, 80, 15)

    def take_damage(self, damage):
        absorbed = 5
        actual_damage = damage - absorbed
        if actual_damage < 0:
            actual_damage = 0
        print(f'{self.get_name()} поглощает {absorbed} урона! Получено: {actual_damage}. ', end='')
        super().take_damage(actual_damage)


class Ghost(Monster):
    def __init__(self, name):
        super().__init__(name, 60, 20)

    def take_damage(self, damage):
        if random.random() < 0.3:
            print(f'{self.get_name()} уклоняется от удара!')
        else:
            print(f'{self.get_name()} получает {damage} урона. ', end='')
            super().take_damage(damage)


class Werewolf(Monster):
    def __init__(self, name):
        super().__init__(name, 100, 25)
        self._transformed = False

    def take_damage(self, damage):
        super().take_damage(damage)
        if not self._transformed and self.get_hp() < 50:
            self._transformed = True
            print(f'{self.get_name()} трансформируется!')

class Weapon:
    def __init__(self, name):
        self.name = name

    def use(self, monster):
        # Базовый метод, который будет переопределен в дочерних классах
        pass


class SilverSword(Weapon):
    def __init__(self):
        super().__init__("Серебряный меч")

    def use(self, monster):
        damage = 30
        print(f"Атака оружием {self.name} по {monster.get_name()}! ", end="")
        monster.take_damage(damage)


class HolyWater(Weapon):
    def __init__(self):
        super().__init__("Святая вода")

    def use(self, monster):
        damage = 20
        print(f"Применение оружия {self.name} против {monster.get_name()}! ", end="")
        monster.take_damage(damage)


class CrossbowBolt(Weapon):
    def __init__(self):
        super().__init__("Арбалет с болтом")

    def use(self, monster):
        damage = 25
        print(f"Выстрел из оружия {self.name} в {monster.get_name()}! ", end="")
        monster.take_damage(damage)


class Hunter:
    def __init__(self, name):
        self.__name = name
        self.__hp = 100
        self.__weapons = []  # Приватный инвентарь (список оружия)

    def get_name(self):
        return self.__name

    def get_hp(self):
        return self.__hp

    def set_hp(self, value):
        if value < 0:
            self.__hp = 0
        else:
            self.__hp = value

    def is_alive(self):
        return self.__hp > 0

    def add_weapon(self, weapon):
        self.__weapons.append(weapon)

    def show_inventory(self):
        if not self.__weapons:
            print("Инвентарь пуст")
            return
        print("Арсенал охотника:")
        # enumerate(..., 1) выводит нумерацию оружия, начиная с 1
        for index, weapon in enumerate(self.__weapons, 1):
            print(f"{index}. {weapon.name}")

    def attack(self, weapon_index, monster):
        # Проверяем корректность переданного индекса (переводим из 1-нумерации в 0-индекс)
        actual_index = weapon_index - 1
        if 0 <= actual_index < len(self.__weapons):
            chosen_weapon = self.__weapons[actual_index]
            # Вызываем метод use() у выбранного оружия
            chosen_weapon.use(monster)
        else:
            print("Оружие с таким номером не найдено в инвентаре!")

######################################################################################################

def run_game():
    print("=== НАЧАЛО ИГРЫ ===")
    # 1. Создаем Охотника и выдаем ему оружие
    hunter = Hunter("Ван Хельсинг")
    hunter.add_weapon(SilverSword())
    hunter.add_weapon(HolyWater())
    hunter.add_weapon(CrossbowBolt())

    # 2. Создаем список из 4 монстров
    monsters = [
        Zombie("Зомби-работяга"),
        Vampire("Граф Дракула"),
        Ghost("Бесплотный Дух"),
        Werewolf("Люкан")
    ]

    # Игровой цикл: Охотник сражается с монстрами по очереди
    for monster in monsters:
        print(f"\n На пути встает новый враг: {monster.get_name()} ({monster.get_hp()} HP)!")

        round_num = 1
        # Бой идет, пока оба живы
        while monster.is_alive() and hunter.is_alive():
            print(f"\n--- Раунд {round_num} ---")

            # Шаг 1: Охотник атакует случайным оружием из инвентаря (индексы от 1 до 3)
            weapon_index = random.randint(1, 3)
            hunter.attack(weapon_index, monster)

            # Шаг 2: Если монстр выжил, он атакует в ответ
            if monster.is_alive():
                monster.attack_hunter(hunter)
            else:
                print(f" {monster.get_name()} повержен!")

            # Шаг 3: Вывод статуса Охотника после раунда
            print(f"Статус Охотника: {hunter.get_name()} | HP: {hunter.get_hp()}")

            round_num += 1

        # Если Охотник погиб, прерываем прохождение
        if not hunter.is_alive():
            print(f"\n {hunter.get_name()} погиб в бою с {monster.get_name()}...")
            break

    # 3. Вывод итогового сообщения игры
    print("\n=== КОНЕЦ ИГРЫ ===")
    if hunter.is_alive():
        print(" ПОБЕДА! Охотник уничтожил всех монстров и очистил эти земли!")
    else:
        print(" ПОРАЖЕНИЕ! Тьма поглотила этот мир...")


# Точка входа для запуска игры
run_game()
