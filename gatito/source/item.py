import pygame
from sprite_strip_anim import SpriteStripAnim
from settings import TILE_SIZE


class Item(pygame.sprite.Sprite):
    def __init__(self, itemname: str, topleft: tuple[int], frames: int = 1,
                 *groups: pygame.sprite.AbstractGroup) -> None:
        super().__init__(*groups)

        self.animation = SpriteStripAnim(
            f'/gatito/assets/sprites/itens/{itemname}',
            (topleft, (TILE_SIZE, TILE_SIZE)), frames=frames, loop=True)
