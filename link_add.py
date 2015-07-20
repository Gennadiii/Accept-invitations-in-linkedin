from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.common.action_chains import ActionChains
import os.path
from time import sleep

my_login = 'g.mishchevskii@gmail.com'
my_password = input('Password: ')
wanted_list = ['hr', 'recruiter', 'рекрутер', 'recruitment', 'open', 'looking', 'talent','resercher', 'wanted']

count = 0
people_number = int(input('Enter a number of people you want to add: '))

driver = webdriver.Chrome(os.path.expanduser(r'~\Dropbox\Work\Python\chromedriver.exe'))
driver.get('https://www.linkedin.com/nhome/')
driver.implicitly_wait(60)

log_in = driver.find_element_by_xpath("//div[@class='fieldgroup']/input[@id='session_key-login']")
password = driver.find_element_by_xpath("//div[@class='fieldgroup']/input[@id='session_password-login']")
sign_in_button = driver.find_element_by_xpath("//li[@class='button']/input[@id='signin']")

log_in.send_keys(my_login)
password.send_keys(my_password)
sign_in_button.click()

while count < people_number:
    driver.get('https://www.linkedin.com/people/pymk/hub?trk=hp-feed-xconny-icon')
    driver.implicitly_wait(20)

    positions = driver.find_elements_by_xpath("//div[@class='card-wrapper']//p[@class='headline']/span[@title]")
    names = driver.find_elements_by_xpath("//h4[@class='name']//a[@class='title']")
    buttons = driver.find_elements_by_xpath("//div[@class='card-wrapper']//button[@data-act='request']")
    card = driver.find_elements_by_xpath("//div[@class='card-wrapper']")
    delete = driver.find_elements_by_xpath("//button[@class='bt-close']")

    for num in range(8):
        flag = False
        for wanted in wanted_list:
            if wanted in positions[num].text.lower():
                buttons[num].click()

                if 'Enter' in driver.find_element_by_xpath("//div[@class='email-confirm']").text:
                    ActionChains(driver).move_to_element(card[num]).perform()
                    driver.implicitly_wait(20)
                    try:
                        delete[num].click()
                    except ElementNotVisibleException:
                        pass

                count += 1

                print('{:->40}'.format(str(count)))
                try:
                    print(names[num].text)
                except UnicodeEncodeError:
                    pass
                break
            else:
                flag = True

        if flag:
            ActionChains(driver).move_to_element(card[num]).perform()
            driver.implicitly_wait(20)
            try:
                delete[num].click()
            except ElementNotVisibleException:
                pass
    sleep(3)

driver.quit()
exit()
