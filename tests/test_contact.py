import pytest

from pages.contact_page import ContactPage

VALID = {
    "name": "Иван Петров",
    "email": "ivan.petrov@mail.ru",
    "phone": "+7 999 123-45-67",
    "topic": "Предложение",
    "message": "Хотел бы узнать о сроках доставки заказа.",
}


def test_send_form_with_valid_data(driver):
    page = ContactPage(driver).open_page()

    page.fill_form(**VALID)
    page.submit()

    assert page.get_success_message() == "Спасибо, Иван Петров! Ваше сообщение отправлено."
    for field in ["name", "email", "phone", "message"]:
        assert not page.has_error(field)


@pytest.mark.parametrize(
    "field, expected_error",
    [
        ("name", "Введите имя"),
        ("email", "Введите email"),
        ("message", "Введите сообщение"),
    ],
    ids=["name", "email", "message"],
)
def test_empty_required_field(driver, field, expected_error):
    page = ContactPage(driver).open_page()

    data = dict(VALID)
    data[field] = ""  # одно обязательное поле оставляем пустым
    page.fill_form(**data)
    page.submit()

    assert page.get_error(field) == expected_error
    assert not page.is_present(page.SUCCESS)
