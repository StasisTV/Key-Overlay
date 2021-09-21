import pygame

class keyWave:
    height = 0
    speed = 4
    cut = False
    out = False
    color = (255, 255, 255)

    def __init__(self, pos, width, speed, color, timer, threshold):
        self.pos = pos
        self.width = width
        self.speed = speed
        self.color = color
        self.timer = timer

        if timer:
            self.time = 0
            self.threshold = threshold
            self.start_time = pygame.time.get_ticks()
    
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


        if self.timer:
            #if wave not cut update timer time
            if not self.cut:
                self.time = pygame.time.get_ticks() - self.start_time

            #if wave time above or equal to threshhold display timer
            if self.threshold <= self.time:
                text = pygame.font.SysFont('Sans Serif', 50).render(str(round(self.time / 1000, 2)), True, (255 - self.color[0], 255 - self.color[1], 255 - self.color[2]))
                text_rect = text.get_rect()
                text_rect.center = rect.center
                WIN.blit(text, text_rect)

        #out of bounds check
        if rect.bottom < 0:
            self.out = True
            

        

