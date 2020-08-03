import pygame
import sys

def check_keydown_events(ship,event):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

def check_keyup_events(ship,event):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ship):
    """响应鼠标和按钮事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(ship,event)

        elif event.type == pygame.KEYUP:
            check_keyup_events(ship,event)


def update_screen(screen,ai_settings,ship):
    # 背景色填充屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # 让最近绘制的屏幕可见，擦除旧屏幕
    pygame.display.flip()