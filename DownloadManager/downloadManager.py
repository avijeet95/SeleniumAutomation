from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def download(title):
	#Initialise Driver
	driver = webdriver.Chrome()
	driver.get("http://dayt.se/forum/search.php")
	#Find Elements on Page for Navigation
	elem = driver.find_element_by_name("query")
	elem.send_keys(title)
	elem.send_keys(Keys.RETURN)

	elem = driver.find_element_by_class_name("title")
	elem.click()

	elem = driver.find_element_by_id("dm2")
	elem.click()

	#Switch To correct Window
	ctr=0
	for x in driver.window_handles:
		driver.switch_to_window(driver.window_handles[ctr])
		if driver.title=="MEGA":
			break
		ctr=ctr+1
	driver.set_window_size(1124, 850)

	#Executes Downloading Command in Terminal
	cmd = "megadl '"+driver.current_url+"'"
	os.system(cmd)
	driver.close()


#Call Download Function
download("Title")