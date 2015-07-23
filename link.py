from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from os.path import expanduser

my_login = 'g.mishchevskii@gmail.com'
my_password = input('Password: ')
count = 0

driver = webdriver.Chrome(os.path.expanduser(r'~\Dropbox\Work\Python\chromedriver.exe'))
driver.get('https://www.linkedin.com/nhome/')
driver.implicitly_wait(60)

log_in = driver.find_element_by_xpath("//div[@class='fieldgroup']/input[@id='session_key-login']")
password = driver.find_element_by_xpath("//div[@class='fieldgroup']/input[@id='session_password-login']")
sign_in_button = driver.find_element_by_xpath("//li[@class='button']/input[@id='signin']")

log_in.send_keys(my_login)
password.send_keys(my_password)
sign_in_button.click()

driver.get('https://www.linkedin.com/inbox/#invitations')
driver.implicitly_wait(60)

names = driver.find_elements_by_xpath("//p[@class='participants']//a")
positions = driver.find_elements_by_xpath("//p[@class='headline']")

try: 
	invitations = driver.find_elements_by_xpath("//a[@class='accept accept-invite']")
except NoSuchElementException:
	driver.quit()
	print('Nothing to accept')
	exit()

num = 0
for name in names:
	try:
		print('\n' + '{:*>80}'.format(name.text) + '\n' + '{:>80}'.format(positions[num].text) + '\n' + name.get_attribute('href'))
	except UnicodeEncodeError:
		try:
			print('\n' + '{:*>80}'.format(name.text) + '\n' + name.get_attribute('href'))
		except UnicodeEncodeError:
			print('\n' + name.get_attribute('href'))
	num += 1

action = input('\nStart accepting? ')

if action == 'no':
	exit()

driver.get('https://www.linkedin.com/inbox/#invitations')
driver.implicitly_wait(60)
invitations = driver.find_elements_by_xpath("//a[@class='accept accept-invite']")

for invitation in invitations:
	invitation.click()
	driver.implicitly_wait(5)
	count += 1
print(str(count) + ' invitations are accepted')

driver.quit()
exit()
