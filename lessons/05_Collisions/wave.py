"""
Dino Jump

Use the arrow keys to move the blue square up and down to avoid the black
obstacles. The game should end when the player collides with an obstacle ...
but it does not. It's a work in progress, and you'll have to finish it. 

"""
import pygame
import random
from pathlib import Path
i=0
game_over = False
passedobj = 0
hiscore = 0
# Initialize Pygame
pygame.init()

images_dir = Path(__file__).parent / "images" if (Path(__file__).parent / "images").exists() else Path(__file__).parent / "assets"
assets = Path(__file__).parent / "images"

# Screen dimensions
WIDTH, HEIGHT = 600, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Jump")

# Colors
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (150, 150, 150)

# FPS
FPS = 60

# Player attributes
PLAYER_SIZE = 30

player_speed = 5

# Obstacle attributes
OBSTACLE_WIDTH = 200
OBSTACLE_HEIGHT = 90
obstacle_speed = 5

# Font
font = pygame.font.SysFont(None, 36)




# Define an obstacle class
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((OBSTACLE_WIDTH, OBSTACLE_HEIGHT), pygame.SRCALPHA)
        self.image.fill(BLACK)
        self.rect = pygame.Rect(100,200,10,10)
        self.rect.x = WIDTH
        self.rect.y = HEIGHT - OBSTACLE_HEIGHT - 10

        self.explosion = pygame.image.load(images_dir / "explosion1.gif")
        self.cactus = pygame.image.load(images_dir / "gdspike.png")
        # pygame.draw.polygon(self.image, 'red', [(self.rect.x + OBSTACLE_HEIGHT, self.rect.y + OBSTACLE_HEIGHT),( self.rect.x+OBSTACLE_WIDTH, self.rect.y + OBSTACLE_HEIGHT), (self.rect.x+OBSTACLE_WIDTH/2, self.rect.y)] )
        self.mask = pygame.mask.from_surface(self.image)

        self.image = self.cactus
        self.image = pygame.transform.scale(self.image, (OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
        self.rect = pygame.Rect(500,210,50,75)
        

    def update(self):
        self.rect.x -= obstacle_speed
        # Remove the obstacle if it goes off screen
        if self.rect.right < 0:
            self.kill()
            global passedobj
            passedobj += 1
        
            

    def explode(self):
        """Replace the image with an explosition image."""
        
        # Load the explosion image
        self.image = self.explosion
        self.image = pygame.transform.scale(self.image, (OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
        self.rect = self.image.get_rect(center=self.rect.center)
        global game_over
        game_over = True
        

    

# Define a player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = HEIGHT - PLAYER_SIZE - 10
        self.speed = player_speed
        self.vel = 0
        self.isjumping = False

        

        



    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            if self.rect.top > 0:
                self.rect.y -= 7
                self.dino = pygame.image.load(images_dir / "waveup.png")
                self.image = self.dino
            self.image = pygame.transform.scale(self.image, (PLAYER_SIZE, PLAYER_SIZE))
            self.rect = self.image.get_rect(center=self.rect.center)
            self.mask = pygame.mask.from_surface(self.image)
        elif self.rect.bottom < 295:
            self.dino = pygame.image.load(images_dir / "wavedown.png")
            self.image = self.dino
            self.image = pygame.transform.scale(self.image, (PLAYER_SIZE, PLAYER_SIZE))
            self.rect = self.image.get_rect(center=self.rect.center)
            self.mask = pygame.mask.from_surface(self.image)
            self.rect.y += 7
         
        
    

        # Keep the player on screen
    
            
        
       

    
            
        # print("Jumping: " + str(self.isjumping)+ " Y: " +str(self.rect.y))


        #if self.rect.top > 0:
            
            
        

        


# Create a player object
player = Player()
player_group = pygame.sprite.GroupSingle(player)



# Add obstacles periodically
def add_obstacle(obstacles):
    # random.random() returns a random float between 0 and 1, so a value
    # of 0.25 means that there is a 25% chance of adding an obstacle. Since
    # add_obstacle() is called every 100ms, this means that on average, an
    # obstacle will be added every 400ms.
    # The combination of the randomness and the time allows for random
    # obstacles, but not too close together. 
    if random.random() < 0.4:
        obstacle = Obstacle()
        obstacles.add(obstacle)
        return 1
    return 0






# Main game loop
def game_loop():
    global game_over
    global passedobj
    global hiscore

    clock = pygame.time.Clock()
    
    last_obstacle_time = pygame.time.get_ticks()

    # Group for obstacles
    obstacles = pygame.sprite.Group()

    button = Button(220,100,60,150,'grey',"New Button",'black',)

    player = Player()
    player_group.add(player)

    obstacle_count = 0
    while True:
        while game_over == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            

            # Update player
            player.update()

            # Add obstacles and update
            if pygame.time.get_ticks() - last_obstacle_time > 500:
                last_obstacle_time = pygame.time.get_ticks()
                obstacle_count += add_obstacle(obstacles)
            
            obstacles.update()

            def point_in_triangle(px, py, p1, p2, p3):
                def sign(p1, p2, p3):
                    return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])
                
                b1= sign((px, py), p1, p2) < 0
                b2= sign((px, py), p2, p3) < 0
                b3= sign((px, py), p3, p1) < 0

                return b1 == b2 == b3

            # for obstacle in obstacles:
                
            #     collision = player.mask.overlap(obstacle.mask, (obstacle.rect.x-player.rect.x, obstacle.rect.y - player.rect.y))
            #     print(collision) 
                
            #     pygame.draw.rect(screen, BLUE, obstacle)

            #     if collision != None:
                    
            #         obstacle.explode()
            collider = pygame.sprite.spritecollide(player, obstacles, dokill=False)
            if collider:
                collider[0].explode()

            # Check for collisions
              
        
            # Draw everything
            screen.fill(WHITE)
            pygame.draw.rect(screen, BLUE, player)
            obstacles.draw(screen)
            player_group.draw(screen)

            # Display obstacle count
            obstacle_text = font.render(f"Obstacles: {passedobj}", True, BLACK)
            screen.blit(obstacle_text, (10, 10))
            if passedobj > hiscore:
                hiscore = passedobj
            obstacle_text = font.render(f"HIGHSCORE: {hiscore}", True, 'gold')
            screen.blit(obstacle_text, (10, 40))
            
            for obstacle in obstacles:
                pygame.draw.circle(screen, 'red', (obstacle.rect.x, obstacle.rect.y), 10)
                pygame.draw.rect(screen, BLUE, obstacle)
                
                

        


        
            pygame.display.update()
            clock.tick(FPS)

        # Game over screen
        
        while game_over == True:
            screen.fill(WHITE)
            button.button_draw()
            
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    return 0
        
            pygame.display.update()
            clock.tick(60)

            if button.button_clicked() == True:
                obstacles = pygame.sprite.Group()
                passedobj = 0
                
                game_over = False




class Button():
    def __init__(self, butx, buty, butwid, buthigh, butcolor, buttext, buttxtcolor):
        self.butx = 220
        self.buty = 100
        self.butwid = 60
        self.buthigh = 150
        self.butcolor = GREY
        self.buttext = 'Retry'
        self.buttxtcolor = BLACK

    def button_draw(self):
        pygame.draw.rect(screen, self.butcolor, (self.butx, self.buty, self.buthigh, self.butwid))
        buttontext = font.render(self.buttext, True, self.buttxtcolor)
        screen.blit(buttontext, (self.butx+((self.buthigh-141.89)/2), self.buty+((self.butwid-21.67)/2)))

    def button_clicked(self):
            if pygame.mouse.get_pos()[0] > self.butx and pygame.mouse.get_pos()[0] <  self.butx +self.buthigh and pygame.mouse.get_pos()[1] >  self.buty and pygame.mouse.get_pos()[1] <  self.buty + self.butwid and pygame.mouse.get_pressed()[0] == True:
                return True
            else:
                return False
        
                                    

        

        #     def custom_button(custombutx, custombuty, custombutwid,custombuthigh,color,custombuttext,txtcolor):
        #         pygame.draw.rect(screen, color, (custombutx, custombuty, custombuthigh, custombutwid))
        #         buttontext = font.render(custombuttext, True, txtcolor)
        #         screen.blit(buttontext, (custombutx+((custombuthigh-141.89)/2), custombuty+((custombutwid-21.67)/2)))

            

        #         if pygame.mouse.get_pos()[0] > custombutx:
        #             if pygame.mouse.get_pos()[0] < custombutx+custombuthigh:
        #                 if pygame.mouse.get_pos()[1] > custombuty:
        #                     if pygame.mouse.get_pos()[1] < custombuty+custombutwid:
        #                         print('on button')
        #                         if pygame.mouse.get_pressed()[0] == True:
        #                             global game_over
        #                             game_over = False
        #                             obstacles = pygame.sprite.Group()
            
        #     # button Parameters: (x, y, width, height, color, text, textcolor)
        #     #--------------------------------------------------------#
        #     for eveny in pygame.event.get():
        #         if event.type == pygame.MOUSEBUTTONUP:
        #             print(pygame.mouse.get_pos())
        #     print(str(game_over) + "game")   
        #     custom_button(220,100,60,150,'grey',"New Button",'black')
        #     pygame.display.update()
        #     clock.tick(60)
        # #--------------------------------------------------------#
        


 





if __name__ == "__main__":
    game_loop()
    

    