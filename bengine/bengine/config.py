

class Config(object):
    _debug: bool = True
    _wireframe: bool = False

    @staticmethod
    def get_debug() -> bool:
        return Config._debug

    @staticmethod
    def set_debug(debug: bool) -> None:
        Config._debug = debug

    @staticmethod
    def get_wireframe() -> bool:
        return Config._wireframe

    @staticmethod
    def set_wireframe(wireframe: bool) -> None:
        Config._wireframe = wireframe