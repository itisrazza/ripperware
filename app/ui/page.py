from pygame import Surface

from ui.component import BBox, Component, Point, Size

from util import ifnone


class Page:
    def __init__(
        self,
        items: list[Component] = [],
        leading_items: list[Component] = [],
        trailing_items: list[Component] = [],
        scrollable: bool = False,
    ):
        """
        Keyword arguments:
        items -- the items contained within the page
        leading_items -- the items displayed at the top of the page
        trailing_items -- the items displayed at the bottom of the page
        scrollable -- whether the page scrolls if the items overflow the contents
        """

        self.items = items
        self.leading_items = leading_items
        self.trailing_items = trailing_items
        self.scrollable = scrollable
        self.scroll_offset = 0

    def point_to(self, point: Point, view_size: Size) -> Component:
        for item, bbox in self._perform_layout(view_size):
            if item.point_to(point, bbox) is not None:
                return item

        return None

    def render(self, target: Surface):
        for item, bbox in self._perform_layout(target.get_size()):
            item.render(target, bbox)

    def _perform_layout(self, size: tuple[int, int]) -> list[tuple[Component, BBox]]:
        layout_width, layout_height = size

        layout = []

        items_layout_top = 0
        items_layout_bottom = 0

        layout_y_pos = 0
        for item in self.leading_items:
            item_width, item_height = item.size()
            item_width = ifnone(item_width, layout_width)
            item_height = ifnone(item_height, 0)

            layout.append((item, (0, layout_y_pos, item_width, item_height)))
            layout_y_pos += item_height
        items_layout_top = layout_y_pos

        layout_y_pos = layout_height
        for item in reversed(self.trailing_items):
            item_width, item_height = item.size()
            item_width = ifnone(item_width, layout_width)
            item_height = ifnone(item_height, 0)

            layout_y_pos -= item_height
            layout.append((item, (0, layout_y_pos, item_width, item_height)))
        items_layout_bottom = layout_y_pos

        layout_y_pos = items_layout_top
        for item in self.items:
            item_width, item_height = item.size()
            item_width = ifnone(item_width, layout_width)
            item_height = ifnone(item_height, 0)

            layout.append((item, (0, layout_y_pos, item_width, item_height)))
            layout_y_pos += item_height

        return layout
