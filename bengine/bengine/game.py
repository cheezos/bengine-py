import os

class Game:
    def __init__(self, root_directory: str) -> None:
        self.root_directory = root_directory 
        print(self.root_directory)

    def init(self) -> None: pass
    def update(self, delta_time: float) -> None: pass
    def quit(self) -> None: pass