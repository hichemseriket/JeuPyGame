import pygame
import Player
# from Player import Player
# definir la classe qui va gérer le projectile de notre joueur
class Projectile(pygame.sprite.Sprite):
    # definir le constructeur de la classe
    def __init__(self, player, velocity=2):
        super().__init__()
        self.velocity = velocity
        self.player = player
        # self.image = pygame.image.load("assets/projectile/fx.impact/impact1-1.png")
        # self.image = pygame.image.load("assets/img_2.png")
        self.image = pygame.image.load("assets/photos/hichem/p-2.png")
        # pour redemensioner mon image j'utilise ceci
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.image = pygame.transform.rotate(self.image, 180)
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x+80
        self.rect.y = player.rect.y+20
        self.origin_image = self.image
        self.angle = 0
    def rotate(self):
        # tourner le projectile
        self.angle += 10
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)
    def remove(self):
        self.player.all_projectiles.remove(self)
        self.image= pygame.image.load("assets/projectile/standard_engine_prototype.fx.propFlame/propFlame.gif")
        # self.direction = direction
        # self.speed = speed
    def move(self):
        self.rect.x += self.velocity
        self.rotate()
        # verifie si le projectiles entre en collision avec un monstre
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            self.remove()
            print("monstre touché")
            # infliger des degats au monstre
            monster.damage(self.player.attack)
        # verifie si le projectiles n'est plus sur l'ecran
        if self.rect.x > 1080:
            self.remove()
            print("projectile supprimé")

    def move_left(self):
        self.rect.x -= self.velocity
        self.rotate()
        # verifie si le projectiles n'est plus sur l'ecran
        if self.rect.x < 0:
            self.remove()
            print("projectile supprimé à gauche")