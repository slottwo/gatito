from os import walk
from os.path import join
import pygame


def import_folder(path: str) -> list[pygame.Surface]:
    surface_list = []

    for _, __, files in walk(path):
        for img in files:
            surface_list.append(
                pygame.image.load(join(path, img)).convert_alpha()
            )

    return surface_list


def scale(sprite: pygame.Surface, ratio: int):
    new_size = [ratio * i for i in sprite.get_size()]
    return pygame.transform.scale(sprite, new_size)
