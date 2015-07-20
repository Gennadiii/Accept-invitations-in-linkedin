from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.common.action_chains import ActionChains
import os.path

my_login = 'g.mishchevskii@gmail.com'
my_password = input('Password: ')
wanted_list = ['hr', 'recruiter', 'рекрутер', 'recruitment', 'open', 'looking', 'talent','resercher', 'wanted']

count = 0
people_number = int(input('Enter a number of people you want to add: '))

driver = webdriver.Chrome(os.path.expanduser(r'~\Dropbox\Work\Python\chromedriver.exe'))
driver.implicitly_wait(60)
driver.get('https://www.linkedin.com/nhome/')

log_in = driver.find_element_by_xpath("//div[@class='fieldgroup']/input[@id='session_key-login']")
password = driver.find_element_by_xpath("//div[@class='fieldgroup']/input[@id='session_password-login']")
sign_in_button = driver.find_element_by_xpath("//li[@class='button']/input[@id='signin']")

log_in.send_keys(my_login)
password.send_keys(my_password)
sign_in_button.click()

while count < people_number:
    driver.get('https://www.linkedin.com/people/pymk/hub?trk=hp-feed-xconny-icon')
    driver.implicitly_wait(10)

    people = driver.find_elements_by_xpath("//div[@class='card-wrapper']//p[@class='headline']/span[@title]")
    buttons = driver.find_elements_by_xpath("//div[@class='card-wrapper']//button[@data-act='request']")
    card = driver.find_elements_by_xpath("//div[@class='card-wrapper']")
    delete = driver.find_elements_by_xpath("//button[@class='bt-close']")

    num = 0
    for person in card:
        flag = False
        for wanted in wanted_list:
            if wanted in people[num].text.lower():
                buttons[num].click()
                count += 1
                print(str(count) + ' - ')
                break
            else:
                flag = True

        if flag:
            ActionChains(driver).move_to_element(person).perform()
            try:
                delete[num].click()
            except ElementNotVisibleException:
                pass
        
        num += 1
        if num > 7:
            break

driver.quit()
exit()
