from world import World


class Ploppa:

    cnt = 0
    all = []

    def __init__(self, x, y, world: World):
        self.__x = x
        self.__y = y
        self.__world = world
        self.__name = "Ploppa:" + str(Ploppa.cnt)
        Ploppa.cnt = Ploppa.cnt + 1
        Ploppa.all.append(self)

    def __str__(self):
        return self.__name

    def do_action(self):
        ret = self.__move(0, 1)
        print(ret)

    def __move(self, delta_x: int, delta_y: int):
        new_x = self.__x + delta_x
        new_y = self.__y + delta_y
        old_cell = self.__world.get_item(self.__x, self.__y)
        move_cell = self.__world.get_item(new_x, new_y)
        if move_cell is None:
            self.__world.set_item(old_cell, new_x, new_y)
            self.__world.set_item(None, self.__x, self.__y)
            self.__x = new_x
            self.__y = new_y
            return True
        else:
            return False

    def __move_to(self, x: int, y: int):
        pass
