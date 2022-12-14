from json import load
from settings import *


class Map:
    def __init__(self, id: int, level) -> None:
        with open(f'gatito/assets/tilemaps/{id}.json') as file:
            self.data: dict = load(file)
