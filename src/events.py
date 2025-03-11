import pygame

from src.enterprise.value_objects import Vector

class Events:

    KEY_1_DOWN : bool = False
    KEY_2_DOWN : bool = False

    KEY_1_UP : bool = False
    KEY_2_UP : bool = False

    CTRL_DOWN: bool = False
    CTRL_PRESSED : bool = False
    CTRL_UP: bool = False

    KEY_S_DOWN : bool = False
    KEY_L_DOWN : bool = False

    MOUSE_LEFT_BUTTON_DOWN : bool = False
    MOUSE_MIDDLE_BUTTON_DOWN : bool = False
    MOUSE_RIGHT_BUTTON_DOWN : bool = False

    MOUSE_LEFT_BUTTON_UP : bool = False
    MOUSE_MIDDLE_BUTTON_UP : bool = False
    MOUSE_RIGHT_BUTTON_UP : bool = False

    MOUSE_MOVING : bool = False

    MOUSE_POS : Vector = None

    QUIT : bool = False

    def reset():
        Events.MOUSE_LEFT_BUTTON_DOWN = False
        Events.MOUSE_MIDDLE_BUTTON_DOWN = False
        Events.MOUSE_RIGHT_BUTTON_DOWN = False
        Events.MOUSE_LEFT_BUTTON_UP = False
        Events.MOUSE_MIDDLE_BUTTON_UP = False
        Events.MOUSE_RIGHT_BUTTON_UP = False
        Events.KEY_1_DOWN = False
        Events.KEY_2_DOWN = False
        Events.KEY_1_UP = False
        Events.KEY_2_UP = False
        Events.CTRL_DOWN = False
        Events.CTRL_UP = False
        Events.KEY_S_DOWN = False
        Events.KEY_L_DOWN = False

    def capture():
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key == 49:
                    Events.KEY_1_DOWN = True
                if event.key == 50:
                    Events.KEY_2_DOWN = True
                if event.key == 1073742048:
                    Events.CTRL_DOWN = True
                    Events.CTRL_PRESSED = True
                if event.key == 115:
                    Events.KEY_S_DOWN = True
                if event.key == 108:
                    Events.KEY_L_DOWN = True
            if event.type == pygame.KEYUP:
                if event.key == 49:
                    Events.KEY_1_UP = True
                if event.key == 50:
                    Events.KEY_2_UP = True
                if event.key == 1073742048:
                    Events.CTRL_PRESSED = False
                    Events.CTRL_UP = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    Events.MOUSE_LEFT_BUTTON_DOWN = True
                if event.button == 2:
                    Events.MOUSE_MIDDLE_BUTTON_DOWN = True
                if event.button == 3:
                    Events.MOUSE_RIGHT_BUTTON_DOWN = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    Events.MOUSE_LEFT_BUTTON_UP = True
                if event.button == 2:
                    Events.MOUSE_MIDDLE_BUTTON_UP = True
                if event.button == 3:
                    Events.MOUSE_RIGHT_BUTTON_UP = True
            if event.type == pygame.MOUSEMOTION:
                Events.MOUSE_MOVING = True
                Events.MOUSE_POS = Vector(event.pos[0], event.pos[1])
            else:
                Events.MOUSE_MOVING = False
            if event.type == pygame.QUIT:
                Events.QUIT = True