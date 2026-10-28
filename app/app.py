import re

from flask import Flask, render_template, request

app = Flask(__name__)

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[a-zA-Z]{2,}$")
PHONE_RE = re.compile(r"^\+?[\d\s()-]{10,18}$")


def validate(form):
    errors = {}

    if not form["name"]:
        errors["name"] = "Введите имя"

    if not form["email"]:
        errors["email"] = "Введите email"
    elif not EMAIL_RE.match(form["email"]):
        errors["email"] = "Некорректный email"

    # телефон необязательный, но если введён — проверяем формат
    if form["phone"] and not PHONE_RE.match(form["phone"]):
        errors["phone"] = "Некорректный номер телефона"

    if not form["message"]:
        errors["message"] = "Введите сообщение"

    return errors


@app.route("/")
@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = {"name": "", "email": "", "phone": "", "topic": "Вопрос", "message": ""}
    errors = {}
    success = None

    if request.method == "POST":
        for field in form:
            form[field] = request.form.get(field, "").strip()

        errors = validate(form)
        if not errors:
            success = f"Спасибо, {form['name']}! Ваше сообщение отправлено."
            form = {"name": "", "email": "", "phone": "", "topic": "Вопрос", "message": ""}

    return render_template("contact.html", form=form, errors=errors, success=success)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
