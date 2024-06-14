import pygame
from pygame.locals import *
import random

# Initialize Pygame
pygame.init()

# Define constants
width = 500
height = 500
screen_size = (width, height)
gray = (100, 100, 100)
green = (76, 208, 56)
red = (200, 0, 0)
white = (255, 255, 255)
yellow = (255, 232, 0)
fps = 120

# Define game settings
speed = 2
score = 0

# Define marker sizes and road layout
marker_width = 10
marker_height = 50
road = (100, 0, 300, height)
left_edge_marker = (95, 0, marker_width, height)
right_edge_marker = (395, 0, marker_width, height)
left_lane = 150
center_lane = 250
right_lane = 350
lanes = [left_lane, center_lane, right_lane]
lane_marker_move_y = 0

# Define desired width for car images
desired_width = 30  

class PlayerVehicle(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.original_image = image  
        self.image = pygame.transform.scale(self.original_image, (desired_width, int(self.original_image.get_rect().height * (desired_width / self.original_image.get_rect().width))))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

        # Get the width of the player's car image
        self.player_width = self.image.get_rect().width

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[K_LEFT] and self.rect.centerx > left_lane:
            self.rect.centerx -= speed
        if keys[K_RIGHT] and self.rect.centerx < right_lane:
            self.rect.centerx += speed


class Vehicle(pygame.sprite.Sprite):
    def __init__(self, image, x, y, player_width):
        super().__init__()
        self.original_image = image  
        self.image = pygame.transform.scale(self.original_image, (player_width, int(self.original_image.get_rect().height * (player_width / self.original_image.get_rect().width))))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        self.rect.y += speed


# Main game function
def start_game():
    global vehicle_images

    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Car Game")

    player_image = pygame.image.load("images/car.png")
    crash_image = pygame.image.load("images/crash.png")

    player = PlayerVehicle(player_image, 250, 400)
    player_group = pygame.sprite.Group(player)

    vehicle_images = [pygame.image.load(f'images/{img}') for img in ['pickup_truck.png', 'semi_trailer.png', 'taxi.png', 'van.png']]

    vehicle_group = pygame.sprite.Group()

    gameover = game_loop(screen, player_group, vehicle_group, player, crash_image)

    if gameover:
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    return
                if event.type == KEYDOWN:
                    if event.key == K_y:
                        start_game()
                    elif event.key == K_n:
                        pygame.quit()
                        return


# Game loop
def game_loop(screen, player_group, vehicle_group, player, crash_image):
    global speed, score, lane_marker_move_y
    clock = pygame.time.Clock()
    running = True
    gameover = False

    while running:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        # Move the player's car using the left/right arrow keys
        keys = pygame.key.get_pressed()
        if keys[K_LEFT] and player.rect.centerx > left_lane:
            player.rect.centerx -= speed
        if keys[K_RIGHT] and player.rect.centerx < right_lane:
            player.rect.centerx += speed

        # Update player position
        player_group.update()

        # Handle vehicle creation and movement
        if random.randint(0, 50) == 1:
            random_lane = random.choice(lanes)
            random_vehicle = random.choice(vehicle_images)
            # Pass the player's width to the Vehicle constructor
            new_vehicle = Vehicle(random_vehicle, random_lane, -50, player.player_width)
            vehicle_group.add(new_vehicle)
        vehicle_group.update()

        # Remove vehicles that go off-screen
        for vehicle in vehicle_group:
            if vehicle.rect.top > height:
                vehicle_group.remove(vehicle)
                score += 1

        # Check for collisions between player and other vehicles
        if pygame.sprite.spritecollideany(player, vehicle_group):
            gameover = True
            running = False

        # Draw game elements
        screen.fill(gray)
        pygame.draw.rect(screen, green, road)
        pygame.draw.rect(screen, yellow, left_edge_marker)
        pygame.draw.rect(screen, yellow, right_edge_marker)

        # Update lane markers
        lane_marker_move_y += speed
        if lane_marker_move_y > marker_height:
            lane_marker_move_y = 0

        # Draw lane markers
        for lane in lanes:
            pygame.draw.rect(screen, white, (lane - marker_width // 2, lane_marker_move_y, marker_width, marker_height))

        # Draw sprites
        player_group.draw(screen)
        vehicle_group.draw(screen)

        # Display score
        font = pygame.font.Font(None, 36)
        text = font.render(f"Score: {score}", True, white)
        screen.blit(text, (10, 10))

        # Update display
        pygame.display.flip()

    # Game over screen
    if gameover:
        screen.blit(crash_image, (width // 2 - crash_image.get_width() // 2, height // 2 - crash_image.get_height() // 2))
        font = pygame.font.Font(None, 48)
        text = font.render("Game Over!", True, red)
        text_rect = text.get_rect(center=(width // 2, height // 2 - 50))
        screen.blit(text, text_rect)
        text = font.render(f"Score: {score}", True, white)
        text_rect = text.get_rect(center=(width // 2, height // 2 + 50))
        screen.blit(text, text_rect)
        text = font.render("Play Again? (Y/N)", True, white)
        text_rect = text.get_rect(center=(width // 2, height // 2 + 100))
        screen.blit(text, text_rect)
        pygame.display.flip()

    return gameover

# Start the game
start_game()