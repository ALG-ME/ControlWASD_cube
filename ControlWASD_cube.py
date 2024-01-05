import pygame

# Что бы всё работало корректно нужна инициализация, проверяет всё ли на месте
# pygame.init()

# Каркас

# Кастомный размер
# size = [800, 600]

# Разрешение экрана
# pygame.display.set_mode((600, 400))  # Передаём разрешение через картеж
# pygame.display.set_mode(size, pygame.RESIZABLE)  # Передаём разрешение через переменную
# clock = pygame.time.Clock()  # Время для корректной работы

# Проверка работы приложения заводим его в цикл
size = [800, 600]
screen = pygame.display.set_mode(size)
action = True
x = 30
y = 30
clock = pygame.time.Clock()

while action:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            action = False
        if event.type == pygame.K_DOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        y -= 3
    if pressed[pygame.K_DOWN]:
        y += 3
    if pressed[pygame.K_LEFT]:
        x -= 3
    if pressed[pygame.K_RIGHT]:
        x += 3

    is_blue = 0
    if is_blue:
        color = (0, 128, 255)
    else:
        color = (255, 100, 0)

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))
    pygame.display.flip()
    clock.tick(60)
