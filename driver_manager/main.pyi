from pathlib import Path
from typing import ClassVar, Literal, TypedDict, overload

from selenium.webdriver import Chrome as SeChrome
from selenium.webdriver import ChromeOptions, FirefoxOptions
from selenium.webdriver import Firefox as SeFirefox
from selenium.webdriver.support.wait import WebDriverWait
from seleniumwire.webdriver import Chrome as WiredChrome
from seleniumwire.webdriver import Firefox as WiredFirefox

class Drivers(TypedDict):
    chrome: type[SeChrome]
    firefox: type[SeFirefox]

class WiredDrivers(TypedDict):
    chrome: type[WiredChrome]
    firefox: type[WiredFirefox]

class DriverManager[D]:
    SE_DRIVER: ClassVar[Drivers]
    WIRED_DRIVER: ClassVar[WiredDrivers]
    wait: WebDriverWait[D]  # pyright: ignore[reportInvalidTypeArguments]

    @overload
    def __init__(
        self: DriverManager[SeFirefox],
        browser: Literal["firefox"],
        options: FirefoxOptions,
        *,
        wired: Literal[False] = False,
        download_path: Path | None = None,
    ) -> None: ...
    @overload
    def __init__(
        self: DriverManager[WiredFirefox],
        browser: Literal["firefox"],
        options: FirefoxOptions,
        *,
        wired: Literal[True] = True,
        download_path: Path | None = None,
    ) -> None: ...
    @overload
    def __init__(
        self: DriverManager[SeChrome],
        browser: Literal["chrome"],
        options: ChromeOptions,
        *,
        wired: Literal[False] = False,
        download_path: Path | None = None,
    ) -> None: ...
    @overload
    def __init__(
        self: DriverManager[WiredChrome],
        browser: Literal["chrome"],
        options: ChromeOptions,
        *,
        wired: Literal[True] = True,
        download_path: Path | None = None,
    ) -> None: ...
    @overload
    @classmethod
    def with_options(
        cls,
        browser: Literal["firefox"],
        options: FirefoxOptions,
        *,
        wired: Literal[False],
        download_path: Path | None = None,
    ) -> DriverManager[SeFirefox]: ...
    @overload
    @classmethod
    def with_options(
        cls,
        browser: Literal["firefox"],
        options: FirefoxOptions,
        *,
        wired: Literal[True],
        download_path: Path | None = None,
    ) -> DriverManager[WiredFirefox]: ...
    @overload
    @classmethod
    def with_options(
        cls,
        browser: Literal["chrome"],
        options: ChromeOptions,
        *,
        wired: Literal[False],
        download_path: Path | None = None,
    ) -> DriverManager[SeChrome]: ...
    @overload
    @classmethod
    def with_options(
        cls,
        browser: Literal["chrome"],
        options: ChromeOptions,
        *,
        wired: Literal[True],
        download_path: Path | None = None,
    ) -> DriverManager[WiredChrome]: ...
    @property
    def driver(self) -> D: ...
    def exit(self) -> None: ...
