import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import getpass
passwd = getpass.getpass()
course=input("Enter course: ")
service = Service(executable_path=EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service)
driver.get("https://hello.iitk.ac.in/index.php/user/login")
course_dict={
"chm102":"https://hello.iitk.ac.in/index.php/course/chm102aa2122",
"mth102":"https://hello.iitk.ac.in/course/mth102aa2122",
"phy102":"https://hello.iitk.ac.in/course/phy102aa2122",
"phy101":"https://hello.iitk.ac.in/course/phy101aa2122",
"ta101":"https://hello.iitk.ac.in/ta101aa2122"}
driver.implicitly_wait(5)
username= driver.find_element_by_id("edit-name")
username.send_keys("jdevansh21@iitk.ac.in")
password= driver.find_element_by_id("edit-pass")
password.send_keys(passwd)
signin=driver.find_element_by_id("edit-submit")
signin.click()
driver.get(course_dict[course])
access=driver.find_element_by_id("edit-access-course")
access.click()
time.sleep(3600)
driver.quit()
