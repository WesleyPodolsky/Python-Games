"""
Gravity bounce using Vectors. 

This version of the Gravity Bounce program uses Pygame's Vector2 class to handle
the player's position and velocity. This makes the code more readable and
understandable, and makes it easier to add more complex features to the game.


"""
import pygame
from dataclasses import dataclass
from jtlgames.vector20 import Vector20Factory

class Colors:
    """Constants for Colors"""
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    PLAYER_COLOR = (0, 0, 255)
    BACKGROUND_COLOR = (255, 255, 255)


v_thrust = pygame.Vector2(5, -25)
v_movel =  pygame.Vector2(30, 1)
middle = 250,250

@dataclass
class GameSettings:
    """Settings for the game"""
    thrust: float = 0
    width: int = 500
    height: int = 500
    gravity: float = 0.3
    player_start_x: int = 100
    player_start_y: int = None
    player_v_y: float = 0  # Initial y velocity
    player_v_x: float = 4  # Initial x velocity
    player_width: int = 20
    player_height: int = 20
    player_jump_velocity: float = 15
    frame_rate: int = 15
    drag: float = 0


class Game:
    """Main object for the top level of the game. Holds the main loop and other
    update, drawing and collision methods that operate on multiple other
    objects, like the player and obstacles."""
    
    def __init__(self, settings: GameSettings):
        pygame.init()

        self.settings = settings
        self.running = True

        self.screen = pygame.display.set_mode((self.settings.width, self.settings.height))
        self.clock = pygame.time.Clock()

        # Turn Gravity into a vector
        self.gravity = pygame.Vector2(0, self.settings.gravity)

    def run(self):

        """Main game loop"""

        player = Player(self)

        while self.running:




            
            



            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    self.running = False

            player.update()

            #self.screen.fill(Colors.BACKGROUND_COLOR)
            player.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(self.settings.frame_rate)


            


        pygame.quit()

screen = pygame.display.set_mode((GameSettings.width, GameSettings.height))
pygame.display.set_caption("Vector with Arrow")
Vector20, draw_v20, draw_grid = Vector20Factory(GameSettings.width, GameSettings.height, 20)

class Player:
    """Player class, just a bouncing rectangle"""

    def __init__(self, game: Game):
        self.game = game
        settings = self.game.settings

        self.width = settings.player_width
        self.height = settings.player_height
    
        # Vector for our jump velocity, which is just up
        self.v_jump = pygame.Vector2(0, -settings.player_jump_velocity)
        #self.v_thrust = pygame.Vector2(0, 10)
        # Player position
        self.pos = pygame.Vector2(settings.player_start_x, 
                                  settings.player_start_y if settings.player_start_y is not None else settings.height - self.height)
        
        # Player's velocity
        self.vel = pygame.Vector2(settings.player_v_x, settings.player_v_y)  # Velocity vector
        self.drag = self.vel * 0.8
        self.vel = self.vel - self.drag


    # Direction functions. IMPORTANT! Using these functions isn't really
    # necessary, but it makes the code more readable. You could just use
    # self.vel.x < 0, but writing "self.going_left()" is a lot easier to read and
    # understand, it makes the code self-documenting. 

    def gotomiddle(self):
        self.pos.x=350
        self.pos.y=200


    def going_up(self):
        """Check if the player is going up"""
        return self.vel.y < 0
    
    def going_down(self):
        """Check if the player is going down"""
        return self.vel.y > 0
    
    def going_left(self):
        """Check if the player is going left"""
        return self.vel.x < 0
    
    def going_right(self):
        """Check if the player is going right"""
        return self.vel.x > 0
    

####update input#######
####update input#######
####update input#######
####update input#######

    def vec_to_center(self):
        global v_tomiddle
        v_tomiddle = pygame.Vector2(250-self.pos.x/self.pos.x-250, 250-self.pos.y/self.pos.y-250)

    def update_input(self):
        print('ADD THE TWO VECTORS HERE')
        self.vel = self.vel
        v_tomiddle = pygame.Vector2(250-self.pos.x, 250-self.pos.y)/500
        self.vel += v_tomiddle
        #draw_v20(screen, (self.pos.x-250, self.pos.y-250), v_thrust)
        pygame.draw.circle(screen, 'red', (self.pos.x,self.pos.y), 5, 25)
        
    
    

            
####update input#######
####update input#######
####update input#######
####update input#######
####update input#######


    # Location Fuctions
    
    def at_top(self):
        """Check if the player is at the top of the screen"""
        return self.pos.y <= 0
    
    def at_bottom(self):
        """Check if the player is at the bottom of the screen"""
        return self.pos.y >= self.game.settings.height - self.height

    def at_left(self):
        """Check if the player is at the left of the screen"""
        return self.pos.x <= 0
    
    def at_right(self):
        """Check if the player is at the right of the screen"""
        return self.pos.x >= self.game.settings.width - self.width
    
    
    # Updates
    

    def update(self):
        """Update player position, continuously jumping"""
        self.update_jump()
        self.update_v()
        self.update_pos()
        
    def update_v(self):
        """Update the player's velocity based on gravity and bounce on edges"""
         
        #self.vel += self.game.gravity  # Add gravity to the velocity

        # if self.at_bottom() and self.going_down():
        #     self.vel.y = 0

        # if self.at_top() and self.going_up():
        #     self.vel.y = -self.vel.y # Bounce off the top. 

        # # If the player hits one side of the screen or the other, bounce the
        # # player. we are also checking if the player has a velocity going farther
        # # off the screeen, because we don't want to bounce the player if it's
        # # already going away from the edge
        
        # if (self.at_left() and self.going_left() ) or ( self.at_right() and self.going_right()):
        #     self.vel.x = -self.vel.x
            
    def update_pos(self):
        """Update the player's position based on velocity"""
        self.pos += self.vel  # Update the player's position based on the current velocity

        # If the player is at the bottom, stop the player from falling and
        # stop the jump
        
        # if self.at_bottom():
        #     self.pos.y = self.game.settings.height - self.height

        # if self.at_top():
        #     self.pos.y = 0

        # # Don't let the player go off the left side of the screen
        # if self.at_left():
        #     self.pos.x = 0
  
        # # Don't let the player go off the right side of the screen
        # elif self.at_right():
        #     self.pos.x = self.game.settings.width - self.width

    def update_jump(self):
        """Handle the player's jumping logic"""
        
    
        # Notice that we've gotten rid of self.is_jumping, because we can just
        # check if the player is at the bottom. 

        # if self.at_bottom():
        #     self.vel += self.v_jump
         
    

    def draw(self, screen):
        Player.update_input(self)
        global v_thrust
        # if self.pos.y == 480:
        #     self.drag = self.vel * 0.4
        # self.vel = self.vel - self.drag
        #pygame.draw.line(screen, 'red', (self.pos.x +7, self.pos.y), (250, 250), 2)
        pygame.draw.circle(screen, 'green', (250,250), 50, 25)
        
        #pygame.draw.rect(screen, Colors.PLAYER_COLOR, (self.pos.x, self.pos.y, self.width, self.height))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            if self.pos.y == 480:
                print('spoce')
            Player.update_input(self)
        if keys[pygame.K_RIGHT]:
            print('>')
            v_thrust.rotate_ip(10)
        if keys[pygame.K_UP]:
            print('^')
            v_thrust.scale_to_length(v_thrust.length() + 5)
        if keys[pygame.K_DOWN]:
            print('v')
            v_thrust.scale_to_length(v_thrust.length() - 5)
        if keys[pygame.K_LEFT]:
            print('<')
            v_thrust.rotate_ip(-10)
        if keys[pygame.K_j]:
            print('test')
            v_movel = pygame.Vector2(1,0)
            #go torwards it using vector seperately <broken>
            self.vel = self.vel
            self.vel += v_movel
        if keys[pygame.K_k]:

            print('reL')
            v_movel = pygame.Vector2(0,-5)
            #go torwards it using vector seperately <broken>
            Player.gotomiddle(self)
            
        # draw_v20(screen, self.pos, v_thrust)
        
        


pygame.display.flip()
settings = GameSettings()
game = Game(settings)
game.run()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()