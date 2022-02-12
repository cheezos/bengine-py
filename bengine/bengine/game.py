from abc import abstractmethod

class Game:
    @abstractmethod
    def on_init(self) -> None: pass

    @abstractmethod
    def on_update(self, delta_time: float) -> None: pass

    @abstractmethod
    def on_quit(self) -> None: pass