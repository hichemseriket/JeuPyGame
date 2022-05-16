import pygame
from Game import Game
from PIL import Image

pygame.init()
clock = pygame.time.Clock()
# generer la fenetre de notre jeux

pygame.display.set_caption("Comet fall Game")
screen = pygame.display.set_mode((950, 740))
# screen = pygame.display.set_mode((1900, 1080))

# charger BG
background = pygame.image.load("assets/img_1.png")

# importer ou charger notre banniere
# banner = pygame.image.load("assets/photos/darshaaaaan/p-270.png")
banner = pygame.image.load("assets/photos/hichem/p-1.png")
banner = pygame.transform.scale(banner, (500, 450))
banner_rect = banner.get_rect()
banner_rect.x = screen.get_width() / 2 - banner_rect.width / 2
banner_rect.y = screen.get_height() / 2 - banner_rect.height / 2

# importer ou charger mon boutton pour lancer la partie
start_button = pygame.image.load("assets/photos/hichem/p-3.png")
start_button = pygame.transform.scale(start_button, (450, 100))
start_button_rect = start_button.get_rect()
start_button_rect.x = screen.get_width() / 2 - start_button_rect.width / 2
start_button_rect.y = screen.get_height() / 2 - start_button_rect.height / 2 + 300
# chrager le game
game = Game()

# # charger notre joueur
# player = Player()
running = True

# boucle tant que running est tru
while running:
    # appliquer le background
    screen.blit(background, (0, 0))

    # verifier si notre jeu a commencé ou non
    if game.is_playing:
        # si oui alors on lance le jeu
        game.update(screen)
    else:
        # sinon on affiche la banniere donc un ecran de bienvenue
        screen.blit(banner, (banner_rect.x , banner_rect.y))
        screen.blit(start_button, (start_button_rect.x, start_button_rect.y))
        # mettre un text sur le boutton
        font = pygame.font.SysFont("comicsans", 50)
        text = font.render("START !", True, (255, 255, 255))
        text_rect = text.get_rect()
        screen.blit(text, (start_button_rect.x + start_button_rect.width / 2 - text_rect.width / 2,
                           start_button_rect.y + start_button_rect.height / 2 - text_rect.height / 2))

    # mettre à jour l'ecran
    pygame.display.flip()

    # detecter les evenements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            print("quitter")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            # detecter si la touche espace est enclenché pour lancer mon projectile
            if event.key == pygame.K_SPACE:
                game.player.launchProjectile()
            if event.key == pygame.K_b:
                game.player.launchProjectileArriere()
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # verifier si la souris est en collision avec le boutton
            if start_button_rect.collidepoint(event.pos):
                # si oui alors on lance le jeu
                game.start()




    dt = clock.tick(160)