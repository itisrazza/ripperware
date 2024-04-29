from abc import abstractmethod

from pygame import Surface
from ui.component import Component, Point, Size
from ui.page import Page


class PageManager:
    def __init__(self) -> None:
        self.size: Size = (320, 480)
        self.stack: list[PageState] = []
        self.changes: list[tuple[str, PageState | None]] = []

    def commit(self):
        changes = self.changes
        self.changes = []

        for change, state in changes:
            if change == "push":
                self.stack.append(state)
                state.mount()
            elif change == "pop":
                state = self.stack.pop()
                state.unmount()
            elif change == "reset":
                for state in self.stack:
                    state.unmount()
                self.stack = [state]
                state.mount()
            else:
                raise ValueError(f"unsupported stack operation '{change}'")

    def reset(self, state: "PageState"):
        self.changes.append(("reset", state))

    def push(self, state: "PageState"):
        self.changes.append(("push", state))

    def pop(self):
        self.changes.append(("pop", None))

    def peek(self) -> "PageState":
        return self.stack[-1]

    def peek_page(self) -> Page:
        return self.peek().get_page()

    def render(self, target: Surface):
        self.size = target.get_size()
        self.peek_page().render(target)

    def send_mouse_event(self, point: Point, button: str | None):
        self.peek().on_mouse_event(point, button, self.size)


class PageState:
    _SCROLL_OFFSET_THRES = 8

    def __init__(self) -> None:
        self.mouse_down: Point | bool = False
        self.scroll_offset_start: int | None = None
        self.mouse_over_item: Component | None = None

    @abstractmethod
    def get_page(self) -> Page:
        """
        Returns the page layout of this state.
        """
        ...

    def mount(self):
        """
        Called when the page is added to the page stack.
        """
        pass

    def unmount(self):
        """
        Called when the page is removed from the page stack.
        """
        pass

    def on_mouse_event(self, point: Point, button: str | None, view_size: Size):
        """
        Called when a mouse even is received.

        The default implementation provides rudimentary clicky things.

        Arguments:
        point  -- whether mouse is found
        button -- whether mouse button is "down" / "up"
        """

        ignore_mouse_input = False

        if button == "down":
            self.mouse_down = point
        elif button == "up":
            self.mouse_down = False

        page = self.get_page()
        if page.scrollable and self.mouse_down:
            if self.scroll_offset_start is None:
                self.scroll_offset_start = page.scroll_offset

            content_height, view_height = page.get_content_height(view_size)

            offset = self.mouse_down[1] - point[1]
            if abs(offset) >= 8:
                page.scroll_offset = self.scroll_offset_start + offset
                if self.mouse_over_item is not None:
                    self.mouse_over_item.active = False
                self.mouse_over_item = None
                ignore_mouse_input = True

            if page.scroll_offset < 0:
                page.scroll_offset = 0
            if page.scroll_offset > content_height - view_height:
                page.scroll_offset = content_height - view_height

        if not ignore_mouse_input:
            if self.mouse_down != False:
                item_under_mouse = page.point_to(point, view_size)
                if self.mouse_over_item is not None:
                    self.mouse_over_item.active = False

                self.mouse_over_item = item_under_mouse
                if self.mouse_over_item is not None:
                    self.mouse_over_item.active = True
            else:
                if self.mouse_over_item is not None:
                    self.mouse_over_item.active = False
                    self.mouse_over_item.do_action()
                self.mouse_over_item = None
