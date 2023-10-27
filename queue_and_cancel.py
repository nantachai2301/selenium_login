import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class YourSeleniumTest(unittest.TestCase):
    def setUp(self):
        # ระบุพาธของ ChromeDriver
        self.chrome_driver_path = "C:/Users/jay/chromedriver.exe"

        # เริ่มต้น WebDriver
        self.driver = webdriver.Chrome()
        # ขยายหน้าต่างเบราวเซอร์ให้เต็มหน้าจอ
        self.driver.maximize_window()

        # เปิดเว็บไซต์ของคุณ
        self.driver.get("https://online-web-mauve.vercel.app/")

    def test_run_selenium(self):
        # คลิกปุ่ม "เข้าสู่ระบบ"
        open_modal_button = self.driver.find_element(By.XPATH, "//span[text()='เข้าสู่ระบบ']")
        open_modal_button.click()

        # ระบุ element ของรหัสประจำตัวประชาชนและรหัสผ่านใน Modal
        id_input = self.driver.find_element(By.XPATH, "//label[text()='รหัสประจำตัวประชาชน']/following-sibling::input")
        password_input = self.driver.find_element(By.XPATH, "//label[text()='รหัสผ่าน']/following-sibling::input")

        # กรอกข้อมูลใน input field
        id_input.send_keys("7788888888888")
        password_input.send_keys("123456")

        time.sleep(2)

        # คลิกปุ่ม "เข้าสู่ระบบ" ด้วย XPath
        login_button = self.driver.find_element(By.XPATH, "//button[text()='เข้าสู่ระบบ']")
        login_button.click()

        # รอสักครู่เพื่อให้หน้าเว็บโหลดและดำเนินการต่อ
        time.sleep(5)  # รอ 5 วินาที (หรือตามที่คุณต้องการ)

        # คลิกปุ่ม "จองคิว" โดยใช้ XPath
        booking_button = self.driver.find_element(By.XPATH, "//h4[text()='จองคิว']")
        booking_button.click()

        time.sleep(2)

        # กรอกข้อมูลในฟิลด์ "กรุณาระบุอาการเบื้องต้น"
        symptom_input = self.driver.find_element(By.XPATH, "//input[@name='symptom']")
        symptom_input.send_keys("")

        time.sleep(2)

        # สร้าง Select object จาก element dropdown
        department_dropdown = Select(self.driver.find_element(By.XPATH, "//select[@name='department_id']"))

        # เลือกแผนกที่คุณต้องการ (เช่น "ทันตกรรม")
        department_dropdown.select_by_visible_text("ทันตกรรม")

        time.sleep(2)

        # กรอกข้อมูลในฟิลด์ "วันที่"
        date_input = self.driver.find_element(By.XPATH, "//input[@name='queue_date']")
        date_input.send_keys("12-11-2021")  # แทน "2023-09-10" ด้วยวันที่ที่คุณต้องการ

        time.sleep(2)

        # คลิกปุ่ม "จองคิว" โดยใช้ XPath
        booking_button = self.driver.find_element(By.XPATH, "//button[text()='จองคิว']")
        booking_button.click()

        time.sleep(2)

        # คลิกปุ่ม "ตกลง" โดยใช้ XPath
        confirm_button = self.driver.find_element(By.XPATH, "//button[text()='ยืนยัน']")
        confirm_button.click()

        time.sleep(2)

    def tearDown(self):
        # ปิด WebDriver
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
