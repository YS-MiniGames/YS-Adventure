import pygame
import debug

class Sprite(pygame.sprite.Sprite):
    def __init__(self,x=0,y=0,image='missing.png',size=100,text='sprite'):
        pygame.sprite.Sprite.__init__(self)
        self.x=x
        self.y=y
        self.image=pygame.image.load('images\\'+image).convert()
        self.rect=self.image.get_rect()
        self.size=size
        self.text=text
    def draw(self,screen):
        screen.blit(self.image,self.rect)
    def var_event(self):
        self.rect.topleft=(self.x,self.y)
    def update(self,screen):
        self.var_event()
        self.draw(screen)

class Game():
    def __init__(self):
        self.state=0
        # 0:menu
        self.screen=screen = pygame.display.set_mode((1360,768))
        pygame.display.set_caption('YS-Adventure')

        self.group=pygame.sprite.Group()
        self.clock=pygame.time.Clock()
        self.kb=pygame.key.get_pressed()

        self.sprite_load()

    def sprite_load(self):
        bg=Sprite()
        self.group.add(bg)
    def update(self):
        self.group.update(self.screen)



def init():
    global game
    pygame.init()
    game=Game()

def handle_event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            debug.log('Quit with X')
            pygame.quit()
            exit()

def game_event():
    game.update()
    pygame.display.update()
    game.clock.tick(60)


try:
    if __name__ == '__main__':
        debug.log('Start')
        debug.log('Init')
        init()
        debug.log('Init finish')
        while True:
            handle_event()
            game_event()
    else:
        debug.log('Start as Module',debug.WARN)
except Exception as error:
    debug.log('Error:'+repr(error),debug.ERROR)
finally:
    debug.log('Quit')