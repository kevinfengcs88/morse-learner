from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from strings import get_string
from translator import encode
from actions import auto_type
import requests

options = webdriver.ChromeOptions() # add options to prevent selenium from printing garbage errors to console
options.add_experimental_option('excludeSwitches', ['enable-logging'])

response = requests.get("https://genemecija.github.io/learn-morse-code/")
print("URL: " + response.url)
status = response.status_code
print("HTTP status code: " + str(status), end="")
if status == 200:
    print(", Success")
else:
    print(", Error")
s = Service("C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(service=s, options=options)
driver.get("https://genemecija.github.io/learn-morse-code/")
driver.implicitly_wait(10)
key = driver.find_element(By.ID, "morseButton")
action = ActionChains(driver)


def main():
    clear = driver.find_element(By.ID, "clear-history")
    driver.execute_script("var ele = arguments[0];ele.addEventListener('click', function() {ele.setAttribute("
                          "'automationTrack','true');});", clear)
    input_string = get_string()
    driver.execute_script("var ele = arguments[0]; ele.setAttribute('automationTrack', 'false')", clear)
    morse = encode(input_string)
    print("Click on \"Clear\" for the bot to start typing")

    try:
        while True:
            if clear.get_attribute("automationTrack") == "true":
                print(f"\'{input_string}\' in Morse code: ", end="")
                auto_type(morse, action, key)
                driver.execute_script("var ele = arguments[0]; ele.setAttribute('automationTrack', 'false')", clear)
                break
    finally:
        pass


while True:
    main()

