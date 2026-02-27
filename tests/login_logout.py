from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# class estLoginLogout:
class TestLoginLogout:
    """Заполнение формы Входа, вход и выход из Личного кабинета"""

    login = "v_g_41_654@yandex.ru"
    password = '65tgb$RFV'

    # Заполнение формы Входа и вход в Личный кабинет
    def test_login(self, driver, ml):

        # Ждём кода появится форма с заголовком "Вход"
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(ml.login_header))

        # Ищем поле "Email" и заполняем его
        driver.find_element(*ml.email_field).send_keys(self.login)

        # Ищем поле "Пароль" и заполняем его
        driver.find_element(*ml.password_field).send_keys(self.password)

        # Ищем кнопку "Войти" и кликаем
        driver.find_element(*ml.login_button).click()

        # Ждем когда исчезнет форма входа с кнопкой Войти
        WebDriverWait(driver, 5).until(
            expected_conditions.invisibility_of_element_located(
                ml.login_button)
        )

    # Выход из Личного кабинета
    def test_logout(self, driver, ml):

        # Кликаем по кнопке «Личный кабинет»
        driver.find_element(*ml.personal_account).click()

        # Ждём кода кнопка «Выход» станет кликабельна и кликаем
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(ml.logout_button)
        )
        driver.find_element(*ml.logout_button).click()
