import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time

# Create an undetected_chromedriver instance

    # Open the Google Meet link
name = ["Bob1","Bob2","Bob3","Bob4","Bob5","Bob6"]
for x in range(0,6,1):
    driver = uc.Chrome()
    driver.get('https://meet.google.com/pho-wjco-cwv')
    print("Opened The Website")
    time.sleep(20)
    # Wait for the element to be clickable (adjust timeout as needed)
    element = driver.find_element(By.CSS_SELECTOR, '.ksBjEc > .VfPpkd-vQzf8d:nth-child(4)')
    print("Got the Microphone Element")
    time.sleep(10)
    element.click()
    print("Clicked The Microphone Element")
    element4 = driver.find_element(By.CSS_SELECTOR, '.LjDxcd > .VfPpkd-vQzf8d')
    element4.click()
    print("Got the Input Name Field")
    time.sleep(10)
    element1 = driver.find_element(By.CSS_SELECTOR, 'input#c22')
    element1.send_keys(name[x])
    print("Typed the Name")
    time.sleep(10)
    element2 = driver.find_element(By.CSS_SELECTOR, '.XCoPyb > .VfPpkd-dgl2Hf-ppHlrf-sM5MNb:nth-child(1)')
    print("Got the Join Btn")
    time.sleep(5)
    element2.click()
    time.sleep(10)

driver.close()
