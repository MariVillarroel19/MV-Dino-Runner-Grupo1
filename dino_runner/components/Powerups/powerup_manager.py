from dino_runner.components.Powerups.shield import Shield

class PowerUpManager: 

    def __init__(self):
        self.power_ups = []
        self.when_appears = 0
    
    def update(self, game): 
        self.generate_power_ups()
        for power_up in self.power_ups: 
            power_up.update(game.game_speed)
            if game.dinosaur.dino_rect.colliderect(power_up.rect): 
                power_up.start_time = pygame.time.get_ticks()
                game.dinosaur.isShieldType = True 
                power_up.start_time = pygame.time.get_ticks()
                self.power_ups.remove(power_up)

    def generate_power_ups(self): 
        if len(self.power_ups) == 0:  
            self.power_ups.append(Shield())
    def draw(self):
        for power_up in self.power_ups: 
            power_up.draw(screen)

    def reset_power_ups(self): 
        self.power_ups = []


