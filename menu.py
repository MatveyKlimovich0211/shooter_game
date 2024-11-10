import pygame
import shooter_game

pygame.init()



window = pygame.display.set_mode((700,500))
fps = pygame.time.Clock()

fon = pygame.image.load('galaxy.jpg')
fon = pygame.transform.scale(fon,(700,500))

button_rect = pygame.Rect(200,200,200,50)
button_exit = pygame.Rect(200,270,200,50)

bed = pygame.font.Font(None,35).render('Начать игру', True, (255,255,255))
exit_bed = pygame.font.Font(None,35).render('Выход', True, (255,255,255))

run = True
while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        elif i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
            if button_rect.collidepoint(i.pos):
                shooter_game.game()
                running = False

            elif button_exit.collidepoint(i.pos):
                running = False
               

    pygame.draw.rect(window, (22,66,168),button_rect)
    pygame.draw.rect(window, (22,66,168),button_exit)
    window.blit(bed,(225,210))
    window.blit(exit_bed,(250,280))
    pygame.display.update()
    fps.tick(60)


