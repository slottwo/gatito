from json import load
from tile import Tile
from item import Item
from player import Player
from settings import *


class Map:
    def __init__(self, id: int, level) -> None:
        with open(f'gatito/assets/tilemaps/{id}.json') as file:
            self.data: dict = load(file)

        for layer in self.data['layers']:
            if layer['visible']:
                if layer['type'] == 'tilelayer':
                    self.load_blocks(layer['data'])
                elif layer['type'] == 'objectgroup':
                    self.load_entities(layer['objects'])

    def load_blocks(self, data: list):
        for index, id in enumerate(data):
            yield TILE_DICT[id], (int(index % SCREEN_WIDTH) * TILE_SIZE,
                                  int(index / SCREEN_WIDTH) * TILE_SIZE)

    def load_entities(self, objects: list[dict]):
        ...
