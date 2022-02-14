from enum import Enum

class Level(Enum):
    INFO = 0
    WARN = 1
    ERR = 2

class Log(object):
    @staticmethod
    def print(level: Level, msg: str) -> None:
        match level:
            case Level.INFO:
                print(f"INFO: {msg}")

            case Level.WARN:
                print(f"WARN: {msg}")

            case Level.ERR:
                print(f"ERROR: {msg}")