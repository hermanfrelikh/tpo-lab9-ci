import os
import threading

import pytest
from selenium import webdriver
from werkzeug.serving import make_server

from app.app import app


@pytest.fixture(scope="session")
def server():
    # поднимаем форму из ЛР4 в отдельном потоке на время всех UI-тестов,
    # чтобы не запускать её руками ни локально, ни в GitHub Actions
    srv = make_server("127.0.0.1", 8000, app)
    thread = threading.Thread(target=srv.serve_forever, daemon=True)
    thread.start()
    yield
    srv.shutdown()


@pytest.fixture
def driver(server):
    options = webdriver.ChromeOptions()
    # в GitHub Actions нет экрана, поэтому Chrome без окна;
    # переменную CI=true GitHub выставляет сам
    if os.getenv("CI") or os.getenv("HEADLESS"):
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1280,900")
    driver = webdriver.Chrome(options=options)  # драйвер подберёт Selenium Manager

    yield driver

    driver.quit()
