from login_logout import TestLoginLogout as log_action
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestSwitchToConstructor:
    """Тесты перехода в Конструктор из Личного кабинета"""

    login = "v_g_41_654@yandex.ru"
    password = '65tgb$RFV'

    # Тест перехода в Конструктор из Личного кабинета по клику на "Конструктор"
    def test_switch_to_constructor_via_constructor_button(self, driver, ml):

        # Ждём кода кнопка «Личный кабинет» станет кликабельна и кликаем
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(ml.personal_account)
        )
        driver.find_element(*ml.personal_account).click()

        # Логинимся
        log_action.test_login(self, driver, ml)

        # Ждём кода кнопка «Личный кабинет» станет кликабельна и кликаем
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(ml.personal_account)
        )
        driver.find_element(*ml.personal_account).click()

        # Ждём кода появится кнопка "Конструктор" и кликаем
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                ml.constructor_button)
        )
        driver.find_element(*ml.constructor_button).click()

        # Проверяем появление заголовка "Соберите бургер"
        assert driver.find_element(*ml.constructor_header)

        # Выходим из Личного кабинета
        log_action.test_logout(self, driver, ml)

    # Тест перехода в Конструктор из Личного кабинета по клику
    # на логотип "Stellar Burgers"
    def test_switch_to_constructor_via_stellar_burger_logo(self, driver, ml):
        # Ждём кода кнопка «Личный кабинет» станет кликабельна и кликаем
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(ml.personal_account)
        )
        driver.find_element(*ml.personal_account).click()

        # Логинимся
        log_action.test_login(self, driver, ml)

        # Ждём кода кнопка «Личный кабинет» станет кликабельна и кликаем
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(ml.personal_account)
        )
        driver.find_element(*ml.personal_account).click()

        # Ждём кода появится логотип "Stellar Burger" и кликаем
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                ml.stellar_burger_logo)
        )
        driver.find_element(*ml.stellar_burger_logo).click()

        # Проверяем появление заголовка "Соберите бургер"
        assert driver.find_element(*ml.constructor_header)

        # Выходим из Личного кабинета
        log_action.test_logout(self, driver, ml)
