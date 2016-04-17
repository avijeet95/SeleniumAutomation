from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time,sys,os
from config import count

def schedule():
	#Fetches Day 
	day = datetime.datetime.today().weekday()
	
	#Add Title of Series here. Day 0 stands for Sunday.
	if day == 0:
		download("title")
	elif day == 1:
		download("title")
	elif day == 2:
		download("title")
	elif day == 3:
		download("title")
	elif day == 4:
		download("title")
	elif day == 5:
		download("title")


def download(title):
	#Initialise Driver
	driver = webdriver.Chrome()
	driver.get("http://dayt.se/forum/search.php")
	#Find Elements on Page for Navigation
	elem = driver.find_element_by_name("query")
	elem.send_keys(title)
	elem.send_keys(Keys.RETURN)

	elem = driver.find_element_by_class_name("title")
	ext = elem.text
	text = text.split(" ")
	
	#Checks For Latest Episode According to Config File
	if count[title]['season'] <= int(text[-11]) and count[title]['episode'] < int(text[-9]):
		elem.click()

		elem = driver.find_element_by_id("dm2")
		elem.click()

		ctr=0
		for x in driver.window_handles:
			driver.switch_to_window(driver.window_handles[ctr])
			if driver.title=="MEGA":
				break
			ctr=ctr+1
		driver.set_window_size(1124, 850)

		cmd = "megadl '"+driver.current_url+"'"
		os.system(cmd)
		
	driver.close()

#Initiates Downloads According to schedule
schedule()