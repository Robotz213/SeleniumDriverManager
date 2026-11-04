"""Forneca recursos do modulo constants."""

from __future__ import annotations

from collections.abc import Iterable
from typing import TYPE_CHECKING

from selenium.common.exceptions import (
    NoSuchElementException,
    StaleElementReferenceException,
)

if TYPE_CHECKING:
    from _manager_types import SeWireArguments

POLL_FREQUENCY: float = 0.1
IGNORED_EXCEPTIONS: Iterable[type[Exception]] = (
    NoSuchElementException,
    StaleElementReferenceException,
)
SEWIRE_ARGUMENTS: SeWireArguments = [
    "--allow-insecure-localhost",
    "--ignore-ssl-errors",
    "--ignore-certificate-errors",
]
