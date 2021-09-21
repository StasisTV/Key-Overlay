import pygame
import json
from button import overBtn
from wave import keyWave

WIDTH, HEIGHT = 250, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Key Overlay")

def draw(list, BG):
    WIN.fill(BG)

    for item in list:
        if not item == None:
            item.draw(WIN)

    pygame.display.update()

def main():
    config = loadCFG("config.json")

    clock = pygame.time.Clock()
    BG = config["BG"]
    FPS = 60
    run = True
    buttons = []
    waves = []

    #left
    buttons.append(overBtn(config["left_key"], config["key_color"], 80, 20, 600))
    #right
    buttons.append(overBtn(config["right_key"], config["key_color"], 80, 150, 600))

    while run:        
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for button in buttons:
            button.tick()
            if button.pressed:
                if button.wave == None:
                    pos = [button.pos[0], button.pos[1]]
                    size = button.size
                    button.wave = keyWave(pos, size, config["speed"])

                button.wave.tick()
            else:
                if button.wave != None:
                    button.wave.cut = True
                    waves.append(button.wave)
                    button.wave = None

        for i, wave in enumerate(waves):
            wave.tick()
            
            if wave.out:
                del waves[i]

        draw(buttons + waves, BG)    

    pygame.quit()

def loadCFG(path):
    file = open(path, "r")
    data = json.load(file)
    file.close()    

    return data

if __name__ == "__main__":
    main()