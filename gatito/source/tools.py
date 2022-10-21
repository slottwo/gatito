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


# debug
if __name__ == '__main__':
    print(import_folder('gatito/assets/graphics/character/left_fall'))
