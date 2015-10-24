from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from os.path import expanduser
from time import sleep

driver = webdriver.Chrome(expanduser(r'~\Dropbox\Work\Python\chromedriver.exe'))
driver.maximize_window()
driver.get('https://www.linkedin.com/nhome/')
driver.implicitly_wait(60)

input('Let\'s roll!')

driver.get('https://www.linkedin.com/people/pymk/hub?ref=global-nav&trk=nav_utilities_invites_header')

see_more = driver.find_element_by_xpath("//span[contains(text(), 'See more')]")
see_more.click()

input('Start accepting?')

count = 0
avatars = driver.find_elements_by_class_name('avatar')

for avatar in avatars:
	ActionChains(driver).move_to_element(avatar).perform()
	accept = driver.find_element_by_xpath("//span[contains(text(), 'Accept invitation')]")
	accept.click()
	sleep(2)
	count += 1
driver.quit()

input(str(count) + ' invitations have been accepted.')
exit()
