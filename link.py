from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

count = 0

driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\chromedriver.exe')
driver.implicitly_wait(200)
driver.get('https://www.linkedin.com/nhome/')
# driver.find_element_by_xpath("//div[@class='fieldgroup']/input[@id='session_key-login']").send_keys(Keys.WIN + 'd')
driver.find_element_by_xpath("//div[@class='fieldgroup']/input[@id='session_key-login']").send_keys('g.mishchevskii@gmail.com')
driver.find_element_by_xpath("//div[@class='fieldgroup']/input[@id='session_password-login']").send_keys('1890_suMmer_32015')
driver.find_element_by_xpath("//li[@class='button']/input[@id='signin']").click()
driver.get('https://www.linkedin.com/inbox/#invitations')
try: 
	invitation = driver.find_elements_by_xpath("//a[@class='accept accept-invite']")
except NoSuchElementException:
	pass
	driver.quit()
	print('Nothing to accept')
	exit()

names = driver.find_elements_by_xpath("//p[@class='participants']//a")

for name in names:
	print(name.text + '\n' + name.get_attribute('href') + '\n')

input('Start accepting?')

for invitation in invitations:
	invitation.click()
	count += 1
print(str(count) + ' invitations are accepted')

driver.quit()
exit()
