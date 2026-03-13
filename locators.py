from selenium.webdriver.common.by import By


class MyLocators:

    # Заголовок "Регистрация"
    register_header = (By.XPATH, '//h2[text()="Регистрация"]')

    # Заголовок "Вход"
    login_header = (By.XPATH, './/h2[text() = "Вход"]')

    # Заголовок "Соберите бургер"
    constructor_header = (By.XPATH, './/h1[text() = "Соберите бургер"]')

    # Заголовок "Профиль" в Личном кабинете
    profile = (By.LINK_TEXT, 'Профиль')

    # Кнопка Войти
    login_button = (
        By.XPATH,
        '//button[@class = "button_button__33qZ0 '
        'button_button_type_primary__1O7Bx '
        'button_button_size_medium__3zxIa" and text() = "Войти"]',
    )

    # Кнопка Войти в аккаунт
    login_to_account_button = (
        By.XPATH,
        '//button[@class = "button_button__33qZ0 '
        'button_button_type_primary__1O7Bx '
        'button_button_size_large__G21Vg" '
        'and text() = "Войти в аккаунт"]',
    )

    # Кнопка Выход
    logout_button = (
        By.XPATH,
        '//button[@class = "Account_button__14Yp3 '
        'text text_type_main-medium text_color_inactive" '
        'and text() = "Выход" ]',
    )

    # Кнопка Личный кабинет
    personal_account = (
        By.XPATH,
        "//p[@class = 'AppHeader_header__linkText__3q_va ml-2' "
        "and text() = 'Личный Кабинет']",
    )

    # Кнопка Зарегистрироваться
    register_button = (
        By.XPATH,
        '//button[@class =  "button_button__33qZ0 '
        'button_button_type_primary__1O7Bx button_button_size_medium__3zxIa" '
        'and text()="Зарегистрироваться"]'
    )

    # Кнопка Сохранить (в Профиле пользователя)
    save_button = (
        By.XPATH,
        '//button[@class="button_button__33qZ0 '
        'button_button_type_primary__1O7Bx '
        'button_button_size_medium__3zxIa" '
        'and text() = "Сохранить"]',
    )

    # Кнопка "Конструктор"
    constructor_button = (
        By.XPATH,
        "//p[@class = 'AppHeader_header__linkText__3q_va ml-2' "
        "and text() = 'Конструктор']",
    )

    # Поле Email
    email_field = (
        By.XPATH,
        "//label[text()= 'Email']/following-sibling::input",
    )

    # Поле Пароль
    password_field = (
        By.XPATH,
        "//label[text()= 'Пароль']/following-sibling::input",
    )

    # Поле Пароль с ошибкой ввода
    password_field_error = (
        By.CSS_SELECTOR, '.input_status_error'
    )

    # Поле Имя
    name_field = (
        By.XPATH,
        "//label[text()= 'Имя']/following-sibling::input",
    )

    # Поле Логин
    login_field = (
        By.XPATH,
        "//label[text()= 'Логин']/following-sibling::input",
    )

    # Ссылка Зарегистрироваться
    register_link = (By.LINK_TEXT, 'Зарегистрироваться')

    # Ссылка Войти
    login_link = (By.LINK_TEXT, 'Войти')

    # Ссылка Восстановить пароль
    recovery_password_link = (By.LINK_TEXT, 'Восстановить пароль')

    # Сообщение "Некоректный пароль"
    invalid_password_error = (
        By.XPATH,
        '//p[@class="input__error text_type_main-default" '
        'and text() = "Некорректный пароль"]',
    )

    # Логотип "Stellar Burger"
    stellar_burger_logo = (
        By.XPATH,
        "//div[@class='AppHeader_header__logo__2D0X2']",
    )

    # Раздел "Булки"
    burger_bun_partition = (
        By.XPATH,
        "//span[@class='text text_type_main-default' and text() = 'Булки']",
    )

    # Раздел "Соусы"
    sauces_partition = (
        By.XPATH,
        "//span[@class='text text_type_main-default' and text() = 'Соусы']",
    )

    # Раздел "Начинки"
    toppings_partition = (
        By.XPATH,
        "//span[@class='text text_type_main-default' and text() = 'Начинки']",
    )

    # Активный раздел "Булки"
    active_burger_bun_partition = (
        By.XPATH,
        '//span[@class="text text_type_main-default" and text() = '
        '"Булки"]/ancestor::div[contains(@class, '
        '"tab_tab_type_current__2BEPc")]'
    )
    # Активный раздел "Соусы"
    active_sauces_partition = (
        By.XPATH,
        '//span[@class="text text_type_main-default" and text() = '
        '"Соусы"]/ancestor::div[contains(@class, '
        '"tab_tab_type_current__2BEPc")]'
    )
    # Активный раздел "Начинки"
    active_toppings_partition = (
        By.XPATH,
        '//span[@class="text text_type_main-default" and text() = '
        '"Начинки"]/ancestor::div[contains(@class, '
        '"tab_tab_type_current__2BEPc")]'
    )
