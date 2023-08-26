from behave import *
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import re

@given(u'I am on the Demo Login Page')
def demologinpage(context):
    ser_obj = Service("E:/Python Selenium webdriver/Driver file/chromedriver-win32/chromedriver.exe")
    context.driver = webdriver.Chrome(service=ser_obj)
    context.driver.get("https://www.saucedemo.com/")
    context.driver.maximize_window()


@when(u'I fill the account information for account StandardUser into the Username field and the Password field')
def credentialslogin(context):
    user_name = context.driver.find_element(By.XPATH, "//input[@id='user-name']")
    user_name.send_keys("standard_user")
    u_password = context.driver.find_element(By.XPATH, "//input[@id='password']")
    u_password.send_keys("secret_sauce")


@when(u'I click the Login Button')
def loginclick(context):
    context.driver.find_element(By.XPATH, "//input[@id='login-button']").click()


@then(u'I am redirected to the Demo Main Page')
def urlverify(context):
    context.title = context.driver.title
    assert context.title == "Swag Labs"


@then(u'I verify the App Logo exists')
def verifylogo(context):
    logo = context.driver.find_element(By.XPATH, "//div[@class='app_logo']")
    assert logo.is_displayed()
    screenshot_name = "verifylogo" + ".png"
    context.driver.save_screenshot(screenshot_name)

@when(u'I fill the account information for account LockedOutUser into the Username field and the Password field')
def credentiallockedout(context):
    user_name = context.driver.find_element(By.XPATH, "//input[@id='user-name']")
    user_name.send_keys("locked_out_user")
    u_password = context.driver.find_element(By.XPATH, "//input[@id='password']")
    u_password.send_keys("secret_sauce")


@then(u'I verify the Error Message contains the text "Sorry, this user has been banned."')
def userbannedverify(context):
    verify_text = context.driver.find_element(By.XPATH,"//h3[contains(text(),'Epic sadface: Sorry, this user has been locked out')]").text
    assert verify_text == "Epic sadface: Sorry, this user has been locked out."
    screenshot_name = "Banneduser" + ".png"
    context.driver.save_screenshot(screenshot_name)

@given(u'I am on the inventory Page')
def inventorypage(context):
    status1 = context.driver.find_element(By.XPATH,"//span[@class='title']").is_displayed()
    assert status1 is True

@when(u'user sorts products from low price to high price')
def sortproducts(context):
    drop_down = context.driver.find_element(By.XPATH, "//select[@class='product_sort_container']")
    select = Select(drop_down)
    select.select_by_visible_text("Price (low to high)")


@when(u'user adds lowest priced product')
def addlowpriceprod(context):
    context.driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-onesie']").click()


@when(u'user clicks on cart')
def addingincart(context):
   context.driver.find_element(By.XPATH,"//a[@class='shopping_cart_link']").click()


@when(u'user clicks on checkout')
def checkout(context):
    context.driver.find_element(By.XPATH,"//button[@id='checkout']").click()


@when(u'user enters first name John')
def firstname(context):
    context.driver.find_element(By.XPATH,"//input[@id='first-name']").send_keys("John")


@when(u'user enters last name Doe')
def lastname(context):
    context.driver.find_element(By.XPATH,"//input[@id='last-name']").send_keys("Doe")


@when(u'user enters zip code 123')
def zip_code(context):
    context.driver.find_element(By.XPATH,"//input[@id='postal-code']").send_keys("123")


@when(u'user clicks Continue button')
def clickcontinue(context):
    context.driver.find_element(By.XPATH,"//input[@id='continue']").click()


@then(u'I verify in Checkout overview page if the total amount for the added item is $8.63')
def verifyprice(context):
    input_string = context.driver.find_element(By.XPATH, "//div[@class='summary_info_label summary_total_label']").text
    decimal_number = re.findall(r'[$]\d+\.\d+', input_string)
    assert decimal_number[0] == "$8.63"


@when(u'user clicks Finish button')
def clickfinishbutton(context):
    context.driver.find_element(By.XPATH,"//button[@id='finish']").click()


@then(u'Thank you header is shown in Checkout complete page')
def step_impl(context):
    thank_text = context.driver.find_element(By.XPATH,"//h2[normalize-space()='Thank you for your order!']").text
    assert thank_text == "Thank you for your order!"
    screenshot_name = "Thankyoupage" + ".png"
    context.driver.save_screenshot(screenshot_name)