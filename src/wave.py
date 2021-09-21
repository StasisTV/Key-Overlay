import pygame

class keyWave:
    height = 0
    speed = 4
    cut = False
    out = False
    color = (255, 255, 255)

    def __init__(self, pos, width, speed):
        self.pos = pos
        self.width = width
        self.speed = speed
    
    def tick(self):
        if not self.cut:
            self.height += self.speed
        self.pos[1] -= self.speed
        pass

    def draw(self, WIN):
        rect = pygame.Rect(self.pos[0], self.pos[1], self.width, self.height)
        pygame.draw.rect(WIN, self.color, rect)

        if rect.bottom < 0:
            self.out = True
            

        
