import pygame
import json
from button import overBtn
from wave import keyWave

WIDTH, HEIGHT = 300, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Key Overlay")

def draw(list, BG, BORDER):
    WIN.fill(BG)

    #loop through all items in draw list and draw
    for item in list:
        if item != None:
            item.draw(WIN)

    #if border is enabled draw border
    if(BORDER[0]):
        rect = pygame.Rect(0, 0, 300, 700)
        pygame.draw.rect(WIN, BORDER[1], rect, BORDER[2])

    pygame.display.update()

def main():
    #settings
    config = loadCFG("config.json")

    clock = pygame.time.Clock()
    BG = config["BG"]
    FPS = 60
    BORDER = (config["border"], config["border_color"], config["border_width"])
    run = True
    buttons = []
    waves = []

    #left
    buttons.append(overBtn(config["left_key"], config["key_color"], 80, 45, 600))
    #right
    buttons.append(overBtn(config["right_key"], config["key_color"], 80, 175, 600))

    while run:        
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for button in buttons:
            button.tick()

            if button.pressed:
                #if button does not have wave create wave
                if button.wave == None:
                    pos = [button.pos[0], button.pos[1]]
                    size = button.size
                    button.wave = keyWave(pos, size, config["speed"], config["key_color"], config["timers"], config["timer_threshold"])

                button.wave.tick()
            else:
                #cut off button's wave if key is not pressed
                if button.wave != None:
                    button.wave.cut = True
                    waves.append(button.wave)
                    button.wave = None

        #tick all waves
        for i, wave in enumerate(waves):
            wave.tick()
            
            #if wave is offscreen delete
            if wave.out:
                del waves[i]

        draw(buttons + waves, BG, BORDER)    

    pygame.quit()

#load json file and return
def loadCFG(path):
    file = open(path, "r")
    data = json.load(file)
    file.close()    

    return data

if __name__ == "__main__":
    main()