class Settings:
    def __init__(self):
        """初始化游戏的设置"""
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        #飞船的设置
        self.ship_speed=10#飞船速度
        #子弹的设置
        self.bullet_speed=2.0
        self.bullet_width=20
        self.bullet_height=15
        self.bullet_color=(160,160,160)
        self.bullets_allowed=1000
        #外星人的设置
        self.alien_speed=1.0
        self.fleet_drop_speed=10
        #fleet_direction 为1表示向右移动，-1表示向左移动
        self.fleet_direction=1
