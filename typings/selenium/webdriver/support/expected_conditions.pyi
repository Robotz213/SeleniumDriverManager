# Licensed to the Software Freedom Conservancy (SFC) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The SFC licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from collections.abc import Callable
from typing import Literal

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import ByType
from selenium.webdriver.remote.webdriver import WebDriver

from customs import WebElement

"""
 * Canned "Expected Conditions" which are generally
     useful within webdriver
 * tests.
"""

type WebDriverOrWebElement = WebDriver | WebElement

# TO BE CLICKABLE
type RetToBeCliclabe = Literal[False] | WebElement
type ToBeClickabe = Callable[[WebDriverOrWebElement], RetToBeCliclabe]
type MarkToBeClick = WebElement | tuple[str, str]

def title_is(title: str) -> Callable[[WebDriver], bool]: ...
def title_contains(title: str) -> Callable[[WebDriver], bool]: ...
def presence_of_element_located(
    locator: tuple[ByType, str],
) -> Callable[[WebDriverOrWebElement], WebElement]: ...
def url_contains(url: str) -> Callable[[WebDriver], bool]: ...
def url_matches(pattern: str) -> Callable[[WebDriver], bool]: ...
def url_to_be(url: str) -> Callable[[WebDriver], bool]: ...
def url_changes(url: str) -> Callable[[WebDriver], bool]: ...
def visibility_of_element_located(
    locator: tuple[ByType, str],
) -> Callable[[WebDriverOrWebElement], Literal[False] | WebElement]: ...
def visibility_of(
    element: WebElement,
) -> Callable[[object], Literal[False] | WebElement]: ...
def _element_if_visible(
    element: WebElement,
    visibility: bool = True,
) -> Literal[False] | WebElement: ...
def presence_of_all_elements_located(
    locator: tuple[ByType, str],
) -> Callable[[WebDriverOrWebElement], list[WebElement]]: ...
def visibility_of_any_elements_located(
    locator: tuple[ByType, str],
) -> Callable[[WebDriverOrWebElement], list[WebElement]]: ...
def visibility_of_all_elements_located(
    locator: tuple[ByType, str],
) -> Callable[
    [WebDriverOrWebElement],
    list[WebElement] | Literal[False],
]: ...
def text_to_be_present_in_element(
    locator: tuple[ByType, str],
    text_: str,
) -> Callable[[WebDriverOrWebElement], bool]: ...
def text_to_be_present_in_element_value(
    locator: tuple[ByType, str],
    text_: str,
) -> Callable[[WebDriverOrWebElement], bool]: ...
def text_to_be_present_in_element_attribute(
    locator: tuple[ByType, str],
    attribute_: str,
    text_: str,
) -> Callable[[WebDriverOrWebElement], bool]: ...
def frame_to_be_available_and_switch_to_it(
    locator: tuple[ByType, str] | str | WebElement,
) -> Callable[[WebDriver], bool]: ...
def invisibility_of_element_located(
    locator: WebElement | tuple[str, str],
) -> Callable[[WebDriverOrWebElement], WebElement | bool]: ...
def invisibility_of_element(
    element: WebElement | tuple[str, str],
) -> Callable[[WebDriverOrWebElement], WebElement | bool]: ...
def element_to_be_clickable(mark: MarkToBeClick) -> ToBeClickabe: ...
def staleness_of(element: WebElement) -> Callable[[object], bool]: ...
def element_to_be_selected(
    element: WebElement,
) -> Callable[[object], bool]: ...
def element_located_to_be_selected(
    locator: tuple[ByType, str],
) -> Callable[[WebDriverOrWebElement], bool]: ...
def element_selection_state_to_be(
    element: WebElement,
    is_selected: bool,
) -> Callable[[object], bool]: ...
def element_located_selection_state_to_be(
    locator: tuple[ByType, str],
    is_selected: bool,
) -> Callable[[WebDriverOrWebElement], bool]: ...
def number_of_windows_to_be(
    num_windows: int,
) -> Callable[[WebDriver], bool]: ...
def new_window_is_opened(
    current_handles: set[str],
) -> Callable[[WebDriver], bool]: ...
def alert_is_present() -> Callable[[WebDriver], Alert | bool]: ...
def element_attribute_to_include(
    locator: tuple[ByType, str],
    attribute_: str,
) -> Callable[[WebDriverOrWebElement], bool]: ...
def any_of[D, T](
    *expected_conditions: Callable[[D], T],
) -> Callable[[D], Literal[False] | T]: ...
def all_of[D, T](
    *expected_conditions: Callable[[D], T | Literal[False]],
) -> Callable[[D], list[T] | Literal[False]]: ...
def none_of[D, T](
    *expected_conditions: Callable[[D], T],
) -> Callable[[D], bool]: ...
