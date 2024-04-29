from state import page_manager
from ui.button import Button
from ui.page import Page
from ui.manager import PageState


class DiscMetaPage(PageState):
    def __init__(self) -> None:
        super().__init__()
        self.page_layout = Page(
            trailing_items=[
                Button(
                    icon="back",
                    title="Back",
                    action=lambda: self.on_back_clicked(),
                ),
                Button(
                    icon="disc-rip",
                    title="Rip",
                ),
            ]
        )

    def on_back_clicked(self):
        page_manager.pop()

    def get_page(self) -> Page:
        return self.page_layout
