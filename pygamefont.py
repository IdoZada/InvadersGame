import pygame, os, sys


class FontType:

    def __init__(self, fontName, fontSize, color):
        self.font = pygame.font.SysFont(fontName, fontSize)
        self.color = color

    def draw(self, surface, msg, x, y):
         title_text = self.font.render(msg, True, self.color)
         width = title_text.get_width()
         height = title_text.get_height()
         surface.blit(title_text, (x, y, width, height))

    def centre(self, surface, msg, distance_for_top):
        title_text = self.font.render(msg, True, self.color)
        half_width = surface.get_rect().width / 2
        surface.blit(title_text, (half_width - title_text.get_width() // 2, distance_for_top))


