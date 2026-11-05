import tempfile
from pathlib import Path
from threading import Event
from uuid import uuid4

from selenium.webdriver import FirefoxOptions

from driver_manager import DriverManager


class Test:
    id_execucao = str(uuid4().hex)


with tempfile.TemporaryDirectory() as tmpdir:
    user_data_dir = Path(tmpdir)
    t = Test()

    options = FirefoxOptions()
    options.add_argument("--no-sandbox")

    try:
        a = DriverManager("firefox", options).driver
    except Exception as e:
        print(e)
    Event().wait()
