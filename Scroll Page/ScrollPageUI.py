import pygame
import pygame_gui
import consts

pygame.init()

pygame.display.set_caption('Volunteer app')

menu_screen = pygame.display.set_mode((800, 600))

background = pygame.Surface((800, 600))

background.fill(pygame.Color(consts.WHITE))
manager = pygame_gui.UIManager((800, 600))

volunteer = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((450, 175), (200, 200)),
                                            text='VOLUNTEER',
                                            manager=manager)
font = pygame.font.SysFont('Calibri', 50)
img = font.render('Welcome to holocaust volunteer app!', True, consts.BLACK)

survivor = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 175), (200, 200)),
                                            text='SURVIVOR',
                                            manager=manager)


clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == volunteer:
                print('Hello World!')

        manager.process_events(event)

    manager.update(time_delta)

    menu_screen.blit(background, (0, 0))
    menu_screen.blit(img, (30, 20))
    manager.draw_ui(menu_screen)

    pygame.display.update()