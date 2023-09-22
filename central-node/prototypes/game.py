# import and init pygame library
import threading
import asyncio
import pygame
import server
import sqlite3
import requests
import os
import time
import syslog
import json

# websocket server initialization

def start_server(loop, future):
    loop.run_until_complete(server.main(future))

def stop_server(loop, future):
    loop.call_soon_threadsafe(future.set_result, None)

loop = asyncio.get_event_loop()
future = loop.create_future()
thread = threading.Thread(target=start_server, args=(loop, future))
thread.start()

# global variables

LINE_1_DATA = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
LINE_2_DATA = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
LINE_3_DATA = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
LINE_4_DATA = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
LINE_5_DATA = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
LINE_6_DATA = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

BOX_SIDE  = 70
BOX_SPACE = 0
BOX_HORIZ = 100
BOX_HORIZ_TEXT = 110
BOX_GOKEI_OFFSET = 10
VALUES_OFFSET = 20

BOX_UE_1 = 0
BOX_UE_2 = 0
BOX_UE_3 = 0
BOX_UE_4 = 0
BOX_UE_5 = 0
BOX_UE_6 = 0
BOX_UE_7 = 0

BOX_SHITA_1 = 0
BOX_SHITA_2 = 0 
BOX_SHITA_3 = 0 
BOX_SHITA_4 = 0 
BOX_SHITA_5 = 0 
BOX_SHITA_6 = 0 
BOX_SHITA_7 = 0

# screen variables

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 128)

X = 1280 # 800    
Y = 720  # 600

# pygame initialization and start

pygame.init()
pygame.fastevent.init()

# screen dimensions
HEIGHT = 320
WIDTH = 480

screen = pygame.display.set_mode((X, Y), 0, 32)
screen.fill((white))

# set up the drawing window
# screen = pygame.display.set_mode([WIDTH, HEIGHT])
color = pygame.Color('blue')
radius = 30
x = int(WIDTH/2)


###### Classes ######


class Pane(object):
    def __init__(self,
            line_1_box_1_ue, line_1_box_2_ue, line_1_box_3_ue, line_1_box_4_ue, line_1_box_5_ue, line_1_box_6_ue, line_1_box_7_ue,
            line_2_box_1_ue, line_2_box_2_ue, line_2_box_3_ue, line_2_box_4_ue, line_2_box_5_ue, line_2_box_6_ue, line_2_box_7_ue,
            line_3_box_1_ue, line_3_box_2_ue, line_3_box_3_ue, line_3_box_4_ue, line_3_box_5_ue, line_3_box_6_ue, line_3_box_7_ue,
            line_4_box_1_ue, line_4_box_2_ue, line_4_box_3_ue, line_4_box_4_ue, line_4_box_5_ue, line_4_box_6_ue, line_4_box_7_ue,
            line_5_box_1_ue, line_5_box_2_ue, line_5_box_3_ue, line_5_box_4_ue, line_5_box_5_ue, line_5_box_6_ue, line_5_box_7_ue,
            line_6_box_1_ue, line_6_box_2_ue, line_6_box_3_ue, line_6_box_4_ue, line_6_box_5_ue, line_6_box_6_ue, line_6_box_7_ue,
            ):

        self.line_1_box_1_ue = LINE_1_DATA[0]
        self.line_1_box_2_ue = LINE_1_DATA[1] # line_1_box_2_ue
        self.line_1_box_3_ue = LINE_1_DATA[2]
        self.line_1_box_4_ue = LINE_1_DATA[3]
        self.line_1_box_5_ue = LINE_1_DATA[4]
        self.line_1_box_6_ue = LINE_1_DATA[5]
        self.line_1_box_7_ue = LINE_1_DATA[6]

        self.line_2_box_1_ue = LINE_2_DATA[0] 
        self.line_2_box_2_ue = LINE_2_DATA[1]
        self.line_2_box_3_ue = LINE_2_DATA[2]
        self.line_2_box_4_ue = LINE_2_DATA[3]
        self.line_2_box_5_ue = LINE_2_DATA[4]
        self.line_2_box_6_ue = LINE_2_DATA[5]
        self.line_2_box_7_ue = LINE_2_DATA[6]

        self.line_3_box_1_ue = LINE_3_DATA[0] 
        self.line_3_box_2_ue = LINE_3_DATA[1]
        self.line_3_box_3_ue = LINE_3_DATA[2]
        self.line_3_box_4_ue = LINE_3_DATA[3]
        self.line_3_box_5_ue = LINE_3_DATA[4]
        self.line_3_box_6_ue = LINE_3_DATA[5]
        self.line_3_box_7_ue = LINE_3_DATA[6]
        # pygame.init()
        # self.font = pygame.font.SysFont('Arial', 25)
        self.display_surface = pygame.display.set_mode((X, Y))
        self.font = pygame.font.Font(os.path.join('/usr/share/fonts/truetype/fonts-japanese-gothic.ttf'), 30)
        pygame.display.set_caption('はま寿司イタズラ防止管理')
        self.screen = pygame.display.set_mode((X, Y), 0, 32)
        self.screen.fill((white))
        pygame.display.update()


    def addRect(self):
        # line
        # self.rect = pygame.draw.rect(self.screen, (black), (200,                           BOX_HORIZ, BOX_SIDE + 30, BOX_SIDE), 2)
        # box
        self.rect = pygame.draw.rect(self.screen, (black), (200 + 2*BOX_SIDE + BOX_SPACE,  BOX_HORIZ, BOX_SIDE, BOX_SIDE), 2)
        self.rect = pygame.draw.rect(self.screen, (black), (200 + 4*BOX_SIDE + BOX_SPACE,  BOX_HORIZ, BOX_SIDE, BOX_SIDE), 2)
        self.rect = pygame.draw.rect(self.screen, (black), (200 + 6*BOX_SIDE + BOX_SPACE,  BOX_HORIZ, BOX_SIDE, BOX_SIDE), 2)
        self.rect = pygame.draw.rect(self.screen, (black), (200 + 8*BOX_SIDE + BOX_SPACE,  BOX_HORIZ, BOX_SIDE, BOX_SIDE), 2)
        self.rect = pygame.draw.rect(self.screen, (black), (200 + 10*BOX_SIDE + BOX_SPACE, BOX_HORIZ, BOX_SIDE, BOX_SIDE), 2)
        self.rect = pygame.draw.rect(self.screen, (black), (200 + 12*BOX_SIDE + BOX_SPACE, BOX_HORIZ, BOX_SIDE, BOX_SIDE), 2)
        self.rect = pygame.draw.rect(self.screen, (black), (200 + 14*BOX_SIDE + BOX_SPACE, BOX_HORIZ, BOX_SIDE, BOX_SIDE), 2)
        # gokei
        self.rect = pygame.draw.rect(self.screen, (black), (50, 200, BOX_SIDE, BOX_SIDE), 2)
        self.rect = pygame.draw.rect(self.screen, (black), (50, 200 + 2*BOX_SIDE + BOX_SPACE, BOX_SIDE, BOX_SIDE), 2)
        self.rect = pygame.draw.rect(self.screen, (black), (50, 200 + 4*BOX_SIDE + BOX_SPACE, BOX_SIDE, BOX_SIDE), 2)

        pygame.display.update()

    def addText(self):
        # line
        # self.screen.blit(self.font.render('レーン', True, (255,0,0)), (200,                           BOX_HORIZ_TEXT))
        # box
        self.screen.blit(self.font.render('1-1', True, (255,0,0)), (200 + 2*BOX_SIDE  + BOX_SPACE, BOX_HORIZ_TEXT))
        self.screen.blit(self.font.render('1-2', True, (255,0,0)), (200 + 4*BOX_SIDE  + BOX_SPACE, BOX_HORIZ_TEXT))
        self.screen.blit(self.font.render('1-3', True, (255,0,0)), (200 + 6*BOX_SIDE  + BOX_SPACE, BOX_HORIZ_TEXT))
        self.screen.blit(self.font.render('1-4', True, (255,0,0)), (200 + 8*BOX_SIDE  + BOX_SPACE, BOX_HORIZ_TEXT))
        self.screen.blit(self.font.render('1-5', True, (255,0,0)), (200 + 10*BOX_SIDE + BOX_SPACE, BOX_HORIZ_TEXT))
        self.screen.blit(self.font.render('1-6', True, (255,0,0)), (200 + 12*BOX_SIDE + BOX_SPACE, BOX_HORIZ_TEXT))
        self.screen.blit(self.font.render('1-7', True, (255,0,0)), (200 + 14*BOX_SIDE + BOX_SPACE, BOX_HORIZ_TEXT))
        # gokei
        self.screen.blit(self.font.render('1', True, (255,0,0)), (50 + BOX_GOKEI_OFFSET, 200 + BOX_GOKEI_OFFSET))
        self.screen.blit(self.font.render('2', True, (255,0,0)), (50 + BOX_GOKEI_OFFSET, 200 + BOX_GOKEI_OFFSET + 2*BOX_SIDE  + BOX_SPACE))
        self.screen.blit(self.font.render('3', True, (255,0,0)), (50 + BOX_GOKEI_OFFSET, 200 + BOX_GOKEI_OFFSET + 4*BOX_SIDE  + BOX_SPACE))
        pygame.display.update()

    def addValues(self):
        # line1
        self.line_1_box_1_ue = LINE_1_DATA[0]
        self.line_1_box_2_ue = LINE_1_DATA[1] 
        self.line_1_box_3_ue = LINE_1_DATA[2]
        self.line_1_box_4_ue = LINE_1_DATA[3]
        self.line_1_box_5_ue = LINE_1_DATA[4]
        self.line_1_box_6_ue = LINE_1_DATA[5]
        self.line_1_box_7_ue = LINE_1_DATA[6]
        # line2
        self.line_2_box_1_ue = LINE_2_DATA[0]
        self.line_2_box_2_ue = LINE_2_DATA[1] 
        self.line_2_box_3_ue = LINE_2_DATA[2]
        self.line_2_box_4_ue = LINE_2_DATA[3]
        self.line_2_box_5_ue = LINE_2_DATA[4]
        self.line_2_box_6_ue = LINE_2_DATA[5]
        self.line_2_box_7_ue = LINE_2_DATA[6]

        # text_box_ue_ren = self.font.render(str(gokei_ue_ren), True, black, white)
        # textBoxUeRen = text_box_ue_ren.get_rect()
        # textBoxUeRen.center = (200 + BOX_SPACE + VALUES_OFFSET, 200 + BOX_GOKEI_OFFSET + VALUES_OFFSET)
        # self.display_surface.blit(text_box_ue_ren, textBoxUeRen)
        # pygame.display.update(textBoxUeRen)

        # text_box_shita_ren = self.font.render(str(gokei_shita_ren), True, black, white)
        # textBoxShitaRen = text_box_shita_ren.get_rect()
        # textBoxShitaRen.center = (200 + BOX_SPACE + VALUES_OFFSET, 200 + BOX_GOKEI_OFFSET + 2*BOX_SIDE + VALUES_OFFSET)
        # self.display_surface.blit(text_box_shita_ren, textBoxShitaRen)
        # pygame.display.update(textBoxShitaRen)

        # text_box_total_ren = self.font.render(str(gokei_total), True, black, white)
        # textBoxTotalRen = text_box_total_ren.get_rect()
        # textBoxTotalRen.center = (200 + BOX_SPACE + VALUES_OFFSET, 200 + BOX_GOKEI_OFFSET + 4*BOX_SIDE + VALUES_OFFSET)
        # self.display_surface.blit(text_box_total_ren, textBoxTotalRen)
        # pygame.display.update(textBoxTotalRen)

        # line1
        text_box_ue_1 = self.font.render(str(self.line_1_box_1_ue), True, black, white)
        textBoxUe1 = text_box_ue_1.get_rect()
        textBoxUe1.center = (200 + 2*BOX_SIDE  + BOX_SPACE + VALUES_OFFSET, 200 + BOX_GOKEI_OFFSET + VALUES_OFFSET)
        self.display_surface.blit(text_box_ue_1, textBoxUe1)
        pygame.display.update(textBoxUe1)

        text_box_ue_2 = self.font.render(str(self.line_1_box_2_ue), True, black, white)
        textBoxUe2 = text_box_ue_2.get_rect()
        textBoxUe2.center = (200 + 4*BOX_SIDE  + BOX_SPACE + VALUES_OFFSET, 200 + BOX_GOKEI_OFFSET + VALUES_OFFSET)
        self.display_surface.blit(text_box_ue_2, textBoxUe2)
        pygame.display.update(textBoxUe2)

        text_box_ue_3 = self.font.render(str(self.line_1_box_3_ue), True, black, white)
        textBoxUe3 = text_box_ue_3.get_rect()
        textBoxUe3.center = (200 + 6*BOX_SIDE  + BOX_SPACE + VALUES_OFFSET, 200 + BOX_GOKEI_OFFSET + VALUES_OFFSET)
        self.display_surface.blit(text_box_ue_3, textBoxUe3)
        pygame.display.update(textBoxUe3)

        text_box_ue_4 = self.font.render(str(self.line_1_box_4_ue), True, black, white)
        textBoxUe4 = text_box_ue_4.get_rect()
        textBoxUe4.center = (200 + 8*BOX_SIDE  + BOX_SPACE + VALUES_OFFSET, 200 + BOX_GOKEI_OFFSET + VALUES_OFFSET)
        self.display_surface.blit(text_box_ue_4, textBoxUe4)
        pygame.display.update(textBoxUe4)

        text_box_ue_5 = self.font.render(str(self.line_1_box_5_ue), True, black, white)
        textBoxUe5 = text_box_ue_5.get_rect()
        textBoxUe5.center = (200 + 10*BOX_SIDE  + BOX_SPACE + VALUES_OFFSET, 200 + BOX_GOKEI_OFFSET + VALUES_OFFSET)
        self.display_surface.blit(text_box_ue_5, textBoxUe5)
        pygame.display.update(textBoxUe5)

        text_box_ue_6 = self.font.render(str(self.line_1_box_6_ue), True, black, white)
        textBoxUe6 = text_box_ue_6.get_rect()
        textBoxUe6.center = (200 + 12*BOX_SIDE  + BOX_SPACE + VALUES_OFFSET, 200 + BOX_GOKEI_OFFSET + VALUES_OFFSET)
        self.display_surface.blit(text_box_ue_6, textBoxUe6)
        pygame.display.update(textBoxUe6)

        text_box_ue_7 = self.font.render(str(self.line_1_box_7_ue), True, black, white)
        textBoxUe7 = text_box_ue_7.get_rect()
        textBoxUe7.center = (200 + 14*BOX_SIDE  + BOX_SPACE + VALUES_OFFSET, 200 + BOX_GOKEI_OFFSET + VALUES_OFFSET)
        self.display_surface.blit(text_box_ue_7, textBoxUe7)
        pygame.display.update(textBoxUe7)

        # line2
        text_box_shita_1 = self.font.render(str(self.line_2_box_1_ue), True, black, white)
        textBoxShita1 = text_box_shita_1.get_rect()
        textBoxShita1.center = (200 + 2*BOX_SIDE  + BOX_SPACE + VALUES_OFFSET, 200 + 2*BOX_SIDE + BOX_GOKEI_OFFSET + VALUES_OFFSET)
        self.display_surface.blit(text_box_shita_1, textBoxShita1)
        pygame.display.update(textBoxShita1)

        text_box_shita_2 = self.font.render(str(self.line_2_box_2_ue), True, black, white)
        textBoxShita2 = text_box_shita_2.get_rect()
        textBoxShita2.center = (200 + 4*BOX_SIDE  + BOX_SPACE + VALUES_OFFSET, 200 + 2*BOX_SIDE+ BOX_GOKEI_OFFSET + VALUES_OFFSET)
        self.display_surface.blit(text_box_shita_2, textBoxShita2)
        pygame.display.update(textBoxShita2)

        text_box_shita_3 = self.font.render(str(self.line_2_box_3_ue), True, black, white)
        textBoxShita3 = text_box_shita_3.get_rect()
        textBoxShita3.center = (200 + 6*BOX_SIDE  + BOX_SPACE + VALUES_OFFSET, 200 + 2*BOX_SIDE+ BOX_GOKEI_OFFSET + VALUES_OFFSET)
        self.display_surface.blit(text_box_shita_3, textBoxShita3)
        pygame.display.update(textBoxShita3)

        text_box_shita_4 = self.font.render(str(self.line_2_box_4_ue), True, black, white)
        textBoxShita4 = text_box_shita_4.get_rect()
        textBoxShita4.center = (200 + 8*BOX_SIDE  + BOX_SPACE + VALUES_OFFSET, 200 + 2*BOX_SIDE+ BOX_GOKEI_OFFSET + VALUES_OFFSET)
        self.display_surface.blit(text_box_shita_4, textBoxShita4)
        pygame.display.update(textBoxShita4)

        text_box_shita_5 = self.font.render(str(self.line_2_box_5_ue), True, black, white)
        textBoxShita5 = text_box_shita_5.get_rect()
        textBoxShita5.center = (200 + 10*BOX_SIDE  + BOX_SPACE + VALUES_OFFSET, 200 + 2*BOX_SIDE+ BOX_GOKEI_OFFSET + VALUES_OFFSET)
        self.display_surface.blit(text_box_shita_5, textBoxShita5)
        pygame.display.update(textBoxShita5)

        text_box_shita_6 = self.font.render(str(self.line_2_box_6_ue), True, black, white)
        textBoxShita6 = text_box_shita_6.get_rect()
        textBoxShita6.center = (200 + 12*BOX_SIDE  + BOX_SPACE + VALUES_OFFSET, 200 + 2*BOX_SIDE+ BOX_GOKEI_OFFSET + VALUES_OFFSET)
        self.display_surface.blit(text_box_shita_6, textBoxShita6)
        pygame.display.update(textBoxShita6)

        text_box_shita_7 = self.font.render(str(self.line_2_box_7_ue), True, black, white)
        textBoxShita7 = text_box_shita_7.get_rect()
        textBoxShita7.center = (200 + 14*BOX_SIDE  + BOX_SPACE + VALUES_OFFSET, 200 + 2*BOX_SIDE+ BOX_GOKEI_OFFSET + VALUES_OFFSET)
        self.display_surface.blit(text_box_shita_7, textBoxShita7)
        pygame.display.update(textBoxShita7)

        # line3
        text_box_shita_1 = self.font.render(str(self.line_3_box_1_ue), True, black, white)
        textBoxShita1 = text_box_shita_1.get_rect()
        textBoxShita1.center = (200 + 2*BOX_SIDE  + BOX_SPACE + VALUES_OFFSET, 200 + 4*BOX_SIDE + BOX_GOKEI_OFFSET + VALUES_OFFSET)
        self.display_surface.blit(text_box_shita_1, textBoxShita1)
        pygame.display.update(textBoxShita1)

        text_box_shita_2 = self.font.render(str(self.line_3_box_2_ue), True, black, white)
        textBoxShita2 = text_box_shita_2.get_rect()
        textBoxShita2.center = (200 + 4*BOX_SIDE  + BOX_SPACE + VALUES_OFFSET, 200 + 4*BOX_SIDE+ BOX_GOKEI_OFFSET + VALUES_OFFSET)
        self.display_surface.blit(text_box_shita_2, textBoxShita2)
        pygame.display.update(textBoxShita2)

        text_box_shita_3 = self.font.render(str(self.line_3_box_3_ue), True, black, white)
        textBoxShita3 = text_box_shita_3.get_rect()
        textBoxShita3.center = (200 + 6*BOX_SIDE  + BOX_SPACE + VALUES_OFFSET, 200 + 4*BOX_SIDE+ BOX_GOKEI_OFFSET + VALUES_OFFSET)
        self.display_surface.blit(text_box_shita_3, textBoxShita3)
        pygame.display.update(textBoxShita3)

        text_box_shita_4 = self.font.render(str(self.line_3_box_4_ue), True, black, white)
        textBoxShita4 = text_box_shita_4.get_rect()
        textBoxShita4.center = (200 + 8*BOX_SIDE  + BOX_SPACE + VALUES_OFFSET, 200 + 4*BOX_SIDE+ BOX_GOKEI_OFFSET + VALUES_OFFSET)
        self.display_surface.blit(text_box_shita_4, textBoxShita4)
        pygame.display.update(textBoxShita4)

        text_box_shita_5 = self.font.render(str(self.line_3_box_5_ue), True, black, white)
        textBoxShita5 = text_box_shita_5.get_rect()
        textBoxShita5.center = (200 + 10*BOX_SIDE  + BOX_SPACE + VALUES_OFFSET, 200 + 4*BOX_SIDE+ BOX_GOKEI_OFFSET + VALUES_OFFSET)
        self.display_surface.blit(text_box_shita_5, textBoxShita5)
        pygame.display.update(textBoxShita5)

        text_box_shita_6 = self.font.render(str(self.line_3_box_6_ue), True, black, white)
        textBoxShita6 = text_box_shita_6.get_rect()
        textBoxShita6.center = (200 + 12*BOX_SIDE  + BOX_SPACE + VALUES_OFFSET, 200 + 4*BOX_SIDE+ BOX_GOKEI_OFFSET + VALUES_OFFSET)
        self.display_surface.blit(text_box_shita_6, textBoxShita6)
        pygame.display.update(textBoxShita6)

        text_box_shita_7 = self.font.render(str(self.line_3_box_7_ue), True, black, white)
        textBoxShita7 = text_box_shita_7.get_rect()
        textBoxShita7.center = (200 + 14*BOX_SIDE  + BOX_SPACE + VALUES_OFFSET, 200 + 4*BOX_SIDE+ BOX_GOKEI_OFFSET + VALUES_OFFSET)
        self.display_surface.blit(text_box_shita_7, textBoxShita7)
        pygame.display.update(textBoxShita7)

###### End of classes ######

###### Initialization of pygame objects ######

Pan = Pane(
        line_1_box_1_ue=LINE_1_DATA[0], line_1_box_2_ue=LINE_1_DATA[1], line_1_box_3_ue=LINE_1_DATA[2], line_1_box_4_ue=LINE_1_DATA[3], line_1_box_5_ue=LINE_1_DATA[4], line_1_box_6_ue=LINE_1_DATA[5], line_1_box_7_ue=LINE_1_DATA[6],
        line_2_box_1_ue=LINE_2_DATA[0], line_2_box_2_ue=LINE_2_DATA[1], line_2_box_3_ue=LINE_2_DATA[2], line_2_box_4_ue=LINE_2_DATA[3], line_2_box_5_ue=LINE_2_DATA[4], line_2_box_6_ue=LINE_2_DATA[5], line_2_box_7_ue=LINE_2_DATA[6],
        line_3_box_1_ue=LINE_3_DATA[0], line_3_box_2_ue=LINE_3_DATA[1], line_3_box_3_ue=LINE_3_DATA[2], line_3_box_4_ue=LINE_3_DATA[3], line_3_box_5_ue=LINE_3_DATA[4], line_3_box_6_ue=LINE_3_DATA[5], line_3_box_7_ue=LINE_3_DATA[6],
        line_4_box_1_ue=LINE_4_DATA[0], line_4_box_2_ue=LINE_4_DATA[1], line_4_box_3_ue=LINE_4_DATA[2], line_4_box_4_ue=LINE_4_DATA[3], line_4_box_5_ue=LINE_4_DATA[4], line_4_box_6_ue=LINE_4_DATA[5], line_4_box_7_ue=LINE_4_DATA[6],
        line_5_box_1_ue=LINE_5_DATA[0], line_5_box_2_ue=LINE_5_DATA[1], line_5_box_3_ue=LINE_5_DATA[2], line_5_box_4_ue=LINE_5_DATA[3], line_5_box_5_ue=LINE_5_DATA[4], line_5_box_6_ue=LINE_5_DATA[5], line_5_box_7_ue=LINE_5_DATA[6],
        line_6_box_1_ue=LINE_6_DATA[0], line_6_box_2_ue=LINE_6_DATA[1], line_6_box_3_ue=LINE_6_DATA[2], line_6_box_4_ue=LINE_6_DATA[3], line_6_box_5_ue=LINE_6_DATA[4], line_6_box_6_ue=LINE_6_DATA[5], line_6_box_7_ue=LINE_6_DATA[6],
        )
Pan.addRect()
Pan.addText()
Pan.addValues()

##############################################

# run until the user asks to quit
running = True
while running:
    # did the user close the window
    for event in pygame.fastevent.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == server.EVENTTYPE:
            print(event.ip_address) # ip list config of ws clients (192.168.1.{100, 101, 102, 103, 104})
            if event.ip_address == '192.168.1.99':
                print("data from line 1")
                message_json = json.loads(event.message)
                # populate the LINE1 data table
                LINE_1_DATA[0] = message_json['tables'][0]['top']
                print(LINE_1_DATA[0])
                # color = pygame.Color('red')
                # x = (x + radius / 3) % (WIDTH - radius * 2) + radius
            Pan.addValues()

    # fill the background with white
    # screen.fill((255,255,255))

    # draw a solid blue circle in the center
    # pygame.draw.circle(screen, color, (x, int(HEIGHT/2)), radius)

    # flip the display
    # pygame.display.flip()

print("Stoping event loop")
stop_server(loop, future)
print("Waiting for termination")
thread.join()
print("Shutdown pygame")
pygame.quit()
