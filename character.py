import pygame
import time
import os

# Initialize Pygame
pygame.init()
window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Samurai Walk Animation")

walkl = [
    pygame.image.load(os.path.join("scen samurai walkl", "walk1.png")),
    pygame.image.load(os.path.join("scen samurai walkl", "walk2.png")),
    pygame.image.load(os.path.join("scen samurai walkl", "walk3.png")),
    pygame.image.load(os.path.join("scen samurai walkl", "walk4.png")),
    pygame.image.load(os.path.join("scen samurai walkl", "walk6.png")),
    pygame.image.load(os.path.join("scen samurai walkl", "walk7.png")),
    pygame.image.load(os.path.join("scen samurai walkl", "walk8.png"))
]

walkr = [
    pygame.image.load(os.path.join("scen samurai walk", "walk1.png")),
    pygame.image.load(os.path.join("scen samurai walk", "walk2.png")),
    pygame.image.load(os.path.join("scen samurai walk", "walk3.png")),
    pygame.image.load(os.path.join("scen samurai walk", "walk4.png")),
    pygame.image.load(os.path.join("scen samurai walk", "walk6.png")),
    pygame.image.load(os.path.join("scen samurai walk", "walk7.png")),
    pygame.image.load(os.path.join("scen samurai walk", "walk8.png"))
]

coich = [walkl, walkr]

# Character variables
x = 250
y = 250
vel = 5
frame = 0

# Main loop
run = True
clock = pygame.time.Clock()

while run:
    clock.tick(30)  # Setting the frame rate to 30 frames per second
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Handling key inputs
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= vel
        framet = (frame + 1) % len(coich[0])
        toWindow = window.blit(walkr[frame], (x, y))
    if keys[pygame.K_RIGHT]:
        x += vel
        frame = (frame + 1) % len(coich[1])
        toWindow = window.blit(walkr[frame], (x, y))
    if keys[pygame.K_UP]:
        y -= vel
        frame = (frame + 1) % len(walkr)
    if keys[pygame.K_DOWN]:
        y += vel
        frame = (frame + 1) % len(walkr)

    # Update frame index for animation

    # Clear the screen
    window.fill((0, 0, 0))

    # Draw the current frame of the walk cycle at the character's position
    toWindow = window.blit(walkr[frame], (x, y))
    # Update the display
    pygame.display.update()

pygame.quit()
