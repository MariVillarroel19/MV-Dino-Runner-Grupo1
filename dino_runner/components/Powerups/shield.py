from dino_runner.components.Powerups import PowerUp
from dino_runner.utils.constants import SHIELD 
class Shield(PowerUp): 
    def __init__(self):
        self.image = SHIELD
        super(Shield, self).__init__(self.image, SHIELD_TYPE)