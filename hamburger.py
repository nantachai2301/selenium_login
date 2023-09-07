# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# from selenium.webdriver.support.ui import Select

# # ระบุพาธของ ChromeDriver 
# chrome_driver_path = "C:/Users/jay/chromedriver.exe"

# # เริ่มต้น WebDriver
# driver = webdriver.Chrome()
# # ขยายหน้าต่างเบราว์เซอร์ให้เต็มหน้าจอ
# driver.maximize_window()

# # เปิดเว็บไซต์ของคุณ
# driver.get("https://online-web-mauve.vercel.app/")
# # คลิกปุ่ม "เข้าสู่ระบบ"
# open_modal_button = driver.find_element(By.XPATH, "//span[text()='เข้าสู่ระบบ']")
# open_modal_button.click()

# # ระบุ element ของรหัสประจำตัวประชาชนและรหัสผ่านใน Modal
# id_input = driver.find_element(By.XPATH, "//label[text()='รหัสประจำตัวประชาชน']/following-sibling::input")
# password_input = driver.find_element(By.XPATH, "//label[text()='รหัสผ่าน']/following-sibling::input")

# # กรอกข้อมูลใน input field
# id_input.send_keys("7788888888888")
# password_input.send_keys("123456")

# time.sleep(2)

# # คลิกปุ่ม "เข้าสู่ระบบ" ด้วย XPath
# login_button = driver.find_element(By.XPATH, "//button[text()='เข้าสู่ระบบ']")
# login_button.click()

# # รอสักครู่เพื่อให้หน้าเว็บโหลดและดำเนินการต่อ
# time.sleep(5)  # รอ 5 วินาที (หรือตามที่คุณต้องการ)

# # คลิกที่ปุ่ม "เมนู" โดยใช้ XPath และคำอธิบาย (aria-label)
# menu_button = driver.find_element(By.XPATH, "//button[@aria-label='menu']")
# menu_button.click()
# time.sleep(2)
# # คลิกที่ปุ่ม "โปรไฟล์" โดยใช้ XPath และคำอธิบาย (aria-label)
# profile_button = driver.find_element(By.XPATH, "//div[@aria-label='โปรไฟล์']")
# profile_button.click()

# time.sleep(5)






from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select


# ระบุพาธของ ChromeDriver 
chrome_driver_path = "C:/Users/jay/chromedriver.exe"

# เริ่มต้น WebDriver
driver = webdriver.Chrome()
# ขยายหน้าต่างเบราว์เซอร์ให้เต็มหน้าจอ
driver.maximize_window()

# เปิดเว็บไซต์ของคุณ
driver.get("https://online-web-mauve.vercel.app/")
# คลิกปุ่ม "เข้าสู่ระบบ"
open_modal_button = driver.find_element(By.XPATH, "//span[text()='เข้าสู่ระบบ']")
open_modal_button.click()

# ระบุ element ของรหัสประจำตัวประชาชนและรหัสผ่านใน Modal
id_input = driver.find_element(By.XPATH, "//label[text()='รหัสประจำตัวประชาชน']/following-sibling::input")
password_input = driver.find_element(By.XPATH, "//label[text()='รหัสผ่าน']/following-sibling::input")

# กรอกข้อมูลใน input field
id_input.send_keys("1729800262972")
password_input.send_keys("111111")

time.sleep(2)

# คลิกปุ่ม "เข้าสู่ระบบ" ด้วย XPath
login_button = driver.find_element(By.XPATH, "//button[text()='เข้าสู่ระบบ']")
login_button.click()

# รอสักครู่เพื่อให้หน้าเว็บโหลดและดำเนินการต่อ
time.sleep(5)  # รอ 5 วินาที (หรือตามที่คุณต้องการ)

# คลิกที่ปุ่ม "เมนู" โดยใช้ XPath และคำอธิบาย (aria-label)
menu_button = driver.find_element(By.XPATH, "//button[@aria-label='menu']")
menu_button.click()
time.sleep(2)
# คลิกที่ปุ่ม "โปรไฟล์" โดยใช้ XPath และคำอธิบาย (aria-label)
profile_button = driver.find_element(By.XPATH, "//div[@aria-label='โปรไฟล์']")
profile_button.click()

time.sleep(5)


# ระบุ element ของ <button> โดยใช้คลาส "btn-warning" และข้อความ "แก้ไขโปรไฟล์"
button_element = driver.find_element(By.XPATH, "//button[@class='btn btn-warning mx-1' and text()='แก้ไขโปรไฟล์']")

# คลิกที่ <button>
button_element.click()
time.sleep(3) 

# ระบุ element ของ <input> โดยใช้ attribute name="first_name"
first_name_input = driver.find_element(By.XPATH, "//input[@name='first_name']")

# ล้างข้อมูลที่อาจจะมีอยู่ใน input field ก่อนจะกรอก
first_name_input.clear()

# กรอกข้อมูล "ณรงค์ฤทธิ์" ลงใน input field
first_name_input.send_keys("มอส")
time.sleep(3) 

# ระบุ element ของ <button> โดยใช้ attribute class="btn btn-success mx-1" และข้อความ "บันทึก"
save_button = driver.find_element(By.XPATH, "//button[@class='btn btn-success mx-1' and contains(text(), 'บันทึก')]")

# คลิกที่ <button>
save_button.click()
time.sleep(3) 

# ค้นหาปุ่ม "อัปเดต" โดยใช้ XPath
update_button = driver.find_element(By.XPATH, '//button[contains(text(), "อัปเดต")]')

# คลิกปุ่ม "อัปเดต"
update_button.click()
time.sleep(3) 


time.sleep(5) 





