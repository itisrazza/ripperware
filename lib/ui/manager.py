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
    def __init__(self) -> None:
        self.mouse_down: bool = False
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

        if button == "down":
            self.mouse_down = True
        elif button == "up":
            self.mouse_down = False

        if self.mouse_down:
            item_under_mouse = self.get_page().point_to(point, view_size)
            if self.mouse_over_item is not None:
                self.mouse_over_item.active = False

            self.mouse_over_item = item_under_mouse
            if self.mouse_over_item is not None:
                self.mouse_over_item.active = True

            print(f"item_under_mouse={item_under_mouse}")
        else:
            if self.mouse_over_item is not None:
                self.mouse_over_item.active = False
                self.mouse_over_item.do_action()
            self.mouse_over_item = None
