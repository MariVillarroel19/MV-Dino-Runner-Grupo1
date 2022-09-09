from pygame.sprite import Sprite

from utils.constants import RUNNING 

class Dinosaur(Sprite):
    X_POS = 80 
    Y_POS = 360
    def __int__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rec.x = self.X_POS
        self.dino_rec.y = self.Y_POS
        self.step_index = 0 

    def update(self):
        self.run()
        if self.step_index >= 12: 
            self.step_index = 0

    def draw(self, screen): 
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

    def run(self): 
        self.image = RUNNING[0] if self.step_index < 8 else RUNNING[1]  
        self.dino_rect = self.image.get_rect() 
        self.dino_rec.x = self.X_POS
        self.dino_rec.y = self.Y_POS
        self.step_index += 1