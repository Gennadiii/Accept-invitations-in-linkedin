from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

count = 0

driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\chromedriver.exe')
driver.implicitly_wait(60)
driver.get('https://www.linkedin.com/nhome/')
driver.find_element_by_xpath("//div[@class='fieldgroup']/input[@id='session_key-login']").send_keys('*')
driver.find_element_by_xpath("//div[@class='fieldgroup']/input[@id='session_password-login']").send_keys('*')
driver.find_element_by_xpath("//li[@class='button']/input[@id='signin']").click()
driver.get('https://www.linkedin.com/inbox/#invitations')
try: 
	invitations = driver.find_elements_by_xpath("//a[@class='accept accept-invite']")
except NoSuchElementException:
	driver.quit()
	print('Nothing to accept')
	exit()

names = driver.find_elements_by_xpath("//p[@class='participants']//a")
positions = driver.find_elements_by_xpath("//p[@class='headline']")

num = 0
for name in names:
	print('\n' + '{:*>80}'.format(name.text) + '\n' + '{:>80}'.format(positions[num].text) + '\n' + name.get_attribute('href'))
	num += 1

action = input('\nStart accepting? ')

if action == 'no':
	exit()

for invitation in invitations:
	invitation.click()
	count += 1
print(str(count) + ' invitations are accepted')

driver.quit()
exit()
