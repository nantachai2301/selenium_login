from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import unittest
from selenium.webdriver.support.ui import Select

class ManageSymptomTest(unittest.TestCase):

    def setUp(self):
        # Initialize the Chrome WebDriver
        s = Service('D:\webdriver\chromedriver.exe')
        self.driver = webdriver.Chrome(service=s)

    def tearDown(self):
        # Close the browser
        self.driver.quit()

    def test_book_queue_1(self): #จองคิวสำเร็จ
       
       self.driver.get("https://online-web-mauve.vercel.app/")
       time.sleep(5)

            # คลิกปุ่ม "เข้าสู่ระบบ"
       open_modal_button =self.driver.find_element(By.XPATH, "//span[text()='เข้าสู่ระบบ']")
       open_modal_button.click()

         # ระบุ element ของรหัสประจำตัวประชาชนและรหัสผ่านใน Modal
         # ระบุ element ของรหัสประจำตัวประชาชนและรหัสผ่านใน Modal
       id_input = self.driver.find_element(By.XPATH, "//label[text()='รหัสประจำตัวประชาชน']/following-sibling::input")
       password_input = self.driver.find_element(By.XPATH, "//label[text()='รหัสผ่าน']/following-sibling::input")

        # กรอกข้อมูลใน input field
       id_input.send_keys("7788888888888")
       password_input.send_keys("123456")


            # คลิกปุ่ม "เข้าสู่ระบบ" ด้วย XPath
        # คลิกปุ่ม "เข้าสู่ระบบ" ด้วย XPath
       login_button = self.driver.find_element(By.XPATH, "//button[text()='เข้าสู่ระบบ']")
       login_button.click()
        # รอสักครู่เพื่อให้หน้าเว็บโหลดและดำเนินการต่อ
       time.sleep(5)  # รอ 5 วินาที (หรือตามที่คุณต้องการ)
        

       booking_button = self.driver.find_element(By.XPATH, "//h4[text()='จองคิว']")
       booking_button.click()
       time.sleep(4)
            
       symptom_input = self.driver.find_element(By.XPATH, "//input[@name='symptom']")
       symptom_input.send_keys("ปวดพัน")
       time.sleep(2)
                
       department_dropdown = Select(self.driver.find_element(By.XPATH, "//select[@name='department_id']"))
            # เลือกแผนกที่คุณต้องการ (เช่น "ทันตกรรม")
       department_dropdown.select_by_visible_text("ทันตกรรม")
       time.sleep(2)

       date_input = self.driver.find_element(By.XPATH, "//input[@name='queue_date']")
       date_input.send_keys("12-11-2023")  # แทน "2023-09-10" ด้วยวันที่ที่คุณต้องการ
       time.sleep(2)

                # คลิกปุ่ม "จองคิว" โดยใช้ XPath
       booking_button = self.driver.find_element(By.XPATH, "//button[text()='จองคิว']")
       booking_button.click()
       time.sleep(2)

                # คลิกปุ่ม "ตกลง" โดยใช้ XPath
       confirm_button = self.driver.find_element(By.XPATH, "//button[text()='ยืนยัน']")
       confirm_button.click()
       time.sleep(2)

    
    def test_book_queue_2(self): #จองคิวไม่สำเร็จ(ไม่กรอกอาการเบื้องต้น)
       
       self.driver.get("https://online-web-mauve.vercel.app/")
       time.sleep(5)

            # คลิกปุ่ม "เข้าสู่ระบบ"
       open_modal_button =self.driver.find_element(By.XPATH, "//span[text()='เข้าสู่ระบบ']")
       open_modal_button.click()

         # ระบุ element ของรหัสประจำตัวประชาชนและรหัสผ่านใน Modal
         # ระบุ element ของรหัสประจำตัวประชาชนและรหัสผ่านใน Modal
       id_input = self.driver.find_element(By.XPATH, "//label[text()='รหัสประจำตัวประชาชน']/following-sibling::input")
       password_input = self.driver.find_element(By.XPATH, "//label[text()='รหัสผ่าน']/following-sibling::input")

        # กรอกข้อมูลใน input field
       id_input.send_keys("7788888888888")
       password_input.send_keys("123456")


            # คลิกปุ่ม "เข้าสู่ระบบ" ด้วย XPath
        # คลิกปุ่ม "เข้าสู่ระบบ" ด้วย XPath
       login_button = self.driver.find_element(By.XPATH, "//button[text()='เข้าสู่ระบบ']")
       login_button.click()
        # รอสักครู่เพื่อให้หน้าเว็บโหลดและดำเนินการต่อ
       time.sleep(5)  # รอ 5 วินาที (หรือตามที่คุณต้องการ)
        

       booking_button = self.driver.find_element(By.XPATH, "//h4[text()='จองคิว']")
       booking_button.click()
       time.sleep(4)
            
       department_dropdown = Select(self.driver.find_element(By.XPATH, "//select[@name='department_id']"))
            # เลือกแผนกที่คุณต้องการ (เช่น "ทันตกรรม")
       department_dropdown.select_by_visible_text("ทันตกรรม")
       time.sleep(2)

       date_input = self.driver.find_element(By.XPATH, "//input[@name='queue_date']")
       date_input.send_keys("12-11-2023")  # แทน "2023-09-10" ด้วยวันที่ที่คุณต้องการ
       time.sleep(2)

                # คลิกปุ่ม "จองคิว" โดยใช้ XPath
       booking_button = self.driver.find_element(By.XPATH, "//button[text()='จองคิว']")
       booking_button.click()
       time.sleep(2)
    
    
    def test_book_queue_3(self): #จองคิวไม่สำเร็จ(วันที่ย้อนหลัง)
       
       self.driver.get("https://online-web-mauve.vercel.app/")
       time.sleep(5)

            # คลิกปุ่ม "เข้าสู่ระบบ"
       open_modal_button =self.driver.find_element(By.XPATH, "//span[text()='เข้าสู่ระบบ']")
       open_modal_button.click()

         # ระบุ element ของรหัสประจำตัวประชาชนและรหัสผ่านใน Modal
         # ระบุ element ของรหัสประจำตัวประชาชนและรหัสผ่านใน Modal
       id_input = self.driver.find_element(By.XPATH, "//label[text()='รหัสประจำตัวประชาชน']/following-sibling::input")
       password_input = self.driver.find_element(By.XPATH, "//label[text()='รหัสผ่าน']/following-sibling::input")

        # กรอกข้อมูลใน input field
       id_input.send_keys("7788888888888")
       password_input.send_keys("123456")


            # คลิกปุ่ม "เข้าสู่ระบบ" ด้วย XPath
        # คลิกปุ่ม "เข้าสู่ระบบ" ด้วย XPath
       login_button = self.driver.find_element(By.XPATH, "//button[text()='เข้าสู่ระบบ']")
       login_button.click()
        # รอสักครู่เพื่อให้หน้าเว็บโหลดและดำเนินการต่อ
       time.sleep(5)  # รอ 5 วินาที (หรือตามที่คุณต้องการ)
        

       booking_button = self.driver.find_element(By.XPATH, "//h4[text()='จองคิว']")
       booking_button.click()
       time.sleep(4)
            
       symptom_input = self.driver.find_element(By.XPATH, "//input[@name='symptom']")
       symptom_input.send_keys("ปวดพัน")
       time.sleep(2)
                
       department_dropdown = Select(self.driver.find_element(By.XPATH, "//select[@name='department_id']"))
            # เลือกแผนกที่คุณต้องการ (เช่น "ทันตกรรม")
       department_dropdown.select_by_visible_text("ทันตกรรม")
       time.sleep(2)

       date_input = self.driver.find_element(By.XPATH, "//input[@name='queue_date']")
       date_input.send_keys("9-14-2023")  # แทน "2023-09-10" ด้วยวันที่ที่คุณต้องการ
       time.sleep(2)

                # คลิกปุ่ม "จองคิว" โดยใช้ XPath
       booking_button = self.driver.find_element(By.XPATH, "//button[text()='จองคิว']")
       booking_button.click()
       time.sleep(4)
   
    
    def test_book_queue_4(self): #ลงทะเบียนสำเร็จ
        
        self.driver.get("https://online-web-mauve.vercel.app/")
        time.sleep(5)
       
      # คลิกปุ่ม "เข้าสู่ระบบ"
        open_modal_button =self.driver.find_element(By.XPATH, "//span[text()='เข้าสู่ระบบ']")
        open_modal_button.click()

        # ระบุ element ของรหัสประจำตัวประชาชนและรหัสผ่านใน Modal
        id_input = self.driver.find_element(By.XPATH, "//label[text()='รหัสประจำตัวประชาชน']/following-sibling::input")
        password_input = self.driver.find_element(By.XPATH, "//label[text()='รหัสผ่าน']/following-sibling::input")

        # กรอกข้อมูลใน input field
        id_input.send_keys("7777777777777")
        password_input.send_keys("123456")

        # คลิกปุ่ม "เข้าสู่ระบบ" ด้วย XPath
        login_button = self.driver.find_element(By.XPATH, "//button[text()='เข้าสู่ระบบ']")
        login_button.click()
        # รอสักครู่เพื่อให้หน้าเว็บโหลดและดำเนินการต่อ
        time.sleep(5)  # รอ 5 วินาที (หรือตามที่คุณต้องการ)
        
        link_element = self.driver.find_element(By.XPATH, '//div[contains(text(), "จองคิวผู้ป่วย Walk in")]')
        
        link_element.click()
        time.sleep(2)

        # คลิกปุ่ม "เพิ่มผู้ป่วย Walk In" โดยใช้ ID
        add_patient_button = self.driver.find_element(By.ID, "BookingWalkinAddbook-an-appointment")
        add_patient_button.click()

        time.sleep(2)

        # ระบุ element ของฟิลด์เลขบัตรประชาชน
        id_card_input = self.driver.find_element(By.ID, "MainBookAuthor_id_card")

        # กรอกเลขบัตรประชาชนในฟิลด์
        id_card_input.send_keys("1749800297083")  # แทน "1234567890123" ด้วยเลขบัตรประชาชนที่คุณต้องการ

        time.sleep(1)

        # ระบุ element ของ dropdown
        prefix_name_dropdown = Select(self.driver.find_element(By.ID, "MainBookAuthor_prefix_name"))

        # เลือกคำนำหน้าที่คุณต้องการ (เช่น "นาย")
        prefix_name_dropdown.select_by_value("นาย")  # หรือจะใช้ .select_by_visible_text("นาย") ก็ได้

        time.sleep(1)

        # ระบุ element ของช่องข้อมูลชื่อ
        first_name_input = self.driver.find_element(By.ID, "MainBookAuthor_first_name")

        # กรอกชื่อที่คุณต้องการ
        first_name_input.send_keys("นันทชัย")

        time.sleep(1)

        # ระบุ element ของช่องข้อมูลนามสกุล
        last_name_input = self.driver.find_element(By.ID, "MainBookAuthor_last_name")

        # กรอกนามสกุลที่คุณต้องการ
        last_name_input.send_keys("แสงอรุณ")

        time.sleep(1)

        # ระบุ element ของเพศ
        gender_dropdown = Select(self.driver.find_element(By.ID, "MainBookAuthor_gender"))

        # เลือกเพศที่คุณต้องการ (เช่น "ชาย")
        gender_dropdown.select_by_value("ชาย")

        time.sleep(1)

        # ระบุ element ของวันเดือนปีเกิด
        birthday_input = self.driver.find_element(By.ID, "MainBookAuthor_birthday")

        # กรอกข้อมูลใน input field (ในกรณีนี้เราจะใช้ "1990-01-01" เป็นตัวอย่าง)
        birthday_input.send_keys("01-23-2002")

        time.sleep(1)

        # ระบุ element ของน้ำหนัก
        weight_input = self.driver.find_element(By.ID, "MainBookAuthor_weight")

        # กรอกข้อมูลใน input field
        weight_input.send_keys("80")

        time.sleep(1)

        # ระบุ element ของส่วนสูง
        height_input = self.driver.find_element(By.ID, "MainBookAuthor_height")

        # กรอกข้อมูลใน input field
        height_input.send_keys("175")

        time.sleep(1)

        # ระบุ element ของเบอร์โทรศัพท์
        phone_input = self.driver.find_element(By.ID, "MainBookAuthor_phone")

        # กรอกข้อมูลใน input field
        phone_input.send_keys("0808165582")

        time.sleep(1)

        # ระบุ element ของรหัสผ่าน
        password_input = self.driver.find_element(By.ID, "MainAddpassword")

        # กรอกรหัสผ่านใน input field (ในกรณีนี้เราจะใช้ "123456" เป็นตัวอย่าง)
        password_input.send_keys("123456")

        time.sleep(1)

        # ระบุ element ของชื่อ
        contact_first_name_input = self.driver.find_element(By.ID, "MainBookAuthor_contact_first_name")

        # กรอกชื่อใน input field (ในกรณีนี้เราจะใช้ "อลิสรา" เป็นตัวอย่าง)
        contact_first_name_input.send_keys("อลิสรา")

        time.sleep(1)

        # ระบุ element ของนามสกุล
        contact_last_name_input = self.driver.find_element(By.ID, "MainBookAuthor_contact_last_name")

        # กรอกนามสกุลใน input field (ในกรณีนี้เราจะใช้ "ขีดแต้ม" เป็นตัวอย่าง)
        contact_last_name_input.send_keys("ขีดแต้ม")

        time.sleep(1)

        # ระบุ element ของความสัมพันธ์
        relation_select = Select(self.driver.find_element(By.ID, "MainBookAuthor_contact_relation_id"))

        # เลือกความสัมพันธ์
        relation_select.select_by_value("ภรรยา")

        time.sleep(1)

        # ระบุ element ของเบอร์โทร
        phone_input = self.driver.find_element(By.ID, "MainBookAuthor_contact_phoneNumber")

        # กรอกเบอร์โทร
        phone_input.send_keys("0944871974")

        time.sleep(1)

        # ระบุ element ของบ้านเลขที่
        address_input = self.driver.find_element(By.ID, "MainBookAuthor_address")

        # กรอกบ้านเลขที่
        address_input.send_keys("95")

        time.sleep(1)

        # ระบุ element ของเลือกจังหวัด
        province_select = Select(self.driver.find_element(By.ID, "MainBookAuthor_province"))

        # เลือกจังหวัดนครปฐม
        province_select.select_by_visible_text("นครปฐม")

        time.sleep(1)

        # ระบุ element ของ input อำเภอ
        district_input = self.driver.find_element(By.ID, "MainBookAuthor_district")

        # กรอกอำเภอ "กำแพงแสน"
        district_input.send_keys("กำแพงแสน")

        time.sleep(1)

        # ระบุ element ของ input ตำบล
        subdistrict_input = self.driver.find_element(By.ID, "MainBookAuthor_subdistrict")

        # กรอกตำบล "ห้วยม่วง"
        subdistrict_input.send_keys("ห้วยม่วง")

        time.sleep(1)

        # ระบุ element ของ input รหัสไปรษณีย์
        postcode_input = self.driver.find_element(By.ID, "MainBookAuthor_postcode")

        # กรอกรหัสไปรษณีย์ "73180"
        postcode_input.send_keys("73180")

        time.sleep(1)
         # เลื่อนหน้าเว็บมายัง Element 'New'
        new_element = self.driver.find_element(By.ID, "MainBookAuthor_submit")
        self.driver.execute_script("arguments[0].scrollIntoView();", new_element)
        time.sleep(2)  # รอสักครู่ให้หน้าเว็บเลื่อนมา
        # ระบุ element ของปุ่ม "บันทึก" ด้วย id
        save_button = self.driver.find_element(By.ID, "MainBookAuthor_submit")

        # คลิกปุ่ม "บันทึก"
        save_button.click()

        time.sleep(5)

        # ค้นหาปุ่ม "ยืนยัน" โดยใช้ XPath (หรือวิธีการค้นหาที่ถูกต้อง)
        confirm_button = self.driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled']")

        # คลิกปุ่ม "ยืนยัน"
        confirm_button.click()

        time.sleep(5)

    def test_book_queue_5(self): #ลงทะเบียนไม่สำเร็จ(ไม่กรอกบัตรประชาชน)
        
        self.driver.get("https://online-web-mauve.vercel.app/")
        time.sleep(5)
       
      # คลิกปุ่ม "เข้าสู่ระบบ"
        open_modal_button =self.driver.find_element(By.XPATH, "//span[text()='เข้าสู่ระบบ']")
        open_modal_button.click()

        # ระบุ element ของรหัสประจำตัวประชาชนและรหัสผ่านใน Modal
        id_input = self.driver.find_element(By.XPATH, "//label[text()='รหัสประจำตัวประชาชน']/following-sibling::input")
        password_input = self.driver.find_element(By.XPATH, "//label[text()='รหัสผ่าน']/following-sibling::input")

        # กรอกข้อมูลใน input field
        id_input.send_keys("7777777777777")
        password_input.send_keys("123456")

        # คลิกปุ่ม "เข้าสู่ระบบ" ด้วย XPath
        login_button = self.driver.find_element(By.XPATH, "//button[text()='เข้าสู่ระบบ']")
        login_button.click()
        # รอสักครู่เพื่อให้หน้าเว็บโหลดและดำเนินการต่อ
        time.sleep(5)  # รอ 5 วินาที (หรือตามที่คุณต้องการ)
        
        link_element = self.driver.find_element(By.XPATH, '//div[contains(text(), "จองคิวผู้ป่วย Walk in")]')
        
        link_element.click()
        time.sleep(2)

        # คลิกปุ่ม "เพิ่มผู้ป่วย Walk In" โดยใช้ ID
        add_patient_button = self.driver.find_element(By.ID, "BookingWalkinAddbook-an-appointment")
        add_patient_button.click()

        time.sleep(2)

        # ระบุ element ของฟิลด์เลขบัตรประชาชน
        id_card_input = self.driver.find_element(By.ID, "MainBookAuthor_id_card")

        # กรอกเลขบัตรประชาชนในฟิลด์
        id_card_input.send_keys("")  # แทน "1234567890123" ด้วยเลขบัตรประชาชนที่คุณต้องการ

        time.sleep(1)

        # ระบุ element ของ dropdown
        prefix_name_dropdown = Select(self.driver.find_element(By.ID, "MainBookAuthor_prefix_name"))

        # เลือกคำนำหน้าที่คุณต้องการ (เช่น "นาย")
        prefix_name_dropdown.select_by_value("นาย")  # หรือจะใช้ .select_by_visible_text("นาย") ก็ได้

        time.sleep(1)

        # ระบุ element ของช่องข้อมูลชื่อ
        first_name_input = self.driver.find_element(By.ID, "MainBookAuthor_first_name")

        # กรอกชื่อที่คุณต้องการ
        first_name_input.send_keys("นันทชัย")

        time.sleep(1)

        # ระบุ element ของช่องข้อมูลนามสกุล
        last_name_input = self.driver.find_element(By.ID, "MainBookAuthor_last_name")

        # กรอกนามสกุลที่คุณต้องการ
        last_name_input.send_keys("แสงอรุณ")

        time.sleep(1)

        # ระบุ element ของเพศ
        gender_dropdown = Select(self.driver.find_element(By.ID, "MainBookAuthor_gender"))

        # เลือกเพศที่คุณต้องการ (เช่น "ชาย")
        gender_dropdown.select_by_value("ชาย")

        time.sleep(1)

        # ระบุ element ของวันเดือนปีเกิด
        birthday_input = self.driver.find_element(By.ID, "MainBookAuthor_birthday")

        # กรอกข้อมูลใน input field (ในกรณีนี้เราจะใช้ "1990-01-01" เป็นตัวอย่าง)
        birthday_input.send_keys("01-23-2002")

        time.sleep(1)

        # ระบุ element ของน้ำหนัก
        weight_input = self.driver.find_element(By.ID, "MainBookAuthor_weight")

        # กรอกข้อมูลใน input field
        weight_input.send_keys("80")

        time.sleep(1)

        # ระบุ element ของส่วนสูง
        height_input = self.driver.find_element(By.ID, "MainBookAuthor_height")

        # กรอกข้อมูลใน input field
        height_input.send_keys("175")

        time.sleep(1)

        # ระบุ element ของเบอร์โทรศัพท์
        phone_input = self.driver.find_element(By.ID, "MainBookAuthor_phone")

        # กรอกข้อมูลใน input field
        phone_input.send_keys("0808165582")

        time.sleep(1)

        # ระบุ element ของรหัสผ่าน
        password_input = self.driver.find_element(By.ID, "MainAddpassword")

        # กรอกรหัสผ่านใน input field (ในกรณีนี้เราจะใช้ "123456" เป็นตัวอย่าง)
        password_input.send_keys("123456")

        time.sleep(1)

        # ระบุ element ของชื่อ
        contact_first_name_input = self.driver.find_element(By.ID, "MainBookAuthor_contact_first_name")

        # กรอกชื่อใน input field (ในกรณีนี้เราจะใช้ "อลิสรา" เป็นตัวอย่าง)
        contact_first_name_input.send_keys("อลิสรา")

        time.sleep(1)

        # ระบุ element ของนามสกุล
        contact_last_name_input = self.driver.find_element(By.ID, "MainBookAuthor_contact_last_name")

        # กรอกนามสกุลใน input field (ในกรณีนี้เราจะใช้ "ขีดแต้ม" เป็นตัวอย่าง)
        contact_last_name_input.send_keys("ขีดแต้ม")

        time.sleep(1)

        # ระบุ element ของความสัมพันธ์
        relation_select = Select(self.driver.find_element(By.ID, "MainBookAuthor_contact_relation_id"))

        # เลือกความสัมพันธ์
        relation_select.select_by_value("ภรรยา")

        time.sleep(1)

        # ระบุ element ของเบอร์โทร
        phone_input = self.driver.find_element(By.ID, "MainBookAuthor_contact_phoneNumber")

        # กรอกเบอร์โทร
        phone_input.send_keys("0944871974")

        time.sleep(1)

        # ระบุ element ของบ้านเลขที่
        address_input = self.driver.find_element(By.ID, "MainBookAuthor_address")

        # กรอกบ้านเลขที่
        address_input.send_keys("95")

        time.sleep(1)

        # ระบุ element ของเลือกจังหวัด
        province_select = Select(self.driver.find_element(By.ID, "MainBookAuthor_province"))

        # เลือกจังหวัดนครปฐม
        province_select.select_by_visible_text("นครปฐม")

        time.sleep(1)

        # ระบุ element ของ input อำเภอ
        district_input = self.driver.find_element(By.ID, "MainBookAuthor_district")

        # กรอกอำเภอ "กำแพงแสน"
        district_input.send_keys("กำแพงแสน")

        time.sleep(1)

        # ระบุ element ของ input ตำบล
        subdistrict_input = self.driver.find_element(By.ID, "MainBookAuthor_subdistrict")

        # กรอกตำบล "ห้วยม่วง"
        subdistrict_input.send_keys("ห้วยม่วง")

        time.sleep(1)

        # ระบุ element ของ input รหัสไปรษณีย์
        postcode_input = self.driver.find_element(By.ID, "MainBookAuthor_postcode")

        # กรอกรหัสไปรษณีย์ "73180"
        postcode_input.send_keys("73180")

        time.sleep(1)
         # เลื่อนหน้าเว็บมายัง Element 'New'
        new_element = self.driver.find_element(By.ID, "MainBookAuthor_submit")
        self.driver.execute_script("arguments[0].scrollIntoView();", new_element)
        time.sleep(2)  # รอสักครู่ให้หน้าเว็บเลื่อนมา
        # ระบุ element ของปุ่ม "บันทึก" ด้วย id
        save_button = self.driver.find_element(By.ID, "MainBookAuthor_submit")

        # คลิกปุ่ม "บันทึก"
        save_button.click()

        time.sleep(5)

        # ค้นหาปุ่ม "ยืนยัน" โดยใช้ XPath (หรือวิธีการค้นหาที่ถูกต้อง)
        confirm_button = self.driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled']")

        # คลิกปุ่ม "ยืนยัน"
        confirm_button.click()

        time.sleep(5)  

    def test_book_queue_6(self):#ลงทะเบียนไม่สำเร็จ(ไม่กรอกอะไรเลย)
        
        self.driver.get("https://online-web-mauve.vercel.app/")
        time.sleep(5)
       
      # คลิกปุ่ม "เข้าสู่ระบบ"
        open_modal_button =self.driver.find_element(By.XPATH, "//span[text()='เข้าสู่ระบบ']")
        open_modal_button.click()

        # ระบุ element ของรหัสประจำตัวประชาชนและรหัสผ่านใน Modal
        id_input = self.driver.find_element(By.XPATH, "//label[text()='รหัสประจำตัวประชาชน']/following-sibling::input")
        password_input = self.driver.find_element(By.XPATH, "//label[text()='รหัสผ่าน']/following-sibling::input")

        # กรอกข้อมูลใน input field
        id_input.send_keys("7777777777777")
        password_input.send_keys("123456")

        # คลิกปุ่ม "เข้าสู่ระบบ" ด้วย XPath
        login_button = self.driver.find_element(By.XPATH, "//button[text()='เข้าสู่ระบบ']")
        login_button.click()
        # รอสักครู่เพื่อให้หน้าเว็บโหลดและดำเนินการต่อ
        time.sleep(5)  # รอ 5 วินาที (หรือตามที่คุณต้องการ)
        
        link_element = self.driver.find_element(By.XPATH, '//div[contains(text(), "จองคิวผู้ป่วย Walk in")]')
        
        link_element.click()
        time.sleep(2)

        # คลิกปุ่ม "เพิ่มผู้ป่วย Walk In" โดยใช้ ID
        add_patient_button = self.driver.find_element(By.ID, "BookingWalkinAddbook-an-appointment")
        add_patient_button.click()

        time.sleep(2)

       
        new_element = self.driver.find_element(By.ID, "MainBookAuthor_submit")
        self.driver.execute_script("arguments[0].scrollIntoView();", new_element)
        time.sleep(2)  # รอสักครู่ให้หน้าเว็บเลื่อนมา
        # ระบุ element ของปุ่ม "บันทึก" ด้วย id
        save_button = self.driver.find_element(By.ID, "MainBookAuthor_submit")

        # คลิกปุ่ม "บันทึก"
        save_button.click()
        time.sleep(5)
    
    def test_book_queue_7(self): #จองคิวสำเร็จ
       
        self.driver.get("https://online-web-mauve.vercel.app/")

        # คลิกปุ่ม "เข้าสู่ระบบ"
        open_modal_button =self.driver.find_element(By.XPATH, "//span[text()='เข้าสู่ระบบ']")
        open_modal_button.click()

        # ระบุ element ของรหัสประจำตัวประชาชนและรหัสผ่านใน Modal
        id_input = self.driver.find_element(By.XPATH, "//label[text()='รหัสประจำตัวประชาชน']/following-sibling::input")
        password_input = self.driver.find_element(By.XPATH, "//label[text()='รหัสผ่าน']/following-sibling::input")

        # กรอกข้อมูลใน input field
        id_input.send_keys("7777777777777")
        password_input.send_keys("123456")

        # คลิกปุ่ม "เข้าสู่ระบบ" ด้วย XPath
        login_button = self.driver.find_element(By.XPATH, "//button[text()='เข้าสู่ระบบ']")
        login_button.click()

        # รอสักครู่เพื่อให้หน้าเว็บโหลดและดำเนินการต่อ
        time.sleep(5)  # รอ 5 วินาที (หรือตามที่คุณต้องการ)

        link_element = self.driver.find_element(By.XPATH, '//div[contains(text(), "จองคิวผู้ป่วย Walk in")]')
        self.driver.execute_script("arguments[0].click();", link_element)
        time.sleep(3)
        
       
          # Click the date input field (คลิกที่ input ประเภทวันที่)
        date_input = self.driver.find_element(By.ID, "BookingWalkinSearch")

        # Set the date to your desired date (ตั้งค่าวันที่ตามที่คุณต้องการ)
        date_input.clear()
        date_input.send_keys("1749800297083")  
        # รอ 5 วินาที (หรือตามที่คุณต้องการ)
        time.sleep(4) 
        # ค้นหาปุ่ม "จองคิว" โดยใช้ ID
        booking_button = self.driver.find_element(By.ID, 'BookingWalkinopenModal')

        # คลิกปุ่ม "จองคิว"
        booking_button.click()

        time.sleep(5)

        # ค้นหาฟิลด์ "อาการเบื้องต้น" โดยใช้ ID
        symptom_input = self.driver.find_element(By.ID, 'BookingWalkinsymptom')

        # กรอกข้อมูลในฟิลด์
        symptom_input.send_keys('ปวดฟัน')
        time.sleep(1)

        # ค้นหาเลือกแผนกโดยใช้ ID
        department_select = Select(self.driver.find_element(By.ID, 'BookingWalkindepartment_id'))

        # เลือกแผนกที่คุณต้องการ
        department_select.select_by_visible_text('ทันตกรรม')

        time.sleep(1)

        # ค้นหาฟิลด์ "วันที่จะจองคิว" ด้วย ID
        queue_date_input = self.driver.find_element(By.ID, 'BookingWalkinqueue_date')

        # ลบข้อมูลที่อาจมีอยู่ในฟิลด์ก่อน
        queue_date_input.clear()

        # กรอกวันที่ที่คุณต้องการ (เป็นรูปแบบ 'YYYY-MM-DD')
        desired_date = '10-25-2023'  # เปลี่ยนเป็นวันที่ที่คุณต้องการ
        queue_date_input.send_keys(desired_date)

        # รอสักครู่ให้ข้อมูลถูกป้อนเข้าฟิลด์
        time.sleep(1)

        # คลิกปุ่ม "จองคิว" โดยใช้ ID
        booking_button = self.driver.find_element(By.ID, 'BookingWalkinBooking')
        booking_button.click()

        # รอสักครู่ให้การกระทำเสร็จสมบูรณ์
        time.sleep(1)

        # คลิกปุ่ม "ตกลง" โดยใช้คลาสและคำอธิบาย class
        confirm_button = self.driver.find_element(By.CLASS_NAME, 'swal2-confirm')
        confirm_button.click()

        # รอสักครู่ให้การกระทำเสร็จสมบูรณ์
        time.sleep(10)
   
    def test_book_queue_8(self):#จองคิวไม่สำเร็จ(ไม่กรอกอะไรเลย)
       
            self.driver.get("https://online-web-mauve.vercel.app/")

            # คลิกปุ่ม "เข้าสู่ระบบ"
            open_modal_button =self.driver.find_element(By.XPATH, "//span[text()='เข้าสู่ระบบ']")
            open_modal_button.click()

            # ระบุ element ของรหัสประจำตัวประชาชนและรหัสผ่านใน Modal
            id_input = self.driver.find_element(By.XPATH, "//label[text()='รหัสประจำตัวประชาชน']/following-sibling::input")
            password_input = self.driver.find_element(By.XPATH, "//label[text()='รหัสผ่าน']/following-sibling::input")

            # กรอกข้อมูลใน input field
            id_input.send_keys("7777777777777")
            password_input.send_keys("123456")

            # คลิกปุ่ม "เข้าสู่ระบบ" ด้วย XPath
            login_button = self.driver.find_element(By.XPATH, "//button[text()='เข้าสู่ระบบ']")
            login_button.click()

            # รอสักครู่เพื่อให้หน้าเว็บโหลดและดำเนินการต่อ
            time.sleep(5)  # รอ 5 วินาที (หรือตามที่คุณต้องการ)

            link_element = self.driver.find_element(By.XPATH, '//div[contains(text(), "จองคิวผู้ป่วย Walk in")]')
            self.driver.execute_script("arguments[0].click();", link_element)
            time.sleep(3)
            
        
            # Click the date input field (คลิกที่ input ประเภทวันที่)
            date_input = self.driver.find_element(By.ID, "BookingWalkinSearch")

            # Set the date to your desired date (ตั้งค่าวันที่ตามที่คุณต้องการ)
            date_input.clear()
            date_input.send_keys("1749800297083")  
            # รอ 5 วินาที (หรือตามที่คุณต้องการ)
            time.sleep(4) 
            # ค้นหาปุ่ม "จองคิว" โดยใช้ ID
            booking_button = self.driver.find_element(By.ID, 'BookingWalkinopenModal')

            # คลิกปุ่ม "จองคิว"
            booking_button.click()

            time.sleep(5)
           # คลิกปุ่ม "จองคิว" โดยใช้ ID
            booking_button = self.driver.find_element(By.ID, 'BookingWalkinBooking')
            booking_button.click()

            # รอสักครู่ให้การกระทำเสร็จสมบูรณ์
            time.sleep(5)

    def test_book_queue_9(self):#จองคิวไม่สำเร็จ(กรอกวันย้อนหลัง)
       
            self.driver.get("https://online-web-mauve.vercel.app/")

            # คลิกปุ่ม "เข้าสู่ระบบ"
            open_modal_button =self.driver.find_element(By.XPATH, "//span[text()='เข้าสู่ระบบ']")
            open_modal_button.click()

            # ระบุ element ของรหัสประจำตัวประชาชนและรหัสผ่านใน Modal
            id_input = self.driver.find_element(By.XPATH, "//label[text()='รหัสประจำตัวประชาชน']/following-sibling::input")
            password_input = self.driver.find_element(By.XPATH, "//label[text()='รหัสผ่าน']/following-sibling::input")

            # กรอกข้อมูลใน input field
            id_input.send_keys("7777777777777")
            password_input.send_keys("123456")

            # คลิกปุ่ม "เข้าสู่ระบบ" ด้วย XPath
            login_button = self.driver.find_element(By.XPATH, "//button[text()='เข้าสู่ระบบ']")
            login_button.click()

            # รอสักครู่เพื่อให้หน้าเว็บโหลดและดำเนินการต่อ
            time.sleep(5)  # รอ 5 วินาที (หรือตามที่คุณต้องการ)

            link_element = self.driver.find_element(By.XPATH, '//div[contains(text(), "จองคิวผู้ป่วย Walk in")]')
            self.driver.execute_script("arguments[0].click();", link_element)
            time.sleep(3)
            
        
            # Click the date input field (คลิกที่ input ประเภทวันที่)
            date_input = self.driver.find_element(By.ID, "BookingWalkinSearch")

            # Set the date to your desired date (ตั้งค่าวันที่ตามที่คุณต้องการ)
            date_input.clear()
            date_input.send_keys("1749800297083")  
            # รอ 5 วินาที (หรือตามที่คุณต้องการ)
            time.sleep(4) 
            # ค้นหาปุ่ม "จองคิว" โดยใช้ ID
            booking_button = self.driver.find_element(By.ID, 'BookingWalkinopenModal')

            # คลิกปุ่ม "จองคิว"
            booking_button.click()

            time.sleep(5)

             # ค้นหาฟิลด์ "อาการเบื้องต้น" โดยใช้ ID
            symptom_input = self.driver.find_element(By.ID, 'BookingWalkinsymptom')

        # กรอกข้อมูลในฟิลด์
            symptom_input.send_keys('ปวดฟัน')
            time.sleep(1)
            

            # ค้นหาเลือกแผนกโดยใช้ ID
            department_select = Select(self.driver.find_element(By.ID, 'BookingWalkindepartment_id'))

            # เลือกแผนกที่คุณต้องการ
            department_select.select_by_visible_text('ทันตกรรม')

            time.sleep(1)

            # ค้นหาฟิลด์ "วันที่จะจองคิว" ด้วย ID
            queue_date_input = self.driver.find_element(By.ID, 'BookingWalkinqueue_date')

            # ลบข้อมูลที่อาจมีอยู่ในฟิลด์ก่อน
            queue_date_input.clear()

            # กรอกวันที่ที่คุณต้องการ (เป็นรูปแบบ 'YYYY-MM-DD')
            desired_date = '8-29-2023'  # เปลี่ยนเป็นวันที่ที่คุณต้องการ
            queue_date_input.send_keys(desired_date)

            # รอสักครู่ให้ข้อมูลถูกป้อนเข้าฟิลด์
            time.sleep(1)

            # คลิกปุ่ม "จองคิว" โดยใช้ ID
            booking_button = self.driver.find_element(By.ID, 'BookingWalkinBooking')
            booking_button.click()

            # รอสักครู่ให้การกระทำเสร็จสมบูรณ์
            time.sleep(3)


             # คลิกปุ่ม "ตกลง" โดยใช้คลาสและคำอธิบาย class
            confirm_button = self.driver.find_element(By.CLASS_NAME, 'swal2-confirm')
            confirm_button.click()

            # รอสักครู่ให้การกระทำเสร็จสมบูรณ์
            time.sleep(5)
        
if __name__ == "__main__":
 unittest.main()