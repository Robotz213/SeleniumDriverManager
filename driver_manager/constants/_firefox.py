"""Forneca recursos do modulo constants."""

FIREFOX_ARGUMENTS = [
    "--width=1360",
    "--height=768",
]

FIREFOX_PREFERENCES = {
    "browser.download.folderList": 2,
    "browser.download.dir": "",
    "browser.download.useDownloadDir": True,
    "browser.download.manager.showWhenStarting": False,
    "browser.download.alwaysOpenPanel": False,
    "browser.helperApps.neverAsk.saveToDisk": (
        "application/pdf,application/octet-stream,application/zip,text/csv"
    ),
    "pdfjs.disabled": True,
    "browser.download.viewableInternally.enabledTypes": "",
    "credentials_enable_service": False,
    "signon.rememberSignons": False,
    "signon.management.page.breach-alerts.enabled": False,
    "signon.management.page.password-notification.disabled": True,
    "dom.webnotifications.enabled": False,
    "geo.enabled": False,
    "media.volume_scale": "0.0",
    "print.always_print_silent": True,
    "print.show_print_progress": False,
}
