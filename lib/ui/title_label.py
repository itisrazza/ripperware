from ui.colours import COLOR_FOREGROUND
from ui.component import Component
from ui.text import Text


class TitleLabel(Component):
    def __init__(self, text: str) -> None:
        super().__init__()
        self.text = text

    def render(self, target, bbox):
        bbox_x, bbox_y, _, bbox_h = bbox
        text_rendered = Text.title().render(self.text, True, COLOR_FOREGROUND)
        _, text_h = Text.title().size(self.text)
        target.blit(
            text_rendered,
            (
                bbox_x + 16,
                bbox_y + bbox_h / 2 - text_h / 2,
            ),
        )

    def size(self) -> tuple[int | None, int | None]:
        return (None, 55)

    def point_to(
        self, point: tuple[int, int], bbox: tuple[int, int, int, int]
    ) -> Component:
        # this component has no interaction
        return None
