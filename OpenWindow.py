from selenium import webdriver
from time import sleep

driver =webdriver.Chrome()
driver.get("https://www.amazon.in/")
print(driver.title)
sleep(5)
driver.execute_script("window.open('https://www.facebook.com/','new_window')")
all_windows = driver.window_handles
driver.switch_to.window(all_windows[1])
print(driver.title)
sleep(5)
driver.close()
driver.switch_to.window(all_windows[0])
print(driver.title)
driver.quit()