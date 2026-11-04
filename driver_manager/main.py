from __future__ import annotations

from pathlib import Path
from typing import ClassVar, Literal, Self, TypedDict, cast

from selenium.webdriver import Chrome as BaseSeChrome
from selenium.webdriver import ChromeOptions, FirefoxOptions
from selenium.webdriver import Firefox as BaseSeFirefox
from seleniumwire.webdriver import Chrome as BaseWiredChrome
from seleniumwire.webdriver import Firefox as BaseWiredFirefox

from .constants import (
    CHROME_ARGUMENTS,
    CHROME_PREFERENCES,
    SEWIRE_ARGUMENTS,
)
from .element import WebElement


class BaseOptions(FirefoxOptions, ChromeOptions): ...


class WiredChrome(BaseWiredChrome):
    _web_element_cls: WebElement

    def set_web_element_cls(self, cls: type[WebElement]) -> None:
        self._web_element_cls = cls  # pyright: ignore[reportAttributeAccessIssue]


class WiredFirefox(BaseWiredFirefox):
    _web_element_cls: WebElement

    def set_web_element_cls(self, cls: type[WebElement]) -> None:
        self._web_element_cls = cls  # pyright: ignore[reportAttributeAccessIssue]


class SeChrome(BaseSeChrome):
    _web_element_cls: WebElement

    def set_web_element_cls(self, cls: type[WebElement]) -> None:
        self._web_element_cls = cls  # pyright: ignore[reportAttributeAccessIssue]


class SeFirefox(BaseSeFirefox):
    _web_element_cls: WebElement

    def set_web_element_cls(self, cls: type[WebElement]) -> None:
        self._web_element_cls = cls  # pyright: ignore[reportAttributeAccessIssue]


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
        options: ChromeOptions | FirefoxOptions,
        *,
        wired: bool = False,
        download_path: Path | None = None,
    ) -> None:

        try:
            if not download_path:
                download_path = Path.cwd().joinpath("downloads")
                print(f"dowload path: {download_path!s}")

            self.download_dir = download_path
            cls_ = self.SE_DRIVER[browser]
            if wired:
                cls_ = self.WIRED_DRIVER[browser]
                options = self.__wired_args(cast("BaseOptions", options))

            match browser:
                case "chrome":
                    options = self.__chrome_prefs(cast("ChromeOptions", options))
                    options = self.__chrome_args(cast("ChromeOptions", options))

                case "firefox":
                    print("ok")

            self.driver = cls_(options=options)  # pyright: ignore[reportArgumentType]
            self.driver.set_web_element_cls(WebElement)

        except KeyError as e:
            raise StartManagerError from e

    @classmethod
    def with_options(
        cls,
        browser: Literal["firefox", "chrome"],
        options: BaseOptions,
        *,
        wired: bool = False,
        download_path: Path | None = None,
    ) -> Self:

        return cls(browser, options, wired=wired, download_path=download_path)

    def __chrome_prefs(self, options: ChromeOptions) -> ChromeOptions:
        _ = self

        ch_prefs = CHROME_PREFERENCES.copy()
        k = "download.default_directory"
        ch_prefs[k] = str(self.download_dir)
        prefs = cast("dict", ch_prefs)
        options.add_experimental_option("prefs", value=prefs)
        return options

    def __chrome_args(self, options: ChromeOptions) -> ChromeOptions:

        _ = self
        for arg in CHROME_ARGUMENTS:
            options.add_argument(arg)

        return options

    def __wired_args[OPT: ChromeOptions | BaseOptions](self, options: OPT) -> OPT:
        _ = self
        for wire_arguments in SEWIRE_ARGUMENTS:
            options.add_argument(wire_arguments)  # pyright: ignore[reportAttributeAccessIssue]

        return options
