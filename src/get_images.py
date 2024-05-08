from selenium import webdriver
import os
def take_screenshot(url, output_file):
    """
    Takes a screenshot of a web page and saves it to the specified file.

    Args:
    url (str): The URL of the web page to capture.
    output_file (str): The file path where the screenshot will be saved.
    """
    # Configure the browser
    options = webdriver.ChromeOptions()
    options.add_argument('headless')  # Run in headless mode (without a window)
    driver = webdriver.Chrome(options=options)

    # Set the browser window size
    driver.set_window_size(800, 500)

    # Open the web page
    driver.get(url)

    # Take a screenshot
    driver.save_screenshot(output_file)

    # Close the browser
    driver.quit()


