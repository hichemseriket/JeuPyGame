import pygame
from Projectile import Projectile


# crreate the first classe for the player
class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 1000
        self.max_health = 1000
        self.attack = 15
        # self.defense = 5
        self.velocity = 4
        self.all_projectiles = pygame.sprite.Group()
        # image warrior jeu
        # self.image = pygame.image.load("assets/Warrior/Individual Sprite/Attack/Warrior_Attack_1.png")
        # self.image = pygame.transform.scale(self.image, (100, 100))
        # avec limage redimensionner
        if self.health > 0:
            self.image = pygame.image.load("image_400.jpg")
            # self.image = pygame.image.load("assets/photos/Epic Hichem/p-0.png")
        else:
            self.image = pygame.transform.rotate(self.image, 180)
        # avec la grande image
        # self.image = pygame.image.load("assets/photos/hichem/p-1.png")
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 680

        # self.direction = "right"
        # self.animation_counter = 0
        # self.animation_counter_max = 5

    def damage(self, amount):
        a=0
        if self.health - amount > 0:
            self.health -= amount
        else:
            a+=1
            # si le joueur n'a plus de vie alors il est mort
            self.game.game_over()
            font = pygame.font.SysFont("comicsans", 50)
            text = font.render("nombre de fois tué : {}".format(a), True, (255, 255, 255))
            text_rect = text.get_rect()
            text.blit(text, text_rect)
    def update_health_bar(self, surface):
        # definir une couleur pour la jauge de vie (vert clair)
        bar_color = (111, 210, 46)
        # definir une couleur pour l'arriere plan de la jauge (gris foncé)
        back_bar_color = (50, 50, 50)
        # definir la position de la jauge de vie ainsi que sa largeur et son épaisseur
        bar_pos = [self.rect.x - 5, self.rect.y - 10, self.health, 7]
        # definir la position de l'arriere plan de la jauge de vie
        back_bar_pos = [self.rect.x - 5, self.rect.y - 10, self.max_health, 7]
        # dessiner l'arriere plan de la jauge de vie
        pygame.draw.rect(surface, back_bar_color, back_bar_pos)
        # dessiner la jauge de vie
        pygame.draw.rect(surface, bar_color, bar_pos)

    def launchProjectile(self):
        # créer une nouvelle instance de la classe Projectile
        self.all_projectiles.add(Projectile(self, +2))

    # shoot behind the player
    def launchProjectileArriere(self):
        # change projectile direction
        # self.direction = "left"
        # self.animation_counter += 1
        self.all_projectiles.add(Projectile(self, -2))

    def moveRight(self):
        # si le joueur n'est pas en collision avec un monstre
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity
            # self.direction = "right"
            # self.animation_counter += 1
            # if self.animation_counter > self.animation_counter_max:

    def moveLeft(self):
        self.rect.x -= self.velocity
        if self.rect.x < 0:
            self.rect.x = 0
        # self.direction = "left"
        # self.animation_counter += 1
        # if self.animation_counter > self.animation_counter_max:

    def moveUp(self):
        self.rect.y -= self.velocity

    def moveDown(self):
        self.rect.y += self.velocity
