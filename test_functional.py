from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pytest

@pytest.fixture(scope='module')
def driver():
	return webdriver.Chrome()

def test_home_page(driver):
	driver.get('http://localhost:8000')
	# assert 'Django' in driver.title
	try:
		assert 'To-Do' in driver.title
		header = driver.find_element_by_tag_name('h1')
		assert 'To-Do' in header.text

		input_box = driver.find_element_by_id("id_new_item")
		assert input_box.get_attribute('placeholder') == 'Enter a to-do item'

		input_box.send_keys("Buy peocock feathers")
		input_box.send_keys(Keys.ENTER)
		time.sleep(2)

		table = driver.find_element_by_id("id_list_table")
		rows = table.find_elements_by_tag_name('tr')
		assert '1: Buy peocock feathers' in [row.text.strip() for row in rows]
	finally:
		driver.close()

