import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #初始化pygame、设置和屏幕对象
    pygame.init()
    #创建一个Settings实例，并将其存在ai_settings中
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    ship = Ship(screen,ai_settings)


    #开始游戏主循环
    while True:
        #监视鼠标和键盘事件
        gf.check_events(ship)
        ship.update()
        gf.update_screen(screen,ai_settings,ship)

run_game()