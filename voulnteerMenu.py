import pygame
import pygame_gui
import Window


def main():
    pygame.init()

    pygame.display.set_caption('Volunteer app')
    manager = pygame_gui.UIManager((800, 600))

    voulnteer_screen = pygame.display.set_mode((800, 600))
    voulnteer_screen.fill(pygame.Color(Window.WHITE))

    backButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 0), (100, 40)),
                                              text='back',
                                              manager=manager)
    clock = pygame.time.Clock()
    while True:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pass
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == backButton:
                    return
            manager.process_events(event)
        manager.update(time_delta)
        manager.draw_ui(voulnteer_screen)
        pygame.display.update()
