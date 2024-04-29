import pygame


class Icon:
    """Icon utilities"""

    def __init__(self, name: str, scale: int = 24) -> None:
        """Creates a new Icon object"""
        self.name = name
        self.scale = scale
        self.image = pygame.image.load(f"assets/icons/{name}-{scale}.png")
