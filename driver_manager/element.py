"""Extensões de WebElement usadas pelos bots do CrawJUD."""

# pyright: reportUnknownMemberType=false, reportUnnecessaryIsInstance=false
# pyright: reportUnknownArgumentType=false, reportIncompatibleMethodOverride=false
# pyright: reportUnknownVariableType=false
import platform
from contextlib import suppress
from pathlib import Path
from time import sleep
from typing import TYPE_CHECKING, NoReturn, Self, cast
from unicodedata import combining, normalize

from selenium.common import (
    ElementNotInteractableException,
    StaleElementReferenceException,
)
from selenium.common.exceptions import (
    ElementClickInterceptedException,
)
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import (
    ScrollOrigin,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.utils import keys_to_typing
from selenium.webdriver.remote.command import Command
from selenium.webdriver.support.ui import Select

from ._base import SEWebElement
from .constants import (
    COMMAND_SELECT2,
    GET_INNER_TEXT,
)

if TYPE_CHECKING:
    from collections.abc import Sequence

    from selenium.webdriver.remote.webdriver import WebDriver as Driver
    from selenium.webdriver.support.relative_locator import (
        RelativeBy,
    )

JsScripts = Path(__file__).parent.joinpath("js")

COMMAND = 'return arguments[0].hasAttribute("{attr}")'
"""Comando de automação usado pelo fluxo de element."""


def raise_execution_error(message: str) -> NoReturn:

    raise Exception(message)  # noqa: TRY002


class ClickInterceptedError(Exception):
    """Representa falhas de clique interceptado."""

    def __init__(self, message: str) -> None:
        """Inicialize click intercepted error.

        Args:
            message (str): Mensagem processada pela operacao.

        """
        self.message = message
        self.msg = message
        Exception.__init__(self, message)

    def __repr__(self) -> str:
        """Retorna a representação textual da exceção.

        Returns:
            str: Texto formatado da exceção.

        """
        return f"{self.__class__.__name__}(message={self.message})"


class PropertiesWebElement(SEWebElement):
    """Expõe propriedades convenientes sobre `WebElement`."""

    @property
    def text(self) -> str:
        """Retorne o texto visível ou o valor do elemento."""
        text_ = str(self._execute("getElementText")["value"])

        if not text_:
            with suppress(Exception):
                cmd_ = "return arguments[0].value"

                text_ = str(self.parent.execute_script(cmd_, self))
                if text_ == "None":
                    text_ = ""

        return text_

    @property
    def TYPE(self) -> str:
        """Retorne o tipo declarado no elemento."""
        return str(self.get_attribute("type") or "")

    @property
    def parent(self) -> Driver:
        """Obtenha parent.

        Returns:
            Driver: Resultado de obtenha parent.

        """
        return self._parent

    @parent.setter
    def parent(self, val: Driver) -> None:
        """Atualize parent.

        Args:
            val (Driver): Valor de val.

        """
        self._parent = val

    @property
    def actions(self) -> ActionChains:
        """Obtenha actions.

        Returns:
            ActionChains: Resultado de obtenha actions.

        """
        return self._actions

    @actions.setter
    def actions(self, val: ActionChains) -> None:
        """Atualize actions.

        Args:
            val (ActionChains): Valor de val.

        """
        self._actions = val

    @property
    def current_driver(self) -> Driver:
        """Obtenha current driver.

        Returns:
            Driver: Resultado de obtenha current driver.

        """
        return self._current_driver

    @current_driver.setter
    def current_driver(self, val: Driver) -> None:
        """Atualize current driver.

        Args:
            val (Driver): Valor de val.

        """
        self._current_driver = val

    @property
    def innerHTML(self) -> str:
        """Retorna o HTML interno do elemento."""
        cmd_ = "return arguments[0].innerHTML"

        return str(self.parent.execute_script(cmd_, self))


class WebElement(PropertiesWebElement):
    """Adiciona operações de alto nível ao `WebElement` do Selenium."""

    def __init__(self, parent: Driver, id_: str) -> None:
        """Inicialize web element.

        Args:
            parent (Driver): Valor de parent.
            id_ (str): Texto de id.

        """
        self._parent = parent
        self._id = id_

        self.actions = ActionChains(parent)
        self.current_driver = parent

        self.id_property = ""
        with suppress(Exception):
            self.id_property = str(self.get_property("id"))

    def execute_script(
        self,
        script: str,
        *args: object,
    ) -> object:
        """Execute execute script.

        Args:
            script (str): Texto de script.
            *args (object): Valores posicionais adicionais.

        Returns:
            object: Resultado de execute execute script.

        """
        return self.parent.execute_script(script, self, *args)

    def double_click(self) -> None:
        """Executa um clique duplo no elemento."""
        self.actions.double_click(self).perform()

    def selecionar_item(self, item: str) -> None:
        """Execute selecionar item.

        Args:
            item (str): Texto de item.

        """
        normalizado1 = "".join(
            [c for c in normalize("NFKD", item) if not combining(c)]
        ).upper()

        items = self.find_elements(By.TAG_NAME, "option")
        opt_itens: dict[str, str] = {}

        for it in items:
            exec_ = self.parent.execute_script(GET_INNER_TEXT, it)
            key = str(exec_)
            value = it.get_attribute("value")
            if value:
                normalizado2 = "".join(
                    [c for c in normalize("NFKD", key) if not combining(c)]
                ).upper()
                opt_itens.update({normalizado2: value})

        opt = opt_itens.get(normalizado1)
        if not opt:
            raise_execution_error(
                message=f'Opção "{item}" não encontrada!',
            )

        return Select(self).select_by_value(opt)

    def select_item(self, item: str) -> None:
        """Execute select item.

        Args:
            item (str): Texto de item.

        """
        return Select(self).select_by_value(item)

    def click(self) -> None:
        """Clicks the element.

        Example:
            element = driver.find_element(By.ID, "foo")
            element.click()

        """
        try:
            super().click()

        except (
            ElementClickInterceptedException,
            ElementNotInteractableException,
            StaleElementReferenceException,
        ):
            cmd = "arguments[0].click()"
            self.parent.execute_script(cmd, self)

    def clear(self) -> None:
        """Limpa o campo após um clique para ganhar foco."""
        self.click()
        sleep(0.5)

        with suppress(Exception):
            super().clear()

    def scroll_to(self) -> None:
        """Rola a página até o elemento atual."""
        self.actions.scroll_to_element(self)
        sleep(0.5)

    def find_element(
        self,
        by: str | RelativeBy = By.ID,
        value: str | None = None,
    ) -> WebElement:
        """Obtenha find element.

        Args:
            by (str | RelativeBy): Texto de by.
            value (str | None): Valor processado pela operacao.

        Returns:
            WebElement: Resultado de obtenha find element.

        """
        return cast(
            "WebElement",
            super().find_element(by=by, value=value),
        )

    def find_elements(
        self,
        by: str | RelativeBy = By.ID,
        value: str | None = None,
    ) -> Sequence[WebElement]:
        """Obtenha find elements.

        Args:
            by (str | RelativeBy): Texto de by.
            value (str | None): Valor processado pela operacao.

        Returns:
            Sequence[WebElement]: Resultado de obtenha find elements.

        """
        return cast(
            "Sequence[WebElement]",
            super().find_elements(by=by, value=value),
        )

    def send_keys(self, *value: str) -> None:
        """Envie send keys.

        Args:
            *value (str): Valor processado pela operacao.

        """
        word = value
        if isinstance(value, (tuple, str)):
            word = value[0]

        send = False

        keys_ = list(Keys.__dict__.values())
        if_keys = word in keys_

        if if_keys:
            send = True
            super().send_keys(word)
            return

        if not send:
            for c in str(word):
                sleep(0.01)
                super().send_keys(c)

    def send_text(self, text: str) -> None:
        """Envie send text.

        Args:
            text (str): Texto de text.

        """
        super().send_keys(text)

    def send_file(self, file: str | Path) -> None:
        """Envie send file.

        Args:
            file (str | Path): Arquivo usado pela operacao.

        """
        file_ = file
        if isinstance(file, Path):
            file_ = file.as_posix() if platform.system() == "Linux" else str(file)
        self._execute(
            Command.SEND_KEYS_TO_ELEMENT,
            {
                "text": "".join(keys_to_typing(str(file_))),
                "value": keys_to_typing(str(file_)),
            },
        )

    def display_none(self) -> None:
        """Aguarda até que o elemento deixe de ficar visível."""
        while True:
            style = str(self.get_attribute("style"))
            if "display: none;" not in style:
                sleep(0.01)
                break

    def select2(self, opcao: str) -> None:
        """Execute select2.

        Args:
            opcao (str): Texto de opcao.

        """
        items = self.find_elements(By.TAG_NAME, "option")
        opt_itens: dict[str, str] = {}

        for item in items:
            value_item = item.get_attribute("value") or ""
            command = "return $(arguments[0]).text();"
            text_item = self.parent.execute_script(command, item)
            text_item = " ".join(
                [item for item in str(text_item).strip().split(" ") if item]
            ).upper()
            opt_itens.update({text_item: value_item})

        to_search = " ".join(opcao.split(" ")).upper()
        value_opt = opt_itens.get(to_search)

        if value_opt:
            self.parent.execute_script(
                COMMAND_SELECT2,
                self,
                value_opt,
            )
            return

        raise_execution_error(
            message=f'Opção "{to_search}" não encontrada!',
        )

    def scroll_from_origin(
        self,
        delta_x: int,
        delta_y: int,
        origin: Self | None = None,
    ) -> None:
        """Execute scroll from origin.

        Args:
            delta_x (int): Numero inteiro de delta x.
            delta_y (int): Numero inteiro de delta y.
            origin (Self | None): Valor de origin.

        """
        if not origin:
            origin = self

        location = origin.location
        scroll_origin = ScrollOrigin.from_element(
            origin,
            x_offset=int(location.get("x") or "0"),
            y_offset=int(location.get("y") or "0"),
        )

        self.actions.scroll_to_element(self)

        with suppress(Exception):
            return self.actions.scroll_from_origin(
                scroll_origin=scroll_origin,
                delta_x=0,
                delta_y=delta_y,
            ).perform()

    def scroll_to_element(self) -> None:
        """Rola a página até o elemento e executa a ação."""
        self.actions.scroll_to_element(self).perform()

    def blur(self) -> None:
        """Remove o foco do elemento."""
        command = "arguments[0].blur();"
        self.parent.execute_script(command, self)

    def has_attribute(self, attr: str) -> bool:
        """Verifique se um elemento possui um atributo.

        Returns:
            bool: Indica se o atributo existe no elemento.

        Example:
            element.has_attribute(attr="style") # retorna False ou True

        """
        check = False
        with suppress(Exception):
            cmd = COMMAND.format(attr=attr)
            exec_ = self.parent.execute_script(cmd, self)
            check = bool(exec_)

        return check
