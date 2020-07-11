from selenium import webdriver  
from bs4 import BeautifulSoup
print('AUST IUMS auto login')
print('____________________')



usr=input('Enter User Id:') 
passfile = open("password.txt","r")
pwd = passfile.read()

driver = webdriver.Chrome() 
driver.get('https://iums.aust.edu/ums-web/login/') 
print ("Opened IUMS") 
 

username_box = driver.find_element_by_id('userName') 
username_box.send_keys(usr) 
print ("Email Id entered") 


password_box = driver.find_element_by_id('password') 
password_box.send_keys(pwd) 
print ("Password entered") 

login_box = driver.find_element_by_id('login_btn') 
login_box.click()


print(a)
print ("Done") 
input('Press anything to quit') 
driver.quit() 
print("Finished") 

