import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, type: str, topleft: tuple[int],
                 *groups: pygame.sprite.AbstractGroup,
                 opacity: float = 1) -> None:
        super().__init__(*groups)

        self.image = pygame.image.load(
            f'gatito/assets/sprites/tiles/{type}').convert()
        self.rect = self.image.get_rect()


# class WaterTile(pygame.sprite.Sprite):
#     def __init__(self, watertype: str, topleft: tuple[int],
#                  *groups: pygame.sprite.AbstractGroup) -> None:
#         super().__init__(*groups)

#         self.animation = SpriteStripAnim(f'/gatito/assets/sprites/tiles/water/{watertype}', (0, 0, 16, 16), True)
