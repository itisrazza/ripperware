from util import app_version
from state import page_manager
from ui.button import Button
from ui.page import Page
from ui.manager import PageState
from ui.title_label import TitleLabel
from pages.disc_meta_page import DiscMetaPage
from pages.settings_page import SettingsPage


class MainPage(PageState):
    def __init__(self) -> None:
        super().__init__()
        self.page_layout = Page(
            leading_items=[TitleLabel(app_version())],
            trailing_items=[
                Button(
                    icon="disc-rip",
                    title="Rip",
                    action=lambda: self.on_rip_clicked(),
                ),
                Button(icon="disc-burn", title="Burn"),
                Button(icon="folder", title="Browse"),
                Button(icon="settings", title="Settings", action=lambda: self.on_settings_clicked()),
            ],
        )

    def get_page(self) -> Page:
        return self.page_layout

    def on_rip_clicked(self):
        page_manager.push(DiscMetaPage())

    def on_settings_clicked(self):
        page_manager.push(SettingsPage())
