from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from os.path import expanduser
from time import sleep

count = 0

driver = webdriver.Chrome(expanduser(r'~\Dropbox\Work\Python\chromedriver.exe'))
driver.maximize_window()
driver.get('https://www.linkedin.com/nhome/')
driver.implicitly_wait(60)

input('Let\'s roll!')

driver.get('https://www.linkedin.com/inbox/#invitations')

input('Start accepting?')

while True:
	driver.get('https://www.linkedin.com/inbox/#invitations')
	driver.implicitly_wait(60)
	if driver.find_element_by_xpath("//a[@href='/inbox/#invitations']").text == 'Invitations':
		break
	invitations = driver.find_elements_by_xpath("//a[@class='accept accept-invite']")
	for invitation in invitations:
		invitation.click()
		sleep(3)
		count += 1

driver.quit()
input(str(count) + ' invitations have been accepted.')
exit()
