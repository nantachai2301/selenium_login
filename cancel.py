from selenium import webdriver
from selenium.webdriver.common.by import By
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
id_input.send_keys("7788888888888")
password_input.send_keys("123456")

time.sleep(2)

# คลิกปุ่ม "เข้าสู่ระบบ" ด้วย XPath
login_button = driver.find_element(By.XPATH, "//button[text()='เข้าสู่ระบบ']")
login_button.click()

time.sleep(5)

queue_list_button = driver.find_element(By.XPATH, "//h4[text()='รายการจองคิว']")

# คลิกปุ่มนี้
queue_list_button.click()
time.sleep(2)

# คลิกที่ input ประเภทวันที่ (type="date")
date_input = driver.find_element(By.XPATH, "//input[@type='date']")
date_input.click()

# ตั้งค่าวันที่เป็นวันนี้ (สามารถใช้วิธีอื่น ๆ ในการตั้งค่าวันที่ตามที่คุณต้องการ)
date_input.clear()
date_input.send_keys("13-09-2023")  # เอาเป็นวันเดือนปีนะจ๊ะ

time.sleep(2)

department_dropdown = Select(driver.find_element(By.XPATH, "//select[@class='form-select']"))
# เลือกแผนกที่คุณต้องการ (เช่น "ทันตกรรม")
department_dropdown.select_by_visible_text("ทันตกรรม")

time.sleep(2)

queue_status_dropdown = Select(driver.find_element(By.XPATH, "//div[@class='col-2']//select[@class='form-select']"))

# เลือกคิวที่คุณต้องการ (เช่น "คิวที่จอง") ( "1" คิวที่จอง ) ("2" คิวที่กำลังดำเนินการ ) ("4"  ประวัติการจองคิว )
queue_status_dropdown.select_by_value("1")


time.sleep(3)
# คลิกปุ่ม "ยกเลิกคิว" โดยใช้ XPath
cancel_queue_button = driver.find_element(By.XPATH, "//button[@class='btn btn-danger text-white mx-1 mt-1']")
cancel_queue_button.click()

time.sleep(2)

# คลิกปุ่ม "ใช่, ยกเลิกคิว" โดยใช้ XPath
confirm_cancel_button = driver.find_element(By.XPATH, "//button[text()='ใช่, ยกเลิกคิว']")
confirm_cancel_button.click()



time.sleep(5)
