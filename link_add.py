from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

count = 0

driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\chromedriver.exe')
driver.implicitly_wait(60)
driver.get('https://www.linkedin.com/nhome/')
driver.find_element_by_xpath("//div[@class='fieldgroup']/input[@id='session_key-login']").send_keys('*')
driver.find_element_by_xpath("//div[@class='fieldgroup']/input[@id='session_password-login']").send_keys('*')
driver.find_element_by_xpath("//li[@class='button']/input[@id='signin']").click()

while count < 100:
    driver.get('https://www.linkedin.com/people/pymk/hub?trk=hp-feed-xconny-icon')
    driver.implicitly_wait(10)
    people = driver.find_elements_by_xpath("//div[@class='card-wrapper']//p[@class='headline']/span[@title]")
    buttons = driver.find_elements_by_xpath("//div[@class='card-wrapper']//button[@data-act='request']")
    card = driver.find_elements_by_xpath("//div[@class='card-wrapper']")
    delete = driver.find_elements_by_xpath("//button[@class='bt-close']")
    num = 0
    # sleep(3)
    for person in card:
        if 'hr' in people[num].text.lower() or 'recruiter' in people[num].text.lower() or 'рекрутер' in people[num].text.lower() \
        or 'recruitment' in people[num].text.lower() or 'open' in people[num].text.lower() or 'looking' in people[num].text.lower() or \
        'talent' in people[num].text.lower() or 'resercher' in people[num].text.lower() or wanted in people[num].text.lower():
            buttons[num].click()
            count += 1
            print(str(count))
        else:
            ActionChains(driver).move_to_element(person).perform()
            try:
                delete[num].click()
            except ElementNotVisibleException:
                pass
        num += 1
        if num == 8:
            break

driver.quit()
exit()
