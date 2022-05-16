import pygame
from Player import Player
from monster import Monster


# create classe for the game
class Game:
    def __init__(self):
        # definir si le jeu a commencé ou non
        self.is_playing = False
        # generer le player
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.pressed = {}
        # groupe de monster
        self.all_monsters = pygame.sprite.Group()

        self.screen = pygame.display.set_mode((1000, 780), pygame.RESIZABLE)
        self.screen_walls = pygame.Surface((1000, 780))

    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()
        # self.spawn_monster()
        # self.spawn_monster()

    def game_over(self):
        # remmetre le jeu a neuf, retirer les monstre , remmettre le joueur a 100 jeu en attente
        self.is_playing = False
        self.player.health = self.player.max_health
        self.all_monsters = pygame.sprite.Group()

    def update(self, screen):
        # appliquer le joueur
        screen.blit(self.player.image, self.player.rect)

        # actualiser la barre de vie du joueur
        self.player.update_health_bar(screen)
        # recupérer les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # recupérer les monster
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
        # appliquer l'ensemble des images de mon groupe monsters
        self.all_monsters.draw(screen)
        # appliquer l'ensemble des images de mon groupe projectiles
        self.player.all_projectiles.draw(screen)
        # verifier si le joueur souhaite aller à gauche ou à droite
        if self.pressed.get(pygame.K_LEFT) and self.player.rect.x or self.pressed.get(
                pygame.K_q) and self.player.rect.x > 0:
            self.player.moveLeft()
        elif self.pressed.get(
                pygame.K_RIGHT) and self.player.rect.x < screen.get_width() - self.player.rect.width or self.pressed.get(
            pygame.K_d) and self.player.rect.x < screen.get_width() - self.player.rect.width:
            self.player.moveRight()
        elif self.pressed.get(pygame.K_UP) and self.player.rect.y > 0 or self.pressed.get(
                pygame.K_z) and self.player.rect.y > 0:
            self.player.moveUp()
        elif self.pressed.get(
                pygame.K_DOWN) and self.player.rect.y < screen.get_height() - self.player.rect.height or self.pressed.get(
            pygame.K_s) and self.player.rect.y < screen.get_height() - self.player.rect.height:
            self.player.moveDown()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)
