import time
import bengine

class Main:
    def __init__(self) -> None:
        bengine.init(lambda : self.init())

        self.update()

    def init(self) -> None:
        pass

    def update(self) -> None:
        while bengine.Window.get_window():
            print("swag")

if __name__ == '__main__':
    main = Main()