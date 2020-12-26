from selenium import webdriver
path ='/Users/robertcarroll/PycharmProjects/seleniumTest/drivers/chromedriver'
driver = webdriver.Chrome(executable_path=path)
driver.get('http://www.google.com')
