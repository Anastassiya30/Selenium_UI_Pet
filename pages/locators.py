from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '.p-menuitem:nth-child(1) > .p-menuitem-link')
    DETAILS_OF_PET_BUTTON = (By.XPATH, '//*[@id="app"]/main/div/div[2]/div[2]/div/div[1]/div/div[3]/div[1]/button')
    PET_LIKE_BUTTON = (By.CSS_SELECTOR,
                       '#app > main > div > div.p-dataview.p-component.p-dataview-grid.ml-3.mr-3 > div.p-dataview-content > div > div > div > div.product-grid-item-bottom.grid.flex-row.mt-3 > div.col.flex.align-content-end.justify-content-end')
    BUTTON_PAGINATOR = (By.XPATH, '//*[@id="app"]/main/div/div[2]/div[3]/span/button[3]')
    FILTER_BY_TYPE = (By.ID, 'typesSelector')
    DOG = (By.XPATH, '//li[@aria-label="dog"]')
    CAT = (By.ID, 'pv_id_13_1')
    REPTILE = (By.ID, 'pv_id_13_2')
    HAMSTER = (By.ID, 'pv_id_13_3')
    PARROT = (By.ID, 'pv_id_13_4')
    FILTER_BY_NAME = (By.ID, 'petName')
    user_dog = (By.XPATH, '//*[@id="app"]/main/div/div[2]/div[2]/div/div[4]/div')


class LoginPageLocators:
    LOGIN_EMAIL = (By.ID, "login")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, '#password > input')
    LOGIN_BUTTON = (By.CLASS_NAME, "p-button-label")


class RegisterPageLocators:
    REGISTER_LINK = (By.CSS_SELECTOR, "#app > header > div > ul > li:nth-child(2) > a > span")
    REGISTER_EMAIL = (By.ID, "login")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#password > input")
    CONFIRM_PASSWORD = (By.XPATH, '//*[@id="confirm_password"]/input')
    REGISTER_SUBMIT_BUTTON = (By.CLASS_NAME, 'p-button-label')


class ProfilePageLocators:
    EDIT_BUTTON = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/div/div[1]/div/div[2]/button[1]')
    DELETE_BUTTON = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/div/div[1]/div/div[2]/button[2]')
    DELETE_YES = (By.XPATH, '/html/body/div[3]/div[2]/button[2]')
    DELETE_NO = (By.XPATH, '/html/body/div[3]/div[2]/button[1]')
