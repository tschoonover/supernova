import pygame
from gpiozero import Button
from random import randrange
import glob

def main():
    pygame.init()
    
    sounds = [pygame.mixer.Sound(f) for f in glob.glob("sounds/*.wav")]
    
    is_playing = False
    
    def play_sound():
        nonlocal is_playing
        
        if not is_playing:
            is_playing = True
            sounds[randrange(len(sounds))].play()
            is_playing = False
            
    button = Button(4, bounce_time = 0.1)
    button.when_pressed = play_sound

    pygame.event.clear()

    while True:
        event = pygame.event.wait()
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
if __name__ == '__main__':
    main()