import sys

import pygame

from bullet import Bullet
from settings import Settings
from ship import Ship
from aliens import Alien

class AlienInvasion:
    """管理游戏资源和行为的类"""
    def __init__(self):
        """初始化游戏资源并创建游戏资源"""
        pygame.init()
        self.clock = pygame.time.Clock()#定义一个时钟
        self.settings = Settings()#背景

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) #建立窗口
        pygame.display.set_caption("外星人入侵")

        self.ship = Ship(self)
        self.bullets=pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._creat_fleet()

        #设置背景色

    def run_game(self):
        """开始游戏的主循环"""

        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()
            self.clock.tick(60)#确定帧率：每秒运行60次

    def _check_events(self):
        """侦听键盘和鼠标事件"""
        for event in pygame.event.get():  # 访问键盘和鼠标事件
            if event.type == pygame.QUIT:
                sys.exit()  # 退出界面
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    def _check_keydown_events(self,event):
        if event.key == pygame.K_RIGHT:
            # 向右移动飞船
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # 向左移动飞船
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            #记得点击shift换为英文输入法！
            quit(0)
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """创建一颗子弹，将其加入编组group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet =Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()
        # 删除已消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        collisions=pygame.sprite.groupcollide(
            self.bullets,self.aliens,True,True
        )

    def _update_aliens(self):
        self._check_fleet_edge()
        self.aliens.update()


    def _creat_fleet(self):
        """创建一个外形舰队"""
        #创建一个外星人直到没空间
        #外星人间距为外星人的宽度和外星人的高度
        alien=Alien(self)
        alien_width,alien_height=alien.rect.size

        current_x,current_y=alien_width,alien_height
        while current_y < (self.settings.screen_height-3*alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._creat_alien(current_x,current_y)
                current_x += 2 * alien_width

            #添加一行外星人，重置x值并递增y值
            current_x = alien_width
            current_y += 2*alien_height



    def _creat_alien(self,x_position,y_position):
        """创建一个外星人并将其放入当前行中"""
        new_alien = Alien(self)
        new_alien.x=x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _check_fleet_edge(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction*=-1

    def _update_screen(self):
        # 每次循环重新绘制屏幕
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        """让最近的屏幕可见"""
        pygame.display.flip()


if __name__  == '__main__':
    #实例化对象
    ai = AlienInvasion()
    ai.run_game()