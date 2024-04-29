import pygame
from pages.main_page import MainPage
from ui import Page, Button
from state import page_manager
from ui.colours import COLOR_BACKGROUND
from util import app_version

DISPLAY_SIZE = DISPLAY_WIDTH, DISPLAY_HEIGHT = 320, 480

if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode(DISPLAY_SIZE, pygame.RESIZABLE)
    running = True

    page_manager.reset(MainPage())
    page_manager.commit()

    background = "purple" if app_version() == "testmode" else COLOR_BACKGROUND

    while running:
        for event in pygame.event.get():
            # lifecycle events

            if event.type == pygame.QUIT:
                running = False

            # mouse events

            if event.type == pygame.MOUSEMOTION:
                page_manager.send_mouse_event(event.pos, None)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                page_manager.send_mouse_event(event.pos, "down")
            elif event.type == pygame.MOUSEBUTTONUP:
                page_manager.send_mouse_event(event.pos, "up")

            #     clicked_item = page.point_to(event.pos, screen)
            #     if clicked_item is not None:
            #         print(f"got {clicked_item}")
            #         clicked_item.active = True
            # if event.type == pygame.MOUSEBUTTONUP:
            #     clicked_item = page.point_to(event.pos, screen)
            #     if clicked_item is not None:
            #         print(f"got {clicked_item}")
            #         clicked_item.active = False

        screen.fill("purple")
        page_manager.render(screen)

        pygame.display.flip()
        page_manager.commit()

    pygame.quit()
