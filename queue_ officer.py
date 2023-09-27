from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
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
id_input.send_keys("7777777777777")
password_input.send_keys("123456")

time.sleep(2)

# คลิกปุ่ม "เข้าสู่ระบบ" ด้วย XPath
login_button = driver.find_element(By.XPATH, "//button[text()='เข้าสู่ระบบ']")
login_button.click()

# รอสักครู่เพื่อให้หน้าเว็บโหลดและดำเนินการต่อ
time.sleep(5)  # รอ 5 วินาที (หรือตามที่คุณต้องการ)

link_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//div[contains(text(), "จองคิวผู้ป่วย Walk in")]')
)
)
driver.execute_script("arguments[0].click();", link_element)
time.sleep(2)

# คลิกปุ่ม "เพิ่มผู้ป่วย Walk In" โดยใช้ ID
add_patient_button = driver.find_element(By.ID,"BookingWalkinAddbook-an-appointment")
add_patient_button.click()

time.sleep(2)

# ระบุ element ของฟิลด์เลขบัตรประชาชน
id_card_input = driver.find_element(By.ID, "MainBookAuthor_id_card")

# กรอกเลขบัตรประชาชนในฟิลด์
id_card_input.send_keys("1749800297083")  # แทน "1234567890123" ด้วยเลขบัตรประชาชนที่คุณต้องการ

time.sleep(1)

# ระบุ element ของ dropdown
prefix_name_dropdown = Select(driver.find_element(By.ID, "MainBookAuthor_prefix_name"))

# เลือกคำนำหน้าที่คุณต้องการ (เช่น "นาย")
prefix_name_dropdown.select_by_value("นาย")  # หรือจะใช้ .select_by_visible_text("นาย") ก็ได้

time.sleep(1)

# ระบุ element ของช่องข้อมูลชื่อ
first_name_input = driver.find_element(By.ID, "MainBookAuthor_first_name")

# กรอกชื่อที่คุณต้องการ
first_name_input.send_keys("นันทชัย")

time.sleep(1)

# ระบุ element ของช่องข้อมูลนามสกุล
last_name_input = driver.find_element(By.ID, "MainBookAuthor_last_name")

# กรอกนามสกุลที่คุณต้องการ
last_name_input.send_keys("แสงอรุณ")

time.sleep(1)

# ระบุ element ของเพศ
gender_dropdown = Select(driver.find_element(By.ID, "MainBookAuthor_gender"))

# เลือกเพศที่คุณต้องการ (เช่น "ชาย")
gender_dropdown.select_by_value("ชาย")

time.sleep(1)

# ระบุ element ของวันเดือนปีเกิด
birthday_input = driver.find_element(By.ID, "MainBookAuthor_birthday")

# กรอกข้อมูลใน input field (ในกรณีนี้เราจะใช้ "1990-01-01" เป็นตัวอย่าง)
birthday_input.send_keys("23-01-2002")

time.sleep(1)

# ระบุ element ของน้ำหนัก
weight_input = driver.find_element(By.ID, "MainBookAuthor_weight")

# กรอกข้อมูลใน input field 
weight_input.send_keys("80")

time.sleep(1)

# ระบุ element ของส่วนสูง
height_input = driver.find_element(By.ID, "MainBookAuthor_height")

# กรอกข้อมูลใน input field
height_input.send_keys("175")

time.sleep(1)

# ระบุ element ของเบอร์โทรศัพท์
phone_input = driver.find_element(By.ID, "MainBookAuthor_phone")

# กรอกข้อมูลใน input field
phone_input.send_keys("0808165582")

time.sleep(1)

# ระบุ element ของรหัสผ่าน
password_input = driver.find_element(By.ID, "MainAddpassword")

# กรอกรหัสผ่านใน input field (ในกรณีนี้เราจะใช้ "MyPassword123" เป็นตัวอย่าง)
password_input.send_keys("123456")

time.sleep(1)

# ระบุ element ของชื่อ
contact_first_name_input = driver.find_element(By.ID, "MainBookAuthor_contact_first_name")

# กรอกชื่อใน input field (ในกรณีนี้เราจะใช้ "John" เป็นตัวอย่าง)
contact_first_name_input.send_keys("อลิสรา")

time.sleep(1)

# ระบุ element ของนามสกุล
contact_last_name_input = driver.find_element(By.ID, "MainBookAuthor_contact_last_name")

# กรอกนามสกุลใน input field (ในกรณีนี้เราจะใช้ "Doe" เป็นตัวอย่าง)
contact_last_name_input.send_keys("ขีดแต้ม")

time.sleep(1)

# ระบุ element ของความสัมพันธ์
relation_select = Select(driver.find_element(By.ID, "MainBookAuthor_contact_relation_id"))

# เลือกความสัมพันธ์ 
relation_select.select_by_value("ภรรยา")

time.sleep(1)

# ระบุ element ของเบอร์โทร
phone_input = driver.find_element(By.ID, "MainBookAuthor_contact_phoneNumber")

# กรอกเบอร์โทร
phone_input.send_keys("0944871974")

time.sleep(1)

# ระบุ element ของบ้านเลขที่
address_input = driver.find_element(By.ID, "MainBookAuthor_address")

# กรอกบ้านเลขที่
address_input.send_keys("95")

time.sleep(1)

# ระบุ element ของเลือกจังหวัด
province_select = Select(driver.find_element(By.ID, "MainBookAuthor_province"))

# เลือกจังหวัดนครปฐม
province_select.select_by_visible_text("นครปฐม")

time.sleep(1)

# ระบุ element ของ input อำเภอ
district_input = driver.find_element(By.ID, "MainBookAuthor_district")

# กรอกอำเภอ "กำแพงแสน"
district_input.send_keys("กำแพงแสน")

time.sleep(1)

# ระบุ element ของ input ตำบล
subdistrict_input = driver.find_element(By.ID, "MainBookAuthor_subdistrict")

# กรอกตำบล "ห้วยม่วง"
subdistrict_input.send_keys("ห้วยม่วง")

time.sleep(1)

# ระบุ element ของ input รหัสไปรษณีย์
postcode_input = driver.find_element(By.ID, "MainBookAuthor_postcode")

# กรอกรหัสไปรษณีย์ "73180"
postcode_input.send_keys("73180")

time.sleep(1)

# ระบุ element ของปุ่ม "บันทึก" ด้วย id
save_button = driver.find_element( By.ID, "MainBookAuthor_submit")

# คลิกปุ่ม "บันทึก"
save_button.click()

time.sleep(5)

# ค้นหาปุ่ม "ยืนยัน" โดยใช้ XPath (หรือวิธีการค้นหาที่ถูกต้อง)
confirm_button = driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled']")

# คลิกปุ่ม "ยืนยัน"
confirm_button.click()

time.sleep(5)