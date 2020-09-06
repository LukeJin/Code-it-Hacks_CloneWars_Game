import pygame

bdroid_att1 = pygame.image.load('bdroid_att1.png')
bdroid_att2 = pygame.image.load('bdroid_att2.png')
bdroid_att3 = pygame.image.load('bdroid_att3.png')
bdroid_att4 = pygame.image.load('bdroid_att4.png')
bdroid_att5 = pygame.image.load('bdroid_att5.png')
bdroid_att6 = pygame.image.load('bdroid_att6.png')
bdroid_att7 = pygame.image.load('bdroid_att7.png')
bdroid_death1 = pygame.image.load('bdroid_death1.png')
bdroid_death2 = pygame.image.load('bdroid_death2.png')
bdroid_death3 = pygame.image.load('bdroid_death3.png')
bdroid_death4 = pygame.image.load('bdroid_death4.png')
bdroid_death5 = pygame.image.load('bdroid_death5.png')
bdroid_death6 = pygame.image.load('bdroid_death6.png')
bdroid_death7 = pygame.image.load('bdroid_death7.png')
bdroid_death8 = pygame.image.load('bdroid_death8.png')
bdroid_death9 = pygame.image.load('bdroid_death9.png')

class Bdroid:

    def __init__(self, x, y, health, speed):
        self.x = x
        self.y = y
        self.health = health
        self.maxhealth = health/100
        self.speed = speed
        self.death = False
        self.dmg = speed*5
        self.attack = False
        self.exp = 500
        self.index = 0
        self.att_frames = [bdroid_att1, bdroid_att2, bdroid_att3, bdroid_att4, bdroid_att5, bdroid_att6, bdroid_att7, bdroid_att1, bdroid_att1]
        self.death_frames = [bdroid_death1, bdroid_death2, bdroid_death3, bdroid_death4, bdroid_death5, bdroid_death6, bdroid_death7, bdroid_death8, bdroid_death9]
        self.death = False
        self.dead = False

    def healthCheck(self):
        if self.health <= 0:
            self.death = True
            self.health = 0
        else:
            self.death = False

class Sbdroid:

    def __init__(self, x, y, health, speed):
        self.x = x
        self.y = y
        self.health = health
        self.maxhealth = health/100
        self.speed = speed
        self.dmg = self.speed*10
        self.death = False
        self.attack = False
        self.mana = 50
        self.exp = 2000
        self.index = 0

    def healthCheck(self):
        if self.health <= 0:
            return True
        else:
            return False

