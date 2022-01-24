import random
import pygame
import os
import sys
import time


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def load_image(name, colorkey=None, fon=None):
        fullname = os.path.join('data', name)
        if not os.path.isfile(fullname):
            print(f"Файл с изображением '{fullname}' не найден")
            sys.exit()

        if colorkey is not None:
            image = pygame.image.load(fullname).convert()
            transColor = image.get_at((0, 0))
            image.set_colorkey(transColor)
            image = pygame.image.load(fullname).convert()
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey)
        else:
            image = pygame.image.load(fullname)
            image = image.convert_alpha()

        if fon is None:
            return image

        image = pygame.transform.scale(image, (fon))

        return image


def draw(screen, my_text):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    text = font.render(my_text, True, (255, 100, 100))
    screen.blit(text, (10, 10))


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 500
    screen = pygame.display.set_mode(size)
    pygame.display.flip()
    fps = 15  # количество кадров в секунду
    clock = pygame.time.Clock()
    running = True
    all_sprit = pygame.sprite.Group()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw(screen, str(1) + '/' + str(5))
        pygame.display.flip()





















#============================================

    # size1FirstBtn, size2FirstBtn = 500, 100
    # x1Firstbtn, y1Firstbtn = 1280, 100
    # x2Firstbtn, y2Firstbtn = x1Firstbtn + size1FirstBtn, y1Firstbtn + size2FirstBtn
    #
    # knopka1 = pygame.sprite.Sprite(knopks_group)
    # knopka1.image = Board.load_image('NewGame.png', None, (size1FirstBtn, size2FirstBtn))
    # knopka1.rect = knopka1.image.get_rect()
    # knopks_group.add(knopka1)
    # knopka1.rect.top += y1Firstbtn
    # knopka1.rect.left += x1Firstbtn
    #
    # #-----------
    #
    # size1SecBtn, size2SecBtn = 500, 100
    # x1Secbtn, y1Secbtn = 1280, 300
    # x2Secbtn, y2Secbtn = x1Secbtn + size1SecBtn, y1Secbtn + size2SecBtn
    #
    # knopka2 = pygame.sprite.Sprite(knopks_group)
    # knopka2.image = Board.load_image('Rules.png', None, (size1SecBtn, size2SecBtn))
    # knopka2.rect = knopka2.image.get_rect()
    # knopks_group.add(knopka2)
    # knopka2.rect.top += y1Secbtn
    # knopka2.rect.left += x1Secbtn
    # #-----------
    #
    # size1ThirdBtn, size2ThirdBtn = 500, 100
    # x1Thirdbtn, y1Thirdbtn = 1280, 500
    # x2Thirdbtn, y2Thirdbtn = x1Thirdbtn + size1ThirdBtn, y1Thirdbtn + size2ThirdBtn
    #
    # knopka3 = pygame.sprite.Sprite(knopks_group)
    # knopka3.image = Board.load_image('Exit.png', None, (size1ThirdBtn, size2ThirdBtn))
    # knopka3.rect = knopka3.image.get_rect()
    # knopks_group.add(knopka3)
    # knopka3.rect.top += y1Thirdbtn
    # knopka3.rect.left += x1Thirdbtn
    #
    # #----------
    # size1ForthBtn, size2ForthBtn = 100, 100
    # x1Forthbtn, y1Forthbtn = 1280, 800
    # x2Forthbtn, y2Forthbtn = x1Forthbtn + size1ForthBtn, y1Forthbtn + size2ForthBtn
    #
    # knopka4 = pygame.sprite.Sprite(knopks_group)
    # knopka4.image = Board.load_image('VolumePlus.png', None, (size1ForthBtn, size2ForthBtn))
    # knopka4.rect = knopka4.image.get_rect()
    # knopks_group.add(knopka4)
    # knopka4.rect.top += y1Forthbtn
    # knopka4.rect.left += x1Forthbtn
    # #----------
    # size1FiveBtn, size2FiveBtn = 100, 100
    # x1Fivebtn, y1Fivebtn = 1680, 800
    # x2Fivebtn, y2Fivebtn = x1Fivebtn + size1FiveBtn, y1Fivebtn + size2FiveBtn
    #
    # knopka5 = pygame.sprite.Sprite(knopks_group)
    # knopka5.image = Board.load_image('VolumeMinus.png', None, (size1FiveBtn, size2FiveBtn))
    # knopka5.rect = knopka5.image.get_rect()
    # knopks_group.add(knopka5)
    # knopka5.rect.top += y1Fivebtn
    # knopka5.rect.left += x1Fivebtn
    #
    #
    #
    # flag = 0
    #
    # while running:  # главный игровой цикл
    #     screen.fill((0, 0, 0))
    #
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             running = False
    #
    #         if event.type == pygame.MOUSEMOTION:
    #             if x1Firstbtn <= event.pos[0] <= x2Firstbtn and y1Firstbtn <= event.pos[1] <= y2Firstbtn:
    #                 flag = 1
    #                 knopka1.image = Board.load_image('', None, (size1FirstBtn + 5, size2FirstBtn + 5))
    #
    #             elif x1Secbtn <= event.pos[0] <= x2Secbtn and y1Secbtn <= event.pos[1] <= y2Secbtn:
    #                 flag = 2
    #                 knopka2.image = Board.load_image('Rules.png', None, (size1SecBtn + 5, size2SecBtn + 5))
    #
    #             elif x1Thirdbtn <= event.pos[0] <= x2Thirdbtn and y1Thirdbtn <= event.pos[1] <= y2Thirdbtn:
    #                 flag = 3
    #                 knopka3.image = Board.load_image('Exit.png', None, (size1ThirdBtn + 5, size2ThirdBtn + 5))
    #
    #             elif x1Forthbtn <= event.pos[0] <= x2Forthbtn and y1Forthbtn <= event.pos[1] <= y2Forthbtn:
    #                 flag = 4
    #                 knopka4.image = Board.load_image('VolumePlus.png', None, (size1ForthBtn + 5, size2ForthBtn + 5))
    #             elif x1Fivebtn <= event.pos[0] <= x2Fivebtn and y1Fivebtn <= event.pos[1] <= y2Fivebtn:
    #                 flag = 5
    #                 knopka5.image = Board.load_image('VolumeMinus.png', None, (size1FiveBtn + 5, size2FiveBtn + 5))
    #
    #             else:
    #                 if flag == 1:
    #                     knopka1.image = Board.load_image('NewGame.png', None, (size1FirstBtn, size2FirstBtn))
    #                 elif flag == 2:
    #                     knopka2.image = Board.load_image('Rules.png', None, (size1SecBtn, size2SecBtn))
    #                 elif flag == 3:
    #                     knopka3.image = Board.load_image('Exit.png', None, (size1ThirdBtn, size2ThirdBtn))
    #                 elif flag == 4:
    #                     knopka4.image = Board.load_image('VolumePlus.png', None, (size1ForthBtn, size2ForthBtn))
    #                 elif flag == 5:
    #                     knopka5.image = Board.load_image('VolumeMinus.png', None, (size1FiveBtn, size2FiveBtn))
    #                 flag = 0
    #         if event.type == pygame.MOUSEBUTTONDOWN and flag != 0:
    #             if flag == 1:
    #                 print(1)
    #
    #             if flag == 2:
    #                 print(2)
    #
    #             if flag == 3:
    #                 print(3)
    #
    #             if flag == 4:
    #                 print(4)
    #     knopks_group.update()
    #     knopks_group.draw(screen)
    #     pygame.display.flip()
