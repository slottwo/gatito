import pygame

pygame.init()
DEBUG_SIZE = 16
font = pygame.font.SysFont('FiraCode', DEBUG_SIZE)


def debug(*info: any, y=1, x=1) -> None:
    # get the screen to draw
    display_surface = pygame.display.get_surface()

    # renderize the text
    debug_surface = font.render(' '.join(map(str, info)), True, 'White')

    # set position
    debug_rect = debug_surface.get_rect(
        topleft=(x * DEBUG_SIZE, y * DEBUG_SIZE))

    # draw a black bg
    pygame.draw.rect(display_surface, 'Black', debug_rect)

    # draw the text
    display_surface.blit(debug_surface, debug_rect)
