import pygame

pygame.init()
font = pygame.font.SysFont('FiraCode', 12)


def debug(*info: any, y=12, x=12) -> None:
    display_surface = pygame.display.get_surface()
    debug_surface = font.render(' '.join(map(str, info)), True, 'White')
    debug_rect = debug_surface.get_rect(topleft=(x, y))
    pygame.draw.rect(display_surface, 'Black', debug_rect)
    display_surface.blit(debug_surface, debug_rect)
