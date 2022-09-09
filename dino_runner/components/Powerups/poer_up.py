from pygame.sprite import Sprite 
from utils.constants import HALF_SCREEN_HEIGHT, HALF_SCREEN_WIDTH, SCREEN_WIDTH
class PowerUp(Sprite): 
    def __inti__(self, image): 
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.randit(100, SCREEN_WIDTH) -100
        self.rect.y = 
        self.start_time = 0 
        self.width = self.image.get_width()
        
