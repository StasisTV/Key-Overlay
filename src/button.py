import pygame
import keyboard

pygame.font.init()

class overBtn:
    pressed = False
    level = 0
    max = 10
    width = 5
    wave = None

    def __init__(self, key, color, size, x, y):
        self.key = key
        self.size = size
        self.pos = [x, y]
        self.color = color

    #check if key is pressed and expand/shrink accordingly
    def tick(self):
        if keyboard.is_pressed(self.key):
            self.pressed = True

            if self.level < self.max:
                self.level += 2
        else:
            self.pressed = False
            
            if self.level > 0:
                self.level -= 2
    
    def draw(self, WIN):
        #draw button
        rect = pygame.Rect(self.pos[0] + (self.level/2), self.pos[1] + (self.level/2) , self.size - self.level, self.size - self.level)
        pygame.draw.rect(WIN, self.color, rect, self.width)

        #Draw key text in center of button
        text = pygame.font.Font('font.ttf', 60 - self.level).render(self.key, True, self.color)
        text_rect = text.get_rect()
        text_rect.center = rect.center
        WIN.blit(text, text_rect)

        #if button has wave draw wave
        if self.wave != None:
            self.wave.draw(WIN)
