from enum import Enum


class Command(Enum):
    NONE = 0
    READ = 1
    CREATE = 2
    UPDATE = 3
    LIST = 4
    LISTENG = 7
    DELETE = 5 # добавили новую команду 
    EXIT = 6