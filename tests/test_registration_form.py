import random

from login_logout import TestLoginLogout as log_action
from registration import TestRegistrationForm as reg_action
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestRegistration:
    """Тест успешной и неуспешной регистрации"""

    name = "Колобок"
    login = f"V_G_41_{random.randint(100, 999)}@yandex.ru"
    password = '123456'

    # Тест регистрации с валидными данными
    def test_successful_registration(self, driver, ml):

        # Переходим в форму регистрации, заполняем поля и кликаем на кнопку
        # "Зарегистрироваться"
        reg_action.test_registration_form(self, driver, ml)

        # Ждем когда исчезнет форма регистрации с заголовком "Регистрация"
        WebDriverWait(driver, 3).until(
            expected_conditions.invisibility_of_element_located(
                ml.register_header
            )
        )

        # Проверяем что регистрация прошла успешно, логинимся с данными при
        # регистрации и выходим
        log_action.test_login(self, driver, ml)
        log_action.test_logout(self, driver, ml)

    # Тест регистрации с невалидным паролем
    def test_fail_registration_with_invalid_password(self, driver, ml):

        self.password = '123'

        # Переходим в форму регистрации, заполняем поля и кликаем на кнопку
        # "Зарегистрироваться"
        reg_action.test_registration_form(self, driver, ml)

        # Ждем когда граница поля Пароль станет красного цвета
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                ml.password_field_error)
        )

        # Проверяем появление текста "Некорректный пароль"
        assert driver.find_element(*ml.invalid_password_error)
