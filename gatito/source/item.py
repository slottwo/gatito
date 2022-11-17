import pygame
from sprite_strip_anim import SpriteStripAnim


class Item(pygame.sprite.Sprite):
    def __init__(self, itemname: str, topleft: tuple[int],
                 *groups: pygame.sprite.AbstractGroup) -> None:
        super().__init__(*groups)

        self.animation = SpriteStripAnim(f'/gatito/assets/sprites/itens/{itemname}',
                                         (0,0,16,16), 8, loop=True)
        
