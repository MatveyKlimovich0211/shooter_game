from random import *
import pygame
miss = 0
def game():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load('space.ogg')
    pygame.mixer.music.play()

    window = pygame.display.set_mode((700,500))
    fps = pygame.time.Clock()

    fon = pygame.image.load('galaxy.jpg')
    fon = pygame.transform.scale(fon,(700,500))

    class GameObject(pygame.sprite.Sprite):
        def __init__(self, image, visota, shirina, x, y, speed):
            super().__init__()
            self.img_sprite = pygame.image.load(image)
            self.img_sprite = pygame.transform.scale(self.img_sprite,(visota, shirina))
            self.rect = self.img_sprite.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.speed = speed
            self.move = ''
        def show(self):
            window.blit(self.img_sprite, self.rect)

    class GamePlayer(GameObject):
        def control(self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a] and self.rect.x > 0:
                self.rect.x -= self.speed
            if keys[pygame.K_d] and self.rect.x < 650:
                self.rect.x += self.speed

        def vistrel(self):
            puly = Puly('bullet.png', 15,20,self.rect.x,self.rect.y,10)
            pules.add(puly)
    global miss
    miss = 0
    class Enemy(GameObject):
        def forward(self):
            global miss
            self.rect.y += 2
            if self.rect.y > 500:
                miss+=1
                self.rect.y = -20
                self.rect.x = randint(50,650)
            
    class Puly(GameObject):
        def update(self):
            self.rect.y -= self.speed
            if self.rect.y < 0:
                self.kill()
            
    pules = pygame.sprite.Group()


    monsters = pygame.sprite.Group()
    for i in range(5):
        monster = Enemy('rocket.png', 60,60,randint(50,650), randint(-1000,10), 5)
        monsters.add(monster)



    player = GamePlayer('ufo.png', 60,60,20,400,5)

    run = True
    score = 0
    while run:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                run = False
            elif i.type == pygame.KEYDOWN:
                if i.key == pygame.K_SPACE:
                    player.vistrel()
        kill = pygame.sprite.groupcollide(pules,monsters,True,True)

        for i in kill:
            score += 1
            monster = Enemy('rocket.png', 60,60,randint(50,650), randint(-1000,10), 5)
            monsters.add(monster)

        window.blit(fon,(0,0))
        player.show()
        player.control()
        for i in monsters:
            i.forward()
            i.show()
            if i.rect.colliderect(player.rect):
                run = False

        for i in pules:
            i.show()
            i.update()
        

        result = f'Вы убилив:{str(score)}'
        bed = pygame.font.Font(None, 35).render(result, True, (255,255,255))
        window.blit(bed,(50,50))

        result = f'Вы пропустили:{str(miss)}'
        bed = pygame.font.Font(None, 35).render(result, True, (255,255,255))
        window.blit(bed,(250,50))
        if miss == 10:
            run = False

        pygame.display.update()
        fps.tick(60)
