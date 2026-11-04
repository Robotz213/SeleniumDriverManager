from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable

    from _manager_types import (
        ChromePreferences,
        ChromeSettings,
    )

    type Exc = Iterable[type[Exception]]

CHROME_SETTINGS: ChromeSettings = {
    "recentDestinations": [
        {"id": "Save as PDF", "origin": "local", "account": ""},
    ],
    "selectedDestinationId": "Save as PDF",
    "version": 2,
}
CHROME_ARGUMENTS = [
    "--ignore-ssl-errors=yes",
    "--ignore-certificate-errors",
    "--window-size=1360,768",
    "--kiosk-printing",
    "--disable-gpu",
    "--disable-dev-shm-usage",
    "--disable-software-rasterizer",
    "--disable-background-timer-throttling",
    "--disable-renderer-backgrounding",
    "--disable-backgrounding-occluded-windows",
    "--disable-blink-features=AutomationControlled",
    "--disable-features=MediaFoundationVideoCapture,VizDisplayCompositor,Translate,BackForwardCache",
    "--disable-extensions",
    "--disable-sync",
    "--disable-background-networking",
    "--disable-default-apps",
    "--disable-component-update",
    "--no-first-run",
    "--no-default-browser-check",
    "--disable-notifications",
    "--disable-geolocation",
    "--mute-audio",
    "--hide-scrollbars",
    "--metrics-recording-only",
    "--safebrowsing-disable-auto-update",
    "--no-sandbox",
]
CHROME_PREFERENCES: ChromePreferences = {
    "download.prompt_for_download": False,
    "plugins.always_open_pdf_externally": True,
    "profile.default_content_settings.popups": 0,
    "printing.print_preview_sticky_settings.appState": CHROME_SETTINGS,
    "download.default_directory": "",
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False,
    "profile.password_manager_leak_detection": False,
}
