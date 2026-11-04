from typing import ClassVar, Literal, TypedDict, overload

from selenium.webdriver import Chrome as SeChrome
from selenium.webdriver import ChromeOptions, FirefoxOptions
from selenium.webdriver import Firefox as SeFirefox
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

    @overload
    def __init__(
        self: DriverManager[SeFirefox],
        browser: Literal["firefox"],
        options: FirefoxOptions,
        *,
        wired: Literal[False] = False,
    ) -> None: ...
    @overload
    def __init__(
        self: DriverManager[WiredFirefox],
        browser: Literal["firefox"],
        options: FirefoxOptions,
        *,
        wired: Literal[True] = True,
    ) -> None: ...
    @overload
    def __init__(
        self: DriverManager[SeChrome],
        browser: Literal["chrome"],
        options: ChromeOptions,
        *,
        wired: Literal[False] = False,
    ) -> None: ...
    @overload
    def __init__(
        self: DriverManager[WiredChrome],
        browser: Literal["chrome"],
        options: ChromeOptions,
        *,
        wired: Literal[True] = True,
    ) -> None: ...
    @overload
    @classmethod
    def with_options(
        cls,
        browser: Literal["firefox"],
        options: FirefoxOptions,
        *,
        wired: Literal[False],
    ) -> DriverManager[SeFirefox]: ...
    @overload
    @classmethod
    def with_options(
        cls,
        browser: Literal["firefox"],
        options: FirefoxOptions,
        *,
        wired: Literal[True],
    ) -> DriverManager[WiredFirefox]: ...
    @overload
    @classmethod
    def with_options(
        cls,
        browser: Literal["chrome"],
        options: ChromeOptions,
        *,
        wired: Literal[False],
    ) -> DriverManager[SeChrome]: ...
    @overload
    @classmethod
    def with_options(
        cls,
        browser: Literal["chrome"],
        options: ChromeOptions,
        *,
        wired: Literal[True],
    ) -> DriverManager[WiredChrome]: ...
    @property
    def driver(self) -> D: ...
