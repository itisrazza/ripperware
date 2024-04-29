import pygame
from typing import Callable

from ui.colours import COLOR_ACTIVE, COLOR_BACKGROUND, COLOR_BORDER, COLOR_FOREGROUND
from ui.icon import Icon
from ui.component import Component
from ui.text import Text


class Button(Component):
    def __init__(
        self,
        title: str | None = None,
        icon: str | None = None,
        action: Callable | None = None,
    ) -> None:
        self.title = title
        self.icon = Icon(icon, 48) if icon is not None else None
        self.action = action
        self.active = False

    def render(self, target, bbox):
        bbox_left, bbox_top, bbox_w, bbox_h = bbox

        target.fill(
            COLOR_BACKGROUND if not self.active else COLOR_ACTIVE,
            bbox,
        )
        pygame.draw.rect(
            target,
            COLOR_BORDER,
            (bbox_left, bbox_top, bbox_w, 1),
        )

        if self.icon is not None:
            target.blit(self.icon.image, (bbox_left + 16, bbox_top + 8, 48, 48))

        if self.title is not None:
            title_rendered = Text.body_std().render(self.title, True, COLOR_FOREGROUND)
            _, title_h = Text.body_std().size(self.title)
            target.blit(
                title_rendered,
                (
                    bbox_left + 80,
                    bbox_top + bbox_h / 2 - title_h / 2,
                ),
            )

    def do_action(self):
        if self.action is None:
            return
        self.action()

    def size(self):
        return (None, 64)

    def __repr__(self) -> str:
        return f"Button(title='{self.title}', icon='{self.icon.name}', action={'set' if self.action is not None else 'none'})"
