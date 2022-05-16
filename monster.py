import pygame
import random

# definir la classe Monster
class Monster(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 30
        self.max_health = 30
        self.attack = 0.5
        # a=["monstre1.jpg", "monstre2.jpg", "monstre3.jpg", "monstre4.jpg"]
        a=["assets/photos/Epic Hichem/p-0.png", "assets/photos/Epic Hichem/p-11.png", "assets/photos/Epic Hichem/p-149.png", "assets/photos/Epic Hichem/p-113.png"]

        #self.image = pygame.image.load(random.choice(a))
        self.image = pygame.image.load(a[random.randint(0, len(a)-1)])

        # if self.health> 0:
        #     self.image = pygame.image.load("assets/photos/kheira/p-0.png")
        # else:
        #     self.image = pygame.transform.rotate(self.image, 180)
        self.rect = self.image.get_rect()
        self.rect.x = 950 + random.randint(0, 300)
        # self.rect.y = 640 + random.randint(-30,0)
        self.rect.y = 640
        self.velocity = random.randint(1, 2)
    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            # reaparaitre comme un nouveau monstre
            self.rect.x = 950 + random.randint(0, 300)
            self.velocity = random.randint(1, 3)
            self.health = 30
    def update_health_bar(self, surface):
        # definir une couleur pour la jauge de vie (vert clair)
        bar_color = (111, 210, 46)
        # definir une couleur pour l'arriere plan de la jauge (gris foncé)
        back_bar_color = (50, 50, 50)
        # definir la position de la jauge de vie ainsi que sa largeur et son épaisseur
        bar_pos = [self.rect.x + 15, self.rect.y - 20, self.health, 5]
        # definir la position de l'arriere plan de la jauge de vie
        back_bar_pos = [self.rect.x + 15, self.rect.y - 20, self.max_health, 5]
        # dessiner l'arriere plan de la jauge de vie
        pygame.draw.rect(surface, back_bar_color, back_bar_pos)
        # dessiner la jauge de vie
        pygame.draw.rect(surface, bar_color, bar_pos)


    def forward(self):
        # le deplacement ne se fait que s'il n'ya pas de collision
        # if not self.game.check_collision(self, self.game.all_players) and  self.game.check_collision(self, self.game.screen_walls):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        # si il y a collision
        else:
            self.game.player.damage(self.attack)
        if self.rect.x < 0:
            self.rect.x = 0
