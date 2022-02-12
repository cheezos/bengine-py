import bengine

from bengine.entity import Entity

class Main(bengine.Game):
    def __init__(self) -> None:
        bengine.init(self)

    def on_init(self) -> None:
        print("init")

        ent = Entity()

    def on_update(self, delta_time: float) -> None:
        pass

    def on_quit(self) -> None:
        pass

if __name__ == '__main__':
    main = Main()