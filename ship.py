import pygame
class Ship:
    def __init__(self,ai_game):
        """初始化飞船及其位置"""
        self.screen=ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect=ai_game.screen.get_rect()#访问屏幕的rect(矩形)属性

        #加载飞船图像并获取其外接矩形
        self.image=pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        #建立新飞船在底部
        self.rect.midbottom=self.screen_rect.midbottom

        #将飞船属性x中储存一个浮点数
        self.x=float(self.rect.x)
        #移动标志（飞船一开始不移动）
        self.moving_right=False
        self.moving_left=False
        self.moving_down = False
        self.moving_up = False


    def update(self):
        """根据移动标志调整飞船的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed

        #根据self.x更新rect对象
        self.rect.x=self.x
    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)
