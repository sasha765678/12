#!/usr/bin/env python3

import random
import pygame
import os
import sys
import time


def nachalo():
    global screen, startx, starty, all_sprites, tiles_group, player_group, fin_group, \
        sloi_lab, my_index, tile_width, tile_height, level_x, level_y, level_in_txt, \
        player, vse_yrovne, index_yrovna

    if index_yrovna < len(vse_yrovne):
        screen.fill((0, 0, 0))
        pygame.display.flip()
        startx, starty = None, None
        all_sprites = pygame.sprite.Group()
        tiles_group = pygame.sprite.Group()
        player_group = pygame.sprite.Group()
        fin_group = pygame.sprite.Group()

        sloi_lab = vse_yrovne[index_yrovna]
        my_index = 0

        tile_width = tile_height = 50
        level_x, level_y, startx, starty = generate_level(load_level(sloi_lab[my_index]))

        level_in_txt = load_level(sloi_lab[my_index])
        # ----------------
        player = pygame.sprite.Sprite(all_sprites)
        player.image = player_image
        player.rect = player.image.get_rect()
        all_sprites.add(player)
        player_group.add(player)
        startx, starty = starty, startx
        player.rect.top += startx * tile_width
        player.rect.left += starty * tile_height

        index_yrovna += 1

        with open("chfgh/proekt/data/" + 'index_yrovna.txt', 'w') as f:
            f.write(str(index_yrovna))

        pygame.display.flip()

    else:
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 50)
        text = font.render("!!!победа!!!", True, (100, 255, 100))
        text_x = width // 2 - text.get_width() // 2
        text_y = height // 2 - text.get_height() // 2
        text_w = text.get_width()
        text_h = text.get_height()
        screen.blit(text, (text_x, text_y))
        pygame.draw.rect(screen, (0, 255, 0), (text_x - 10, text_y - 10,
                                               text_w + 20, text_h + 20), 1)

        pygame.display.flip()

        with open("chfgh/proekt/data/" + 'index_yrovna.txt', 'w') as f:
            f.write(str(1))

        while True:  # главный игровой цикл
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    print('bsdlfhvbld')


def my_menu():
    global menu_img

    screen.fill((0, 0, 0))
    screen.blit(menu_img, (80, 100))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            break;


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)
        self.tile_type = tile_type
        if self.tile_type == 'tyr':
            self.pos_tyr = (pos_x, pos_y)

    def update(self):
        global dead_img
        if pygame.sprite.spritecollideany(self, player_group) and self.tile_type == 'finish':
            nachalo()

        if pygame.sprite.spritecollideany(self, player_group) and self.tile_type == 'tyr':
            global index_yrovna

            screen.fill((0, 0, 0))
            # выводит надпись смерть
            # font = pygame.font.Font(None, 50)
            # text = font.render("!!!смерть!!!", True, (255, 100, 100))
            # text_x = width // 2 - text.get_width() // 2
            # text_y = height // 2 - text.get_height() // 2
            # text_w = text.get_width()
            # text_h = text.get_height()
            # screen.blit(text, (text_x, text_y))
            # pygame.draw.rect(screen, (250, 0, 0), (text_x - 10, text_y - 10,
            #                                        text_w + 20, text_h + 20), 1)

            screen.blit(dead_img, (50, 50))
            pygame.display.flip()

            time.sleep(3)

            index_yrovna -= 1
            nachalo()

        if pygame.sprite.spritecollideany(self, player_group) and \
                (self.tile_type == 'tyr1' or self.tile_type == 'tyr2'):
            screen.fill((0, 0, 0))
            #пришеть смерть
            # font = pygame.font.Font(None, 50)
            # text = font.render("!!!смерть!!!", True, (255, 100, 100))
            # text_x = width // 2 - text.get_width() // 2
            # text_y = height // 2 - text.get_height() // 2
            # text_w = text.get_width()
            # text_h = text.get_height()
            # screen.blit(text, (text_x, text_y))
            # pygame.draw.rect(screen, (250, 0, 0), (text_x - 10, text_y - 10,
            #                                        text_w + 20, text_h + 20), 1)


            screen.blit(dead_img, (50, 50))

            pygame.display.flip()

            time.sleep(3)

            index_yrovna -= 1
            nachalo()


def load_level(filename):
    filename = "chfgh/proekt/data/" + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    # и подсчитываем максимальную длину
    max_width = max(map(len, level_map))

    # дополняем каждую строку пустыми клетками ('.')
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


def generate_level(level):
    x, y = None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                posx, posy = x, y
            elif level[y][x] == '!':
                Tile('empty', x, y)
                Tile('finish', x, y)
            elif level[y][x] == '$':
                Tile('empty', x, y)
                Tile('tyr', x, y)
            elif level[y][x] == '-':
                Tile('empty', x, y)
                Tile('tyr1', x, y)
            elif level[y][x] == '|':
                Tile('empty', x, y)
                Tile('tyr2', x, y)

    # вернем игрока, а также размер поля в клетках
    if not (startx is None):
        posx, posy = startx, starty

    return x, y, posx, posy


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
        fullname = os.path.join('chfgh/proekt/data/', name)
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
            image = pygame.transform.scale(image, (50, 50))

        else:
            image = pygame.transform.scale(image, (width, height))

        return image


class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dx = 0
        self.dy = 0

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - width // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - height // 2)


def sloi():
    global my_index, startx, starty, level_in_txt
    global all_sprites, tiles_group
    if my_index == len(sloi_lab) - 1:
        my_index = 0
    else:
        my_index += 1

    level_in_txt = load_level(sloi_lab[my_index])
    if level_in_txt[startx][starty] != '#':
        screen.fill((0, 0, 0))

        all_sprites = pygame.sprite.Group()
        tiles_group = pygame.sprite.Group()

        level_x, level_y, startx, starty = generate_level(load_level(sloi_lab[my_index]))

        player.image = player_image
        player.rect = player.image.get_rect()
        all_sprites.add(player)
        player_group.add(player)
        player.rect.top += startx * tile_width
        player.rect.left += starty * tile_height

        all_sprites.update()
    else:
        if my_index == 0:
            my_index = len(sloi_lab) - 1
        else:
            my_index -= 1

        level_in_txt = load_level(sloi_lab[my_index])


# class Knop1(pygame.sprite.Sprite):
#     def __init__(self, group):
#         super().__init__(group)
#         self.image = Board.load_image('7.png')
#         self.rect = self.image.get_rect()
#         self.rect.x = 100
#         self.rect.y = 100
#
#     def update(self, *args):
#         if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
#                 self.rect.collidepoint(args[0].pos):
#
#             print('продолжить игру')
#
#
# class Knop2(pygame.sprite.Sprite):
#     def __init__(self, group):
#         # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
#         # Это очень важно !!!
#         super().__init__(group)
#         self.image = Board.load_image('4.jpg')
#         self.rect = self.image.get_rect()
#         self.rect.x = 350
#         self.rect.y = 250
#
#     def update(self, *args):
#         if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
#                 self.rect.collidepoint(args[0].pos):
#
#             print('новая игра')


if __name__ == '__main__':
    pygame.init()
    size = width, height = 1920, 1080
    screen = pygame.display.set_mode(size)
    pygame.display.flip()
    fps = 15  # количество кадров в секунду
    clock = pygame.time.Clock()
    running = True
    tile_images = {
        'wall': Board.load_image('fonn.jpg'),
        'empty': Board.load_image('14.jpg'),
        'finish': Board.load_image('star.jpg'),
        'tyr': Board.load_image('trel.png'),
        'tyr1': Board.load_image('45.png'),
        'tyr2': Board.load_image('44.png')
    }

    player_image = Board.load_image('skel2.png')

    vse_yrovne = [['1.txt', '2.txt'], ['3.txt', '4.txt', '5.txt'], ['6.txt', '7.txt', '8.txt', '9.txt', '10.txt'], ['11.txt', '12.txt', '13.txt']]

    with open("chfgh/proekt/data/" + 'index_yrovna.txt', 'r') as f:
        index_yrovna = int(f.readline())
    index_yrovna -= 1

    camera = Camera()

    #dead_img = Board.load_image('смерть.jpg')
    dead_img = pygame.image.load('chfgh/proekt/data/смерть.png').convert_alpha()
    dead_img = pygame.transform.scale(dead_img, (width // 1.1, height // 1.1))

    menu_img = pygame.image.load('chfgh/proekt/data/my_game_menu.png').convert_alpha()
    menu_img = pygame.transform.scale(menu_img, (width // 1.3, height // 1.3))

    dark_img = pygame.image.load('chfgh/proekt/data/shadow.png').convert_alpha()
    dark_img = pygame.transform.scale(dark_img, (size))

    screensaver_img = pygame.image.load('chfgh/proekt/data/Header.png').convert_alpha()
    screensaver_img = pygame.transform.scale(screensaver_img, (size))
    screen.blit(screensaver_img, (0, 0))
    pygame.display.flip()
    time.sleep(3)


    nachalo()


    while running:  # главный игровой цикл
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                sloi()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_F5:
                index_yrovna -= 1
                nachalo()

            # print()
            # print()
            # print()
            # for i in level_in_txt:
            #     print(*i)
            # print(startx, starty)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                if level_in_txt[startx - 1][starty] != '#':
                    player.rect.top -= tile_width
                    startx -= 1
                    player_group.update()
                    player_image = Board.load_image('skel1.png')

            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                if level_in_txt[startx + 1][starty] != '#':
                    player.rect.top += tile_width
                    startx += 1
                    player_image = Board.load_image('skel2.png')

            if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                if level_in_txt[startx][starty - 1] != '#':
                    player.rect.left -= tile_height
                    starty -= 1
                    player_image = Board.load_image('skel3.png')

            if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                if level_in_txt[startx][starty + 1] != '#':
                    player.rect.left += tile_height
                    starty += 1
                    player_image = Board.load_image('skel4.png')
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                my_menu()
                

            player.image = player_image

            all_sprites.update()

        # изменяем ракурс камеры
        camera.update(player);
        # обновляем положение всех спрайтов
        for sprite in all_sprites:
            camera.apply(sprite)

        all_sprites.update()
        all_sprites.draw(screen)
        fin_group.draw(screen)
        player_group.draw(screen)

        screen.blit(dark_img, (0, 0))

        pygame.display.flip()
        clock.tick(fps)
pygame.quit()
