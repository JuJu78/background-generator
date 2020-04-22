from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver')

chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

print('Selenium Easy Demo' in chrome_browser.title)

show_message_button = chrome_browser.find_element_by_class_name('btn-default')

user_message = chrome_browser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys('Je suis le plus cool')

show_message_button.click()

output_message = chrome_browser.find_element_by_id('display')

assert 'Je suis le plus cool' in output_message.text
