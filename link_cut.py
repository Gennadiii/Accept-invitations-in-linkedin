from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from os.path import expanduser
from time import sleep

count = 0

driver = webdriver.Chrome(expanduser(r'~\Dropbox\Work\Python\chromedriver.exe'))
driver.get('https://www.linkedin.com/nhome/')
driver.implicitly_wait(60)

input('Let\'s roll!')

driver.get('https://www.linkedin.com/inbox/#invitations')
driver.implicitly_wait(60)

names = driver.find_elements_by_xpath("//p[@class='participants']//a")
positions = driver.find_elements_by_xpath("//p[@class='headline']")

invitations = driver.find_elements_by_xpath("//a[@class='accept accept-invite']")


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

if len(action) != 0:
	exit()
else:
	driver.get('https://www.linkedin.com/inbox/#invitations')
	driver.implicitly_wait(60)
	invitations = driver.find_elements_by_xpath("//a[@class='accept accept-invite']")
	for invitation in invitations:
		invitation.click()
		driver.implicitly_wait(5)
		sleep(4)
		count += 1
	print(str(count) + ' invitations are accepted')	

driver.quit()
exit()
