from pprint import pprint

from world import World
from ploppa import Ploppa

world = World(10, 10)


def main():
    # world = World(10, 10)
    world.set_item(Ploppa(1, 1, world), 1, 1)
    # world.set_item(Ploppa(8, 8), 8, 8)
    # world.set_item(Ploppa(2, 8), 2, 8)
    # world.set_item(Ploppa(3, 8), 3, 8)
    print(str(world))

    for i in range(4):
        for p in Ploppa.all:
            p.do_action()
            print(str(world))


if __name__ == "__main__":
    print("Start")
    main()
    print("End")
