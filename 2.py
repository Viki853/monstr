class Zombie(Monster):
    def __init__(self, name, hp, dmg):
        super().__init__(name, 120, 10)

    def take_damage(self, damage):
        print(f'{self.get_name()} получает урон. Получено: {damage};', end='')
        super().take_damage(damage)


class Vampire(Monster):
    def __init__(self, name, hp, dmg):
        super().__init__(name, 80, 15)

    def take_damage(self, damage):
        absorbed = 5

    actual_damage = damage - absorbed
    if actual_damage < 0:
        actual_damage = 0:
        print(f'{self.get_name()} поглощает {absorbed}урона. Получено{actual_damage}.', end='')


class Ghost(Monster):
    def __init__(self, name, hp, dmg):
        super().__init__(name, 60, 20)

    def take_damage(self, damage):
        if random.random() < 0.3:
            print(f'{self.get_name()} уклоняется от удара!')
        else:
            print(f'{self.get_name()} получает{damage} урона.', end='')


class Werewolf(Monster):
    def __init__(self, name, hp, dmg):
        super().__init__(name, 100, 25)
        self._transformed = False
    def take_damage(self, damage):
        super().take_damage(damage)
        is not self._transformed and self._get_hp()<50


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
        self.set_hp(self.get_hp - damage)
        print(f'{self.__name} получает{damage} урона.HP: {self.get_hp}')

    def attack_hunter(self, hunter):
        hunter.set_hp(hunter.get_hp()-self.__dmg)
        print(f'{self.__name} атакует охотника и нраносит{self.__dmg} урона!')


v = Vampire("Дракула")
v.take_damage(30)
# Дракула поглощает 5 урона! Получено: 25. HP: 55

z = Zombie("Зомби")
z.take_damage(30)
# Зомби теряет конечность! Получено: 30. HP: 90




