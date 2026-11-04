from typing import TypedDict

from selenium.webdriver import Chrome as _Chrome
from selenium.webdriver.support.relative_locator import RelativeBy
from seleniumwire.inspect import InspectRequestsMixin

from driver_manager.element import WebElement

class Cookie(TypedDict):
    domain: str
    expiry: int
    httpOnly: bool
    name: str
    path: str
    sameSite: str
    secure: int
    value: str

class DriverCommonMixin:
    def _setup_backend(
        self,
        seleniumwire_options: dict[str, object],
    ) -> dict[str, object]: ...
    @property
    def proxy(self) -> dict[str, object]: ...
    @proxy.setter
    def proxy(self, proxy_conf: dict[str, object]) -> None: ...

class Chrome(InspectRequestsMixin, DriverCommonMixin, _Chrome):
    def __init__(
        self,
        *args: object,
        seleniumwire_options: dict[str, object] | None = None,
        **kwargs: object,
    ) -> None: ...
    @property
    def is_closed(self) -> bool: ...
    def get_cookies(self) -> list[Cookie]: ...
    def find_element(
        self,
        by: str | RelativeBy = ...,
        value: str | None = None,
    ) -> WebElement: ...
    def find_elements(
        self,
        by: str | RelativeBy = ...,
        value: str | None = None,
    ) -> list[WebElement]: ...

class Firefox(InspectRequestsMixin, DriverCommonMixin, _Chrome):
    def __init__(
        self,
        *args: object,
        seleniumwire_options: dict[str, object] | None = None,
        **kwargs: object,
    ) -> None: ...
    @property
    def is_closed(self) -> bool: ...
    def get_cookies(self) -> list[Cookie]: ...
    def find_element(
        self,
        by: str | RelativeBy = ...,
        value: str | None = None,
    ) -> WebElement: ...
    def find_elements(
        self,
        by: str | RelativeBy = ...,
        value: str | None = None,
    ) -> list[WebElement]: ...
