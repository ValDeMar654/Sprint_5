from login_logout import TestLoginLogout as log_action
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLoginViaButtons:
    """Тесты входа в Личный кабинет через разные кнопки"""

    login = "v_g_41_654@yandex.ru"
    password = '65tgb$RFV'

    # Вход через кнопку Личный кабинет
    def test_login_via_personal_account_button(self, driver, ml):

        # Ждём кода кнопка «Личный кабинет» станет кликабельна и кликаем
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(ml.personal_account)
        )
        driver.find_element(*ml.personal_account).click()

        # Логинимся и выходим
        log_action.test_login(self, driver, ml)
        log_action.test_logout(self, driver, ml)

    def test_login_via_login_to_account_button(self, driver, ml):

        # Ждём кода кнопка «Войти в аккаунт» станет кликабельна и кликаем
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(
                ml.login_to_account_button)
        )
        driver.find_element(*ml.login_to_account_button).click()

        # Логинимся и выходим
        log_action.test_login(self, driver, ml)
        log_action.test_logout(self, driver, ml)

    def test_login_via_login_link_in_reg_form(self, driver, ml):

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

        # Ждем пока загрузится форма регистрации и станет кликабельна ссылка
        # "Войти" и кликаем на нее
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(ml.login_link)
        )
        driver.find_element(*ml.login_link).click()

        # Логинимся и выходим
        log_action.test_login(self, driver, ml)
        log_action.test_logout(self, driver, ml)

    def test_login_via_login_link_in_passw_recov_form(self, driver, ml):

        # Ждём кода кнопка «Личный кабинет» станет кликабельна и кликаем
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(ml.personal_account)
        )
        driver.find_element(*ml.personal_account).click()

        # Ждем пока загрузится форма входа и станет кликабельна ссылка
        # "Восстановить пароль" и кликаем на нее
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(
                ml.recovery_password_link)
        )
        driver.find_element(*ml.recovery_password_link).click()

        # Ждем пока загрузится форма восстановления пароля и станет
        # кликабельна ссылка "Войти" и кликаем на нее
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(ml.login_link)
        )
        driver.find_element(*ml.login_link).click()

        # Логинимся и выходим
        log_action.test_login(self, driver, ml)
        log_action.test_logout(self, driver, ml)
