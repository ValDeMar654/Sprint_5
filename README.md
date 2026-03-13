# Sprint_5

# Задача

### [x] Регистрация
    Проверь:
    - [x] Успешную регистрацию. Поле «Имя» должно быть не пустым; в поле Email введён email в формате логин@домен:  например, 123@ya.ru. Минимальный пароль — шесть символов.
    - [x] Ошибку для некорректного пароля

### [x] Вход
    Проверь:
    - [x] вход по кнопке «Войти в аккаунт» на главной
    - [x] вход через кнопку «Личный кабинет»
    - [x] вход через кнопку в форме регистрации
    - [x] вход через кнопку в форме восстановления пароля

### [x] Переход в личный кабинет 
    - [x] Проверь переход по клику на «Личный кабинет»

### [x] Переход из личного кабинета в конструктор 
    - [x] Проверь переход по клику на «Конструктор» 
    - [x] и на логотип Stellar Burgers

### [x] Выход из аккаунта
    - [x] Проверь выход по кнопке «Выйти» в личном кабинете

### [x] Раздел «Конструктор»
    Проверь, что работают переходы к разделам:
    - [x] «Булки»
    - [x] «Соусы»
    - [x] «Начинки»

# Реализация
## Оглавление
- [conftest](#conftest)
- [locators](#locators)
- [login_logout](#login_logout)
- [registration](#registration)
- [test_ingredient_navigation](#test_ingredient_navigation)
- [test_login_via_buttons](#test_login_via_buttons)
- [test_registration_form](#test_registration_form)
- [test_switching_to_constructor](#test_switching_to_constructor)

## conftest
Файл содержит стартовую фикстуру и класс локаторов

## locators
В файле собраны различные локаторы

## login_logout
Файл содержит две функции.
Первая:
```
def test_login(self, driver, ml)
```
заполняет форму входа и осуществляет вход в Личный кабинет.
Вторая:
```
def test_logout(self, driver, ml)
```
осуществляет выход из Личного кабинета.

## registration
Файл содержит функцию:
```
def test_registration_form(self, driver, ml)
```
которая заполняет форму регистрации.

## test_ingredient_navigation
Файл содержит функцию:
```
def test_ingredient_navigation(self, driver, ml)
```
которая проверяет работу переходов между разделами Конструктора.

## test_login_via_buttons
Файл содержит 4 функции:
```
def test_login_via_personal_account_button(self, driver, ml)
def test_login_via_login_to_account_button(self, driver, ml)
def test_login_via_login_link_in_reg_form(self, driver, ml)
def test_login_via_login_link_in_passw_recov_form(self, driver, ml)
```
которые проверяют возможность входа в Личный кабинет из различных мест.
Каждый тест заканчивается выходом из Личного кабинета.

## test_registration_form
Файл содержит 2 функции:
```
def test_successful_registration(self, driver, ml)
def test_fail_registration_with_invalid_password(self, driver, ml)
```
которые проверяют успешную регистрацию и ошибку для некорректного пароля.

## test_switching_to_constructor
Файл содержит 2 функции:
```
def test_switch_to_constructor_via_constructor_button(self, driver, ml)
def test_switch_to_constructor_via_stellar_burger_logo(self, driver, ml)
```
которые проверяют переход из личного кабинета в конструктор 
по клику на "Конструктор" или логотип "Stellar Burgers".

