from pygame import *

#класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
    #конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        #вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)
    
        #каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
    
        #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 #метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#класс главного игрока
class Player(GameSprite):
   #метод для управления спрайтом стрелками клавиатуры
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

#игровая сцена:
back_color = (200, 255, 255)
win_width = 600
win_height = 600
display.set_caption("Ping-Pong")
window = display.set_mode((win_width, win_height))
window.fill(back_color)

#Создание мяча и ракетки
racket1 = Player('bebra.png', 30, 200, 50, 150, 4)
racket2 = Player('bebra.png', 520, 200, 50, 150, 4)
ball = GameSprite('sinus.png', 200, 200, 50, 50, 4)

#переменная "игра закончилась": как только там True, в основном цикле перестают работать спрайты
finish = False
FPS = 60
clock = time.Clock()
speed_x = 2
speed_y = 2

#основной цикл игры:
run = True #флаг сбрасывается кнопкой закрытия окна
while run:
    #событие нажатия на кнопку Закрыть
    for e in event.get():
        if e.type == QUIT:
            run = False

    window.fill(back_color)
    ball.rect.x += speed_x
    #ball.rect.y -= speed_y


    racket1.reset()
    racket2.reset()
    ball.reset()
    racket1.update_l()
    racket2.update_r()
    

    display.update()
    clock.tick(FPS)
