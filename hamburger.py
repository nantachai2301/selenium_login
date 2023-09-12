from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

# เริ่มต้น WebDriver
driver = webdriver.Chrome()
driver.maximize_window()
# เปิดเว็บไซต์ของคุณ
driver.get("https://online-web-mauve.vercel.app/")
open_modal_button = driver.find_element(By.XPATH, "//span[text()='เข้าสู่ระบบ']")
open_modal_button.click()

# ระบุ element ของรหัสประจำตัวประชาชนและรหัสผ่านใน Modal
id_input = driver.find_element(By.XPATH, "//label[text()='รหัสประจำตัวประชาชน']/following-sibling::input")
password_input = driver.find_element(By.XPATH, "//label[text()='รหัสผ่าน']/following-sibling::input")

# กรอกข้อมูลใน input field
id_input.send_keys("7788888888888")
password_input.send_keys("123456")

time.sleep(2)

# คลิกปุ่ม "เข้าสู่ระบบ"
login_button = driver.find_element(By.XPATH, "//button[text()='เข้าสู่ระบบ']")
login_button.click()

# รอสักครู่เพื่อให้หน้าเว็บโหลดและดำเนินการต่อ
time.sleep(5)  # รอ 5 วินาที (หรือตามที่คุณต้องการ)

# คลิกที่ปุ่ม "เมนู" โดยใช้ XPath และคำอธิบาย (aria-label)
menu_button = driver.find_element(By.XPATH, "//button[@aria-label='แฮ่มเบอเกอร์']")
menu_button.click()
time.sleep(2)
# คลิกที่ปุ่ม "โปรไฟล์" โดยใช้ XPath และคำอธิบาย (aria-label)
profile_button = driver.find_element(By.XPATH, "//div[@aria-label='โปรไฟล์']")
profile_button.click()

time.sleep(5)

# ระบุ element ของ <button> โดยใช้คลาส "btn btn-warning" และข้อความ "แก้ไขโปรไฟล์"
button_element = driver.find_element(By.XPATH, "//button[@class='btn btn-warning mx-1' and text()='แก้ไขโปรไฟล์']")

# คลิกที่ <button>
button_element.click()
time.sleep(3) 

# ระบุ element ของ <input> โดยใช้ attribute name="first_name"
first_name_input = driver.find_element(By.XPATH, "//input[@name='first_name']")

# ล้างข้อมูลที่อาจจะมีอยู่ใน input field ก่อนจะกรอก
first_name_input.clear()

# กรอกข้อมูล "ณรงค์ฤทธิ์" ลงใน input field
first_name_input.send_keys("หมูท่อ")
time.sleep(3) 

# รอให้ปุ่ม "บันทึก" แสดงขึ้นบนหน้าเว็บ
save_button = driver.find_element(By.XPATH, "//button[@class='btn btn-success mx-1' and contains(text(), 'บันทึก')]")


# คลิกที่ <button>
# คลิกที่ปุ่ม "บันทึก" โดยใช้ JavaScript
driver.execute_script("arguments[0].click();", save_button)

time.sleep(3) 

# ค้นหาปุ่ม "อัปเดต" โดยใช้ XPath
confirm_button = driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled']")

# คลิกปุ่ม "อัปเดต"
confirm_button.click()
time.sleep(3) 


