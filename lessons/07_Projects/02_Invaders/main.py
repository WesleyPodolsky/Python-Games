import pygame
from pathlib import Path


FPS = 60

hiscore = 0
game_over = False
# Initialize Pygame
vel = 0
pygame.init()

images_dir = Path(__file__).parent / "images" if (Path(__file__).parent / "images").exists() else Path(__file__).parent / "assets"
assets = Path(__file__).parent / "images"

# Screen dimensions
WIDTH, HEIGHT = 600, 450
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("invaders")




class Wave(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.wave = pygame.image.load(images_dir / "wave.png")
        self.image = self.wave
        self.rect = pygame.Rect(300,420,0,0)
        self.image = pygame.transform.scale(self.image, (44, 50))
        self.rect = self.image.get_rect(center=self.rect.center)

        

        

        
        






    def update(self):
        global vel
        vel = vel * 0.99
        self.rect.x += vel
        keys = pygame.key.get_pressed()
        if vel <= 7:
            if vel >= -7:
                if keys[pygame.K_LEFT]:
                    vel -= 0.1
                if keys[pygame.K_RIGHT]:
                    vel += 0.1

        if self.rect.x < -10:
            self.rect.x = 610
        if self.rect.x > 610:
            self.rect.x = -10

        





# Create a player object
wave = Wave()     
wave_group = pygame.sprite.GroupSingle(wave)



# Main game loop
def game_loop():
    global hiscore

    clock = pygame.time.Clock()
    

    # Group for obstacles
 

    
    
    wave = Wave()
    wave_group.add(wave)
    
    while True:
        while game_over == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            

            # Update player
            wave.update()



            # Check for collisions
        
        
            # Draw everything
            screen.fill("blue")
            wave_group.draw(screen)
            print("printing red")

            # Display obstacle count
        

        


        
            pygame.display.update()
            clock.tick(FPS)

        # Game over screen
        
game_loop()