# локаторы переходов
from selenium.webdriver.common.by import By


class TrafficLocators:
# логотипы
    LOGO_YANDEX = (By.XPATH, "//*[contains(@class, 'Header_LogoYandex')]/img[@alt='Yandex']")
    LOGO_SCOOTER = (By.XPATH, "//*[contains(@class, 'Header_LogoScooter')]/img[@alt='Scooter']")

# кнопка Заказа сверху
    BUTTON_UP = (By.XPATH, "//*[contains(@class, 'Button_Button') and text()='Заказать']")

#локатор логотипа главной страницы
    MAIN_TITLE = (By.XPATH, "//*[contains(@class, 'Home_Header') and text()='Самокат ']")
# <div class="Home_Header__iJKdX" style="transform: translateY(0px);">Самокат <br>на&nbsp;пару дней
#локатор Дзена
    MAIN_DZEN = (By.XPATH, "//*[contains(@class, 'dzen-layout--navigation-tab') and text()='Главная']")

