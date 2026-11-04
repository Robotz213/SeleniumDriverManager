from collections.abc import Sequence
from typing import (
    Literal,
    NotRequired,
    TypedDict,
)

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

class RecentDestinations(TypedDict):
    id: str
    origin: str
    account: str

class ChromeSettings(TypedDict):
    """Descreva o contrato de dados settings."""

    recentDestinations: list[RecentDestinations]
    selectedDestinationId: str
    version: int

class ChromeDriverKwargs(TypedDict):
    """Descreva o contrato de dados chrome driver kwargs."""

    options: NotRequired[Options]
    service: NotRequired[Service]

class SeleniumWireOptions(TypedDict, total=False):
    """Descreva o contrato de dados selenium wire options."""

    addr: str
    port: int
    exclude_hosts: Sequence[str]
    standalone: bool

class RectWebElement(TypedDict):
    """Descreva o contrato de dados rect web element."""

    height: float
    width: float
    x: float
    y: float

type SeWireArguments = list[str]
ChromePreferences = TypedDict(
    "ChromePreferences",
    {
        "download.prompt_for_download": bool,
        "plugins.always_open_pdf_externally": bool,
        "profile.default_content_settings.popups": int,
        "printing.print_preview_sticky_settings.appState": ChromeSettings,
        "download.default_directory": str,
        "credentials_enable_service": bool,
        "profile.password_manager_enabled": bool,
        "profile.password_manager_leak_detection": bool,
    },
)

type ContentTypes = Literal[
    "application/pdf,application/octet-stream,application/zip,text/csv"
]

FirefoxPreferences = TypedDict(
    "FirefoxPreferences",
    {
        "browser.download.folderList": int,
        "browser.download.dir": str,
        "browser.download.useDownloadDir": Literal[True],
        "browser.download.manager.showWhenStarting": Literal[False],
        "browser.download.alwaysOpenPanel": Literal[False],
        "browser.helperApps.neverAsk.saveToDisk": ContentTypes,
        "pdfjs.disabled": Literal[True],
        "browser.download.viewableInternally.enabledTypes": str,
        "credentials_enable_service": Literal[False],
        "signon.rememberSignons": Literal[False],
        "signon.management.page.breach-alerts.enabled": Literal[False],
        "signon.management.page.password-notification.disabled": Literal[True],
        "dom.webnotifications.enabled": Literal[False],
        "geo.enabled": Literal[False],
        "media.volume_scale": float,
        "print.always_print_silent": Literal[True],
        "print.show_print_progress": Literal[False],
    },
)
