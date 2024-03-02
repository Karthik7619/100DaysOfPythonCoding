from selenium import webdriver

# Initialize the WebDriver (assuming Chrome here)
driver = webdriver.Chrome()

# Open Amazon
driver.get("https://www.amazon.com")

# Click on a link that opens a new window (e.g., Gmail)
# Assuming there's a link with id "gmail_link" that opens Gmail
gmail_link = driver.find_element_by_id("gmail_link")
gmail_link.click()

# Get handles of all currently open windows
all_handles = driver.window_handles

# Switch to the new window (Gmail)
driver.switch_to.window(all_handles[1])

# Now you can perform actions on the Gmail window
# For example, you can login to Gmail, send emails, etc.

# After finishing with Gmail, you can close the window if needed
driver.close()

# Switch back to the original window (Amazon)
driver.switch_to.window(all_handles[0])

# Now you can continue interacting with elements on the Amazon window
# For example, you can search for products, add items to cart, etc.

# Close the WebDriver
driver.quit()
