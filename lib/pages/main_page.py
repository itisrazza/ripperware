from state import page_manager
from ui.button import Button
from ui.page import Page
from ui.manager import PageState
from ui.title_label import TitleLabel
from pages.disc_meta_page import DiscMetaPage


class MainPage(PageState):
    def __init__(self) -> None:
        super().__init__()
        self.page_layout = Page(
            leading_items=[TitleLabel("RipperWare")],
            trailing_items=[
                Button(
                    icon="disc-rip",
                    title="Rip",
                    action=lambda: self.on_rip_clicked(),
                ),
                Button(icon="disc-burn", title="Burn"),
                Button(icon="folder", title="Browse"),
                Button(icon="settings", title="Settings"),
            ],
        )

    def get_page(self) -> Page:
        return self.page_layout

    def on_rip_clicked(self):
        page_manager.push(DiscMetaPage())
