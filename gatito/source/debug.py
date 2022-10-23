import pygame

pygame.init()
font = pygame.font.SysFont('FiraCode', 16)


def debug(info: any, pos: tuple[int] = (10, 10)) -> None:
    display_surface = pygame.display.get_surface()
    debug_surface = font.render(str(info), True, 'White')
    debug_rect = debug_surface.get_rect(topleft=(pos[0], pos[1]))
    pygame.draw.rect(display_surface, 'Black', debug_rect)
    display_surface.blit(debug_surface, debug_rect)
