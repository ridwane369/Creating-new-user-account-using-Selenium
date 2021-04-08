from selenium import webdriver
import re
import time

driver = webdriver.Edge('E:\\Softwares\\edgedriver_win64\\msedgedriver.exe')
regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'


def login(t):
    login_page_url = driver.current_url
    driver.find_element_by_id('email').send_keys(t[0])
    driver.find_element_by_id('passwd').send_keys(t[1])
    print('Logging back in 5 seconds')
    time.sleep(4)
    driver.find_element_by_id('SubmitLogin').click()
    while driver.current_url == login_page_url :
        time.sleep(0.1)
    print('Successful user creation verified')

def send_email(u1):
    email = get_email()
    driver.find_element_by_id('email_create').send_keys(email)
    driver.find_element_by_id('SubmitCreate').click()
    time.sleep(5)
    if(driver.current_url == u1):
        print('The email was not novel, enter a novel one')
        driver.find_element_by_id('email_create').clear()
        send_email(u1)
    else:
        print('Novel email Found!')
    return email

def get_email():
    email = input("Provide email id:\n")
    while(not(re.search(regex, email))):
        email = input("Please provide an valid email id:\n")
    return email

def create_Account():
    driver.get('http://automationpractice.com/index.php')
    main_page_url = driver.current_url
    driver.find_element_by_link_text('Sign in').click()
    while(driver.current_url == main_page_url):
        time.sleep(0.1)
    u1 = driver.current_url
    email = send_email(u1)
    driver.find_element_by_id('id_gender1').click()
    driver.find_element_by_id('customer_firstname').send_keys('Ridwane')
    driver.find_element_by_id('customer_lastname').send_keys('ul-Islam')
    password = '12345'
    driver.find_element_by_id('passwd').send_keys(password)
    driver.find_element_by_id('uniform-newsletter').click()
    driver.find_element_by_xpath('//*[@id="days"]/option[11]').click() #date
    driver.find_element_by_xpath('//*[@id="months"]/option[9]').click() #month
    driver.find_element_by_xpath('//*[@id="years"]/option[38]').click() #year
    driver.find_element_by_id('address1').send_keys('Demo Location')
    driver.find_element_by_id('city').send_keys('Demo City')
    driver.find_element_by_xpath('//*[@id="id_state"]/option[4]').click()
    driver.find_element_by_id('postcode').send_keys('85013')
    driver.find_element_by_id('phone_mobile').send_keys('059161318')
    driver.find_element_by_id('alias').clear()
    driver.find_element_by_id('alias').send_keys('Sample Text')
    time.sleep(3)
    info_page_url = driver.current_url
    driver.find_element_by_id('submitAccount').click()
    while (driver.current_url == info_page_url):
        time.sleep(0.1)
    print('Account created successfully, Signing out in 5 seconds')
    account_page_url = driver.current_url
    time.sleep(4)
    driver.find_element_by_link_text('Sign out').click()
    while driver.current_url == account_page_url :
        time.sleep(0.1)
    return (email,password)

#driver Code
t = create_Account()
print(t)
login(t)
