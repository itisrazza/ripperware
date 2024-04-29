from ui.button import Button
from ui.title_label import TitleLabel
from ui.page import Page
from ui.manager import PageState
from state import page_manager
import subprocess


class SettingsPage(PageState):
    def __init__(self) -> None:
        super().__init__()
        self.page_layout = Page(
            scrollable=True,
            leading_items=[
                TitleLabel("Settings"),
                Button(
                    icon="back",
                    title="Back",
                    action=lambda: self.on_back_clicked(),
                ),
            ],
            items=[
                Button(icon="update", title="Update"),
                Button(icon="disc", title="CD/DVD"),
                Button(icon="network", title="Network"),
                Button(icon="settings", title="System"),
                Button(icon="info", title="About"),
                Button(
                    icon="power",
                    title="Power",
                    action=lambda: self.on_power_clicked(),
                ),
            ],
        )

    def get_page(self) -> Page:
        return self.page_layout

    def on_back_clicked(self):
        page_manager.pop()

    def on_power_clicked(self):
        page_manager.push(PowerPage())


class PowerPage(PageState):
    def __init__(self) -> None:
        super().__init__()
        self.page_layout = Page(
            leading_items=[
                TitleLabel("Power"),
                Button(
                    icon="back",
                    title="Back",
                    action=lambda: self.on_back_clicked(),
                ),
            ],
            items=[
                Button(
                    icon="shutdown",
                    title="Shut Down",
                    action=lambda: self.on_shutdown_clicked(),
                ),
                Button(
                    icon="restart",
                    title="Restart",
                    action=lambda: self.on_restart_clicked(),
                ),
            ],
        )

    def get_page(self) -> Page:
        return self.page_layout

    def on_shutdown_clicked(self):
        subprocess.run(["shutdown", "now"])

    def on_restart_clicked(self):
        subprocess.run(["reboot"])

    def on_back_clicked(self):
        page_manager.pop()
