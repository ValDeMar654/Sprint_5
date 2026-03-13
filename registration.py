from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestRegistrationForm:
    """Заполнение формы регистрации"""

    def test_registration_form(self, driver, ml):

        # Ждём кода кнопка «Личный кабинет» станет кликабельна и кликаем
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(ml.personal_account)
        )
        driver.find_element(*ml.personal_account).click()

        # Ждем пока загрузится форма входа и станет кликабельна ссылка
        # "Зарегистрироваться" и кликаем на нее
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(ml.register_link)
        )
        driver.find_element(*ml.register_link).click()

        # Ждем пока загрузится форма регистрации и станет виден заголовок
        # "Регистрация"
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                ml.register_header)
        )

        # Ищем поле "Имя" и заполняем его
        driver.find_element(*ml.name_field).send_keys(self.name)

        # Ищем поле "Email" и заполняем его
        driver.find_element(*ml.email_field).send_keys(self.login)

        # Ищем поле "Пароль" и заполняем его
        driver.find_element(*ml.password_field).send_keys(self.password)

        # Ищем кнопку "Зарегистрироваться" и кликаем на нее
        driver.find_element(*ml.register_button).click()
