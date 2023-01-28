
class World:

    def __init__(self, x: int, y: int):
        self.__world = []
        for i in range(x):
            row = []
            for j in range(y):
                row.append(Cell(str(i) + ":" + str(j)))
            self.__world.append(row)

    def __str__(self):
        ret = ""
        for row in self.__world:
            tmp = ""
            for cell in row:
                tmp = tmp + " " + str(cell)
            ret = ret + tmp + "\n"

        return ret

    def set_item(self, item, x: int, y: int):
        cell = self.__world[x][y]
        cell.set_item(item)

    def get_item(self, x: int, y: int):
        item = self.__world[x][y].get_item()
        return item


class Cell:

    def __init__(self, name: str):
        self.__contains = None
        self.__name = name

    def __str__(self):
        return "[" + str(self.__contains) + "]"

    @property
    def contains(self):
        return self.__contains

    def set_item(self, item):
        print("Set: " + str(item))
        self.__contains = item

    def get_item(self):
        return self.__contains
