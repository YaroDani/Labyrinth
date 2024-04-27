from pygame import *

window = display.set_mode((700, 500))
display.set_caption("Лабіринт")
background = transform.scale(image.load("background.jpg"), (700, 500))

mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play()

font.init()
font = font.Font(None, 40)
font_w = font.render("YOU WIN", True, (0, 255, 0))
font_l = font.render("YOU LOSE", True, (255, 0, 0))



class GameSprites(sprite.Sprite):
    def __init__(self, player_speed, player_img, player_x, player_y):
        super().__init__()
        self.speed = player_speed
        self.img = transform.scale(image.load(player_img), (50, 50))
        self.rect = self.img.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def show_img(self):
        window.blit(self.img, self.rect)


class Player(GameSprites):
    def move(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        elif keys[K_s] and self.rect.y < 450:
            self.rect.y += self.speed
        elif keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        elif keys[K_d] and self.rect.x < 650:
            self.rect.x += self.speed


class Monster(GameSprites):
    direction = "right"

    def auto_move(self):
        if self.rect.x >= 650:
            self.direction = "left"
        if self.rect.x <= 600 - 50:
            self.direction = "right"
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
class Wall (sprite.Sprite):
    def __init__(self, wall_x , wall_y , wall_width , wall_height, wall_color1,wall_color2,wall_color3):
        super().__init__()
        self.wall_width = wall_width
        self.wall_height = wall_height
        self.wall_color1 = wall_color1
        self.wall_color2 = wall_color2
        self.wall_color3 = wall_color3
        self.surface=Surface((wall_width,wall_height))
        self.rect = self.surface.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
        self.surface.fill((wall_color1,wall_color2,wall_color3))


    def draw_wall(self):
        window.blit(self.surface,(self.rect.x, self.rect.y))



player = Player(5, "hero.png", 20, 50)

monster = Monster(3, "cyborg.png", 560, 300)

treasure = GameSprites(-1, "treasure.png", 600, 420)

w1= Wall(100,0,10,400,170,0,200)
w2= Wall(190,0,10,50,170,0,200)
w3= Wall(190,110,10,390,170,0,200)
w4= Wall(280,0,10,390,170,0,200)
w5= Wall(280,460,10,390,170,0,200)
w6= Wall(370,0,10,50,170,0,200)
w7= Wall(370,130,10,390,170,0,200)
w8= Wall(370,130,165,10,170,0,200)
w9= Wall(535,130,10,390,170,0,200)

FPS = 60

clock = time.Clock()

game = True
finish = False
while game:
    for i in event.get():
        if i.type == QUIT:
            game = False

    if not finish:
        window.blit(background, (0, 0))
        player.show_img()
        monster.show_img()
        treasure.show_img()
        player.move()
        monster.auto_move()
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()
        w9.draw_wall()


    if sprite.collide_rect(player, monster) or sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3) or sprite.collide_rect(player, w4) or sprite.collide_rect(player, w5) or sprite.collide_rect(player, w6) or sprite.collide_rect(player, w7) or sprite.collide_rect(player, w8) or sprite.collide_rect(player, w9):
        finish = True
        window.blit(font_l, (315, 250))
    if sprite.collide_rect(player, treasure):
        finish = True
        window.blit(font_w, (315, 250))


    display.update()
    clock.tick(FPS)