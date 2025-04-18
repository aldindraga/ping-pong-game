from pygame import *

window = display.set_mode((700,500))
background = (145, 147, 146)
img_player = "racket.png" 
img_ball = "tenis_ball.png"




class GameSprite(sprite.Sprite):
    def __init__(self, player_image,player_x,player_y,player_speed,width,height):
        super().__init__()

        self.image = transform.scale(image.load(player_image),(width,height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def move_r1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y >5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y <380:
            self.rect.y += self.speed

    def move_r2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y >5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y <380:
            self.rect.y += self.speed

racket1=Player("racket.png",20,100,3,20,100)
racket2=Player("racket.png",655,100,3,20,100)
ball=GameSprite('tenis_ball.png',300,220,2,40,40)

speed_x=3
speed_y=3

clock = time.Clock()
font.init()
font = font.Font(None,35)
lose1 = font.render("Player 1 lost the game!",True,(180,0,0))
lose2 = font.render("Player 2 lost the game!",True,(180,0,0))
finish = False
game = True
while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
    if finish!= True:
        window.fill(background)
        racket1.reset()
        racket2.reset()
        ball.reset()
        racket1.move_r1()
        racket2.move_r2()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(racket1,ball) or sprite.collide_rect(racket2,ball):
            speed_x *=-1
            speed_y *=1

        if ball.rect.y >450 or ball.rect.y<5:
            speed_y*=-1

        if ball.rect.x <0:
            finish = True
            window.blit(lose1,(250,250))
            game = True

        if ball.rect.x >700:
            finish = True
            window.blit(lose2,(250,250))
            game = True
    display.update()
    clock.tick(60)
