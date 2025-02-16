import pygame

# Initialize the game
pygame.init()
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My First Game")

# Objects

# cordinate
x = 250
y = 250

#size
width = 20
height = 20

#speed
speed = 5

# Game Loop
running = True
while running:
    pygame.time.delay(10)
    #User Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and x > 0:
        x -= speed
    if key[pygame.K_RIGHT] and x < 800 - width:
        x += speed
    if key[pygame.K_UP] and y > 0:
        y -= speed
    if key[pygame.K_DOWN] and y < 600 - height:
        y += speed
    
    # Update Assets
    window.fill((255, 255, 255))
    pygame.draw.rect(window, (255, 0, 0), (x, y, width, height))
    pygame.display.update()


pygame.quit()