import bengine

class Main(bengine.Game):
    def __init__(self) -> None:
        bengine.init(self)

    def on_init(self) -> None:
        print("init")

    def on_update(self, delta_time: float) -> None:
        pass

    def on_quit(self) -> None:
        pass

if __name__ == '__main__':
    main = Main()