from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestIngredientNavigation:
    """Тест переходов по ингридиентам"""

    def test_ingredient_navigation(self, driver, ml):

        # Ждём когда появится заголовок "Соберите бургер"
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                ml.constructor_header)
        )

        # Ищем раздел "Соусы" и кликаем на него
        driver.find_element(*ml.sauces_partition).click()

        # Ждём когда раздел "Соусы" станет активным
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                ml.active_sauces_partition)
        )

        # Ищем раздел "Начинки" и кликаем на него
        driver.find_element(*ml.toppings_partition).click()

        # Ждём когда раздел "Начинки" станет активным
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                ml.active_toppings_partition)
        )

        # Ищем раздел "Булки" и кликаем на него
        driver.find_element(*ml.burger_bun_partition).click()

        # Ждём когда раздел "Булки" станет активным
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                ml.active_burger_bun_partition)
        )
