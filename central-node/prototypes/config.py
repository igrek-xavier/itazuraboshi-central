# config.py

BOX_SIDE  = 70
BOX_SPACE = 0
BOX_HORIZ = 100
BOX_HORIZ_TEXT = 110
BOX_GOKEI_OFFSET = 10
VALUES_OFFSET = 20

# LINE_1_DATA = [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

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


class Pane(object):
    def __init__(self,
            line_1_box_1_ue, line_1_box_2_ue, line_1_box_3_ue, line_1_box_4_ue, line_1_box_5_ue, line_1_box_6_ue, line_1_box_7_ue,
            line_1_box_1_shita, line_1_box_2_shita, line_1_box_3_shita, line_1_box_4_shita, line_1_box_5_shita, line_1_box_6_shita, line_1_box_7_shita,
            ):
        self.line_1_box_1_ue = line_1_box_1_ue
        self.line_1_box_2_ue = line_1_box_2_ue
        self.line_1_box_3_ue = line_1_box_3_ue
        self.line_1_box_4_ue = line_1_box_4_ue
        self.line_1_box_5_ue = line_1_box_5_ue
        self.line_1_box_6_ue = line_1_box_6_ue
        self.line_1_box_7_ue = line_1_box_7_ue

        self.line_1_box_1_shita = line_1_box_1_shita
        self.line_1_box_2_shita = line_1_box_2_shita
        self.line_1_box_3_shita = line_1_box_3_shita
        self.line_1_box_4_shita = line_1_box_4_shita
        self.line_1_box_5_shita = line_1_box_5_shita
        self.line_1_box_6_shita = line_1_box_6_shita
        self.line_1_box_7_shita = line_1_box_7_shita
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
        self.rect = pygame.draw.rect(self.screen, (black), (200,                           BOX_HORIZ, BOX_SIDE + 30, BOX_SIDE), 2)
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
        self.screen.blit(self.font.render('レーン', True, (255,0,0)), (200,                           BOX_HORIZ_TEXT))
        # box
        self.screen.blit(self.font.render('1-1', True, (255,0,0)), (200 + 2*BOX_SIDE  + BOX_SPACE, BOX_HORIZ_TEXT))
        self.screen.blit(self.font.render('1-2', True, (255,0,0)), (200 + 4*BOX_SIDE  + BOX_SPACE, BOX_HORIZ_TEXT))
        self.screen.blit(self.font.render('1-3', True, (255,0,0)), (200 + 6*BOX_SIDE  + BOX_SPACE, BOX_HORIZ_TEXT))
        self.screen.blit(self.font.render('1-4', True, (255,0,0)), (200 + 8*BOX_SIDE  + BOX_SPACE, BOX_HORIZ_TEXT))
        self.screen.blit(self.font.render('1-5', True, (255,0,0)), (200 + 10*BOX_SIDE + BOX_SPACE, BOX_HORIZ_TEXT))
        self.screen.blit(self.font.render('1-6', True, (255,0,0)), (200 + 12*BOX_SIDE + BOX_SPACE, BOX_HORIZ_TEXT))
        self.screen.blit(self.font.render('1-7', True, (255,0,0)), (200 + 14*BOX_SIDE + BOX_SPACE, BOX_HORIZ_TEXT))
        # gokei
        self.screen.blit(self.font.render('上',   True, (255,0,0)), (50 + BOX_GOKEI_OFFSET, 200 + BOX_GOKEI_OFFSET))
        self.screen.blit(self.font.render('下',   True, (255,0,0)), (50 + BOX_GOKEI_OFFSET, 200 + BOX_GOKEI_OFFSET + 2*BOX_SIDE  + BOX_SPACE))
        self.screen.blit(self.font.render('合計', True, (255,0,0)), (50 + BOX_GOKEI_OFFSET, 200 + BOX_GOKEI_OFFSET + 4*BOX_SIDE  + BOX_SPACE))
        pygame.display.update()

    def addValues(self):
        # ren gokei = ue, shita, gokei
        self.line_1_box_1_ue = BOX_UE_1
        self.box_2_ue = BOX_UE_2
        self.box_3_ue = BOX_UE_3
        self.box_4_ue = BOX_UE_4
        self.box_5_ue = BOX_UE_5
        self.box_6_ue = BOX_UE_6
        self.box_7_ue = BOX_UE_7
        # print(self.box_1_ue)
        self.box_1_shita = BOX_SHITA_1
        self.box_2_shita = BOX_SHITA_2
        self.box_3_shita = BOX_SHITA_3
        self.box_4_shita = BOX_SHITA_4
        self.box_5_shita = BOX_SHITA_5
        self.box_6_shita = BOX_SHITA_6
        self.box_7_shita = BOX_SHITA_7
        # print(self.box_1_ue)
        gokei_ue_ren = self.line_1_box_1_ue + self.box_2_ue + self.box_3_ue + self.box_4_ue + self.box_5_ue + self.box_6_ue + self.box_7_ue
        gokei_shita_ren = self.box_1_shita + self.box_2_shita + self.box_3_shita + self.box_4_shita + self.box_5_shita + self.box_6_shita + self.box_7_shita
        gokei_total = gokei_ue_ren + gokei_shita_ren
        gokei_box_1 = self.line_1_box_1_ue + self.box_1_shita
        gokei_box_2 = self.box_2_ue + self.box_2_shita
        gokei_box_3 = self.box_3_ue + self.box_3_shita
        gokei_box_4 = self.box_4_ue + self.box_4_shita
        gokei_box_5 = self.box_5_ue + self.box_5_shita
        gokei_box_6 = self.box_6_ue + self.box_6_shita
        gokei_box_7 = self.box_7_ue + self.box_7_shita
         
        text_box_ue_ren = self.font.render(str(gokei_ue_ren), True, black, white)
        textBoxUeRen = text_box_ue_ren.get_rect()
        textBoxUeRen.center = (200 + BOX_SPACE + VALUES_OFFSET, 200 + BOX_GOKEI_OFFSET + VALUES_OFFSET)
        self.display_surface.blit(text_box_ue_ren, textBoxUeRen)
        pygame.display.update(textBoxUeRen)

        text_box_shita_ren = self.font.render(str(gokei_shita_ren), True, black, white)
        textBoxShitaRen = text_box_shita_ren.get_rect()
        textBoxShitaRen.center = (200 + BOX_SPACE + VALUES_OFFSET, 200 + BOX_GOKEI_OFFSET + 2*BOX_SIDE + VALUES_OFFSET)
        self.display_surface.blit(text_box_shita_ren, textBoxShitaRen)
        pygame.display.update(textBoxShitaRen)

        text_box_total_ren = self.font.render(str(gokei_total), True, black, white)
        textBoxTotalRen = text_box_total_ren.get_rect()
        textBoxTotalRen.center = (200 + BOX_SPACE + VALUES_OFFSET, 200 + BOX_GOKEI_OFFSET + 4*BOX_SIDE + VALUES_OFFSET)
        self.display_surface.blit(text_box_total_ren, textBoxTotalRen)
        pygame.display.update(textBoxTotalRen)

        # box gokei
        # box ue
        text_box_ue_1 = self.font.render(str(self.line_1_box_1_ue), True, black, white)
        textBoxUe1 = text_box_ue_1.get_rect()
        textBoxUe1.center = (200 + 2*BOX_SIDE  + BOX_SPACE + VALUES_OFFSET, 200 + BOX_GOKEI_OFFSET + VALUES_OFFSET)
        self.display_surface.blit(text_box_ue_1, textBoxUe1)
        pygame.display.update(textBoxUe1)

        text_box_ue_2 = self.font.render(str(self.box_2_ue), True, black, white)
        textBoxUe2 = text_box_ue_2.get_rect()
        textBoxUe2.center = (200 + 4*BOX_SIDE  + BOX_SPACE + VALUES_OFFSET, 200 + BOX_GOKEI_OFFSET + VALUES_OFFSET)
        self.display_surface.blit(text_box_ue_2, textBoxUe2)
        pygame.display.update(textBoxUe2)

        text_box_ue_3 = self.font.render(str(self.box_3_ue), True, black, white)
        textBoxUe3 = text_box_ue_3.get_rect()
        textBoxUe3.center = (200 + 6*BOX_SIDE  + BOX_SPACE + VALUES_OFFSET, 200 + BOX_GOKEI_OFFSET + VALUES_OFFSET)
        self.display_surface.blit(text_box_ue_3, textBoxUe3)
        pygame.display.update(textBoxUe3)

        text_box_ue_4 = self.font.render(str(self.box_4_ue), True, black, white)
        textBoxUe4 = text_box_ue_4.get_rect()
        textBoxUe4.center = (200 + 8*BOX_SIDE  + BOX_SPACE + VALUES_OFFSET, 200 + BOX_GOKEI_OFFSET + VALUES_OFFSET)
        self.display_surface.blit(text_box_ue_4, textBoxUe4)
        pygame.display.update(textBoxUe4)

        text_box_ue_5 = self.font.render(str(self.box_5_ue), True, black, white)
        textBoxUe5 = text_box_ue_5.get_rect()
        textBoxUe5.center = (200 + 10*BOX_SIDE  + BOX_SPACE + VALUES_OFFSET, 200 + BOX_GOKEI_OFFSET + VALUES_OFFSET)
        self.display_surface.blit(text_box_ue_5, textBoxUe5)
        pygame.display.update(textBoxUe5)

        text_box_ue_6 = self.font.render(str(self.box_6_ue), True, black, white)
        textBoxUe6 = text_box_ue_6.get_rect()
        textBoxUe6.center = (200 + 12*BOX_SIDE  + BOX_SPACE + VALUES_OFFSET, 200 + BOX_GOKEI_OFFSET + VALUES_OFFSET)
        self.display_surface.blit(text_box_ue_6, textBoxUe6)
        pygame.display.update(textBoxUe6)

        text_box_ue_7 = self.font.render(str(self.box_7_ue), True, black, white)
        textBoxUe7 = text_box_ue_7.get_rect()
        textBoxUe7.center = (200 + 14*BOX_SIDE  + BOX_SPACE + VALUES_OFFSET, 200 + BOX_GOKEI_OFFSET + VALUES_OFFSET)
        self.display_surface.blit(text_box_ue_7, textBoxUe7)
        pygame.display.update(textBoxUe7)

        # box shita
        text_box_shita_1 = self.font.render(str(self.box_1_shita), True, black, white)
        textBoxShita1 = text_box_shita_1.get_rect()
        textBoxShita1.center = (200 + 2*BOX_SIDE  + BOX_SPACE + VALUES_OFFSET, 200 + 2*BOX_SIDE + BOX_GOKEI_OFFSET + VALUES_OFFSET)
        self.display_surface.blit(text_box_shita_1, textBoxShita1)
        pygame.display.update(textBoxShita1)

        text_box_shita_2 = self.font.render(str(self.box_2_shita), True, black, white)
        textBoxShita2 = text_box_shita_2.get_rect()
        textBoxShita2.center = (200 + 4*BOX_SIDE  + BOX_SPACE + VALUES_OFFSET, 200 + 2*BOX_SIDE+ BOX_GOKEI_OFFSET + VALUES_OFFSET)
        self.display_surface.blit(text_box_shita_2, textBoxShita2)
        pygame.display.update(textBoxShita2)

        text_box_shita_3 = self.font.render(str(self.box_3_shita), True, black, white)
        textBoxShita3 = text_box_shita_3.get_rect()
        textBoxShita3.center = (200 + 6*BOX_SIDE  + BOX_SPACE + VALUES_OFFSET, 200 + 2*BOX_SIDE+ BOX_GOKEI_OFFSET + VALUES_OFFSET)
        self.display_surface.blit(text_box_shita_3, textBoxShita3)
        pygame.display.update(textBoxShita3)

        text_box_shita_4 = self.font.render(str(self.box_4_shita), True, black, white)
        textBoxShita4 = text_box_shita_4.get_rect()
        textBoxShita4.center = (200 + 8*BOX_SIDE  + BOX_SPACE + VALUES_OFFSET, 200 + 2*BOX_SIDE+ BOX_GOKEI_OFFSET + VALUES_OFFSET)
        self.display_surface.blit(text_box_shita_4, textBoxShita4)
        pygame.display.update(textBoxShita4)

        text_box_shita_5 = self.font.render(str(self.box_5_shita), True, black, white)
        textBoxShita5 = text_box_shita_5.get_rect()
        textBoxShita5.center = (200 + 10*BOX_SIDE  + BOX_SPACE + VALUES_OFFSET, 200 + 2*BOX_SIDE+ BOX_GOKEI_OFFSET + VALUES_OFFSET)
        self.display_surface.blit(text_box_shita_5, textBoxShita5)
        pygame.display.update(textBoxShita5)

        text_box_shita_6 = self.font.render(str(self.box_6_shita), True, black, white)
        textBoxShita6 = text_box_shita_6.get_rect()
        textBoxShita6.center = (200 + 12*BOX_SIDE  + BOX_SPACE + VALUES_OFFSET, 200 + 2*BOX_SIDE+ BOX_GOKEI_OFFSET + VALUES_OFFSET)
        self.display_surface.blit(text_box_shita_6, textBoxShita6)
        pygame.display.update(textBoxShita6)

        text_box_shita_7 = self.font.render(str(self.box_7_shita), True, black, white)
        textBoxShita7 = text_box_shita_7.get_rect()
        textBoxShita7.center = (200 + 14*BOX_SIDE  + BOX_SPACE + VALUES_OFFSET, 200 + 2*BOX_SIDE+ BOX_GOKEI_OFFSET + VALUES_OFFSET)
        self.display_surface.blit(text_box_shita_7, textBoxShita7)
        pygame.display.update(textBoxShita7)

        # # box gokei
        text_box_shita_1 = self.font.render(str(gokei_box_1), True, black, white)
        textBoxShita1 = text_box_shita_1.get_rect()
        textBoxShita1.center = (200 + 2*BOX_SIDE  + BOX_SPACE + VALUES_OFFSET, 200 + 4*BOX_SIDE + BOX_GOKEI_OFFSET + VALUES_OFFSET)
        self.display_surface.blit(text_box_shita_1, textBoxShita1)
        pygame.display.update(textBoxShita1)

        text_box_shita_2 = self.font.render(str(gokei_box_2), True, black, white)
        textBoxShita2 = text_box_shita_2.get_rect()
        textBoxShita2.center = (200 + 4*BOX_SIDE  + BOX_SPACE + VALUES_OFFSET, 200 + 4*BOX_SIDE+ BOX_GOKEI_OFFSET + VALUES_OFFSET)
        self.display_surface.blit(text_box_shita_2, textBoxShita2)
        pygame.display.update(textBoxShita2)

        text_box_shita_3 = self.font.render(str(gokei_box_3), True, black, white)
        textBoxShita3 = text_box_shita_3.get_rect()
        textBoxShita3.center = (200 + 6*BOX_SIDE  + BOX_SPACE + VALUES_OFFSET, 200 + 4*BOX_SIDE+ BOX_GOKEI_OFFSET + VALUES_OFFSET)
        self.display_surface.blit(text_box_shita_3, textBoxShita3)
        pygame.display.update(textBoxShita3)

        text_box_shita_4 = self.font.render(str(gokei_box_4), True, black, white)
        textBoxShita4 = text_box_shita_4.get_rect()
        textBoxShita4.center = (200 + 8*BOX_SIDE  + BOX_SPACE + VALUES_OFFSET, 200 + 4*BOX_SIDE+ BOX_GOKEI_OFFSET + VALUES_OFFSET)
        self.display_surface.blit(text_box_shita_4, textBoxShita4)
        pygame.display.update(textBoxShita4)

        text_box_shita_5 = self.font.render(str(gokei_box_5), True, black, white)
        textBoxShita5 = text_box_shita_5.get_rect()
        textBoxShita5.center = (200 + 10*BOX_SIDE  + BOX_SPACE + VALUES_OFFSET, 200 + 4*BOX_SIDE+ BOX_GOKEI_OFFSET + VALUES_OFFSET)
        self.display_surface.blit(text_box_shita_5, textBoxShita5)
        pygame.display.update(textBoxShita5)

        text_box_shita_6 = self.font.render(str(gokei_box_6), True, black, white)
        textBoxShita6 = text_box_shita_6.get_rect()
        textBoxShita6.center = (200 + 12*BOX_SIDE  + BOX_SPACE + VALUES_OFFSET, 200 + 4*BOX_SIDE+ BOX_GOKEI_OFFSET + VALUES_OFFSET)
        self.display_surface.blit(text_box_shita_6, textBoxShita6)
        pygame.display.update(textBoxShita6)

        text_box_shita_7 = self.font.render(str(gokei_box_7), True, black, white)
        textBoxShita7 = text_box_shita_7.get_rect()
        textBoxShita7.center = (200 + 14*BOX_SIDE  + BOX_SPACE + VALUES_OFFSET, 200 + 4*BOX_SIDE+ BOX_GOKEI_OFFSET + VALUES_OFFSET)
        self.display_surface.blit(text_box_shita_7, textBoxShita7)
        pygame.display.update(textBoxShita7)
