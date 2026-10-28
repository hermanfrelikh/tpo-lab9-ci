# Лабораторная работа №9. Интеграция автотестов в CI/CD (GitHub Actions)

Автотесты из прошлых лабораторных запускаются автоматически при каждом push в репозиторий GitHub.

Репозиторий: https://github.com/hermanfrelikh/tpo-lab9-ci
Запуски: https://github.com/hermanfrelikh/tpo-lab9-ci/actions

## Что внутри

```
9lab/
├── .github/workflows/run-tests.yml   # workflow GitHub Actions
├── calculator.py                     # ЛР6: класс Calculator
├── app/                              # ЛР4: форма обратной связи на Flask
├── pages/                            # ЛР4: Page Object (BasePage, ContactPage)
├── tests/
│   ├── conftest.py                   # фикстуры: сервер формы в потоке + Chrome (headless в CI)
│   ├── test_calculator.py            # ЛР6: 50 модульных тестов
│   └── test_contact.py               # ЛР4: 4 UI-теста на Selenium
├── pytest.ini
└── requirements.txt                  # flask, selenium, pytest
```

Всего 54 теста. Форму запускать руками не нужно: фикстура `server` сама поднимает её на `127.0.0.1:8000` на время UI-тестов. Chrome в GitHub Actions запускается без окна (headless): GitHub выставляет переменную `CI=true`, и `conftest.py` это видит.

## Workflow

`.github/workflows/run-tests.yml` запускается при каждом `push`, `pull_request` и вручную (кнопка **Run workflow**):

1. `runs-on: ubuntu-latest` — виртуальная машина с Ubuntu (Chrome там уже установлен);
2. `actions/checkout` — скачать код репозитория;
3. `actions/setup-python` — поставить Python (матрица: 3.11 и 3.12, два параллельных задания);
4. `pip install -r requirements.txt` — зависимости;
5. `pytest -v --junitxml=report.xml` — тесты;
6. `actions/upload-artifact` — сохранить `report.xml` (даже если тесты упали).

Если хоть один тест упал, pytest вернёт ненулевой код, шаг станет красным, и у коммита будет красный крестик вместо зелёной галочки.

## Запуск тестов локально (macOS)

```bash
cd ~/Desktop/ТПО/9lab
python3 -m venv venv              # один раз
source venv/bin/activate
pip install -r requirements.txt   # один раз
pytest -v                         # с окнами Chrome
CI=true pytest -v                 # как в GitHub Actions, без окон
```

Ожидаемо: `54 passed`.

## Как запустить workflow

Любой push:

```bash
cd ~/Desktop/ТПО/9lab
git add .
git commit -m "Изменение"
git push
```

Через несколько секунд на вкладке **Actions** репозитория появится новый запуск. Ещё вариант: Actions → Run tests → **Run workflow**.

Проверить, что CI ловит ошибки: в `calculator.py` в `add` заменить `a + b` на `a - b`, сделать commit и push — запуск станет красным. Вернуть обратно и запушить — снова зелёный.
