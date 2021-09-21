import pygame

class keyWave:
    height = 0
    speed = 4
    cut = False
    out = False
    color = (255, 255, 255)

    def __init__(self, pos, width, speed, color):
        self.pos = pos
        self.width = width
        self.speed = speed
        self.color = color
    
    #move wave
    #if wave not cut extend height
    def tick(self):
        if not self.cut:
            self.height += self.speed
        self.pos[1] -= self.speed
        pass

    #draw wave and check if out of bounds
    def draw(self, WIN):
        rect = pygame.Rect(self.pos[0], self.pos[1], self.width, self.height)
        pygame.draw.rect(WIN, self.color, rect)

        if rect.bottom < 0:
            self.out = True
            

        

