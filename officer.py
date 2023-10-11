import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import time

class YourTestCase(unittest.TestCase):
    def setUp(self):
        # ตั้งค่า WebDriver และเปิดเบราวเซอร์เมื่อเริ่มทุกเทส
        self.chrome_driver_path = "C:/Users/jay/chromedriver.exe"
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        # ปิดเบราวเซอร์เมื่อทุกเทสสิ้นสุด
        self.driver.quit()

    def test_login_and_book_queue(self):
        driver = self.driver
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
        time.sleep(3)

        # ค้นหาปุ่ม "จองคิว" โดยใช้ ID
        booking_button = driver.find_element(By.ID, 'BookingWalkinopenModal')

        # คลิกปุ่ม "จองคิว"
        booking_button.click()

        time.sleep(5)

        # ค้นหาฟิลด์ "อาการเบื้องต้น" โดยใช้ ID
        symptom_input = driver.find_element(By.ID, 'BookingWalkinsymptom')

        # กรอกข้อมูลในฟิลด์
        symptom_input.send_keys('ปวดฟัน')
        time.sleep(1)

        # ค้นหาเลือกแผนกโดยใช้ ID
        department_select = Select(driver.find_element(By.ID, 'BookingWalkindepartment_id'))

        # เลือกแผนกที่คุณต้องการ
        department_select.select_by_visible_text('ทันตกรรม')

        time.sleep(1)

        # ค้นหาฟิลด์ "วันที่จะจองคิว" ด้วย ID
        queue_date_input = driver.find_element(By.ID, 'BookingWalkinqueue_date')

        # ลบข้อมูลที่อาจมีอยู่ในฟิลด์ก่อน
        queue_date_input.clear()

        # กรอกวันที่ที่คุณต้องการ (เป็นรูปแบบ 'YYYY-MM-DD')
        desired_date = '01-10-2023'  # เปลี่ยนเป็นวันที่ที่คุณต้องการ
        queue_date_input.send_keys(desired_date)

        # รอสักครู่ให้ข้อมูลถูกป้อนเข้าฟิลด์
        time.sleep(1)

        # คลิกปุ่ม "จองคิว" โดยใช้ ID
        booking_button = driver.find_element(By.ID, 'BookingWalkinBooking')
        booking_button.click()

        # รอสักครู่ให้การกระทำเสร็จสมบูรณ์
        time.sleep(1)

        # คลิกปุ่ม "ตกลง" โดยใช้คลาสและคำอธิบาย class
        confirm_button = driver.find_element(By.CLASS_NAME, 'swal2-confirm')
        confirm_button.click()

        # รอสักครู่ให้การกระทำเสร็จสมบูรณ์
        time.sleep(10)

if __name__ == '__main__':
    unittest.main()
