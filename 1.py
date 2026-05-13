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

m = Monster("Зомби", 100, 10)
m.show_status()     # [Зомби] HP: 100
m.set_hp(-50)
m.show_status()     # [Зомби] HP: 0
print(m.is_alive()) # False




