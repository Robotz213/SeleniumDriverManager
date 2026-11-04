from __future__ import annotations

from typing import ClassVar, Literal, Self, TypedDict

from selenium.webdriver import Chrome as SeChrome
from selenium.webdriver import Firefox as SeFirefox
from selenium.webdriver.common.options import BaseOptions
from seleniumwire.webdriver import Chrome as WiredChrome
from seleniumwire.webdriver import Firefox as WiredFirefox


class StartManagerError(Exception):
    def __init__(self, *args: object) -> None:
        self.message = 'Necessário selecionar "chrome" ou "firefox"'
        Exception.__init__(self, self.message)


class Drivers(TypedDict):
    chrome: type[SeChrome]
    firefox: type[SeFirefox]


class WiredDrivers(TypedDict):
    chrome: type[WiredChrome]
    firefox: type[WiredFirefox]


class DriverManager:
    SE_DRIVER: ClassVar[Drivers] = {"chrome": SeChrome, "firefox": SeFirefox}
    WIRED_DRIVER: ClassVar[WiredDrivers] = {
        "chrome": WiredChrome,
        "firefox": WiredFirefox,
    }

    def __init__(
        self,
        browser: Literal["firefox", "chrome"],
        options: BaseOptions,
        *,
        wired: bool = False,
    ) -> None:

        try:
            cls_ = self.SE_DRIVER[browser]
            if wired:
                cls_ = self.WIRED_DRIVER[browser]

            self.driver = cls_(options=options)  # pyright: ignore[reportArgumentType]

        except KeyError as e:
            raise StartManagerError from e

    @classmethod
    def with_options(
        cls,
        browser: Literal["firefox", "chrome"],
        options: BaseOptions,
        *,
        wired: bool = False,
    ) -> Self:

        return cls(browser, options, wired=wired)
