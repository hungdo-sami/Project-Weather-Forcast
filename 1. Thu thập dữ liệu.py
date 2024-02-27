from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Khởi tạo trình duyệt
driver = webdriver.Chrome()

# Mở trang web
driver.get("https://power.larc.nasa.gov/data-access-viewer/")
time.sleep(10)

#Tat trang thong tin
access_data = driver.find_element(By.XPATH, '//div[@style="margin-bottom: 25px" and contains(@class, "jimu-btn") and contains(@class, "enable-btn")]')
access_data.click()
time.sleep(5)
#Chọn thẻ trang chọn theo khu vực
choose_type = driver.find_element(By.CSS_SELECTOR, ".icon-item.icon-item-background1.dockable")
choose_type.click()
time.sleep(3)
# Tìm phần tử <input> bằng ID
date_input = driver.find_element(By.ID, "datepickerstartr")

# Xóa dữ liệu hiện tại trong trường <input>
date_input.clear()

# Gửi ngày vào trường <input>
date_input.send_keys("01/01/2000")  

# Hoặc sử dụng phím Enter để hoàn thành việc nhập liệu
date_input.send_keys(Keys.RETURN)
######################################################
# Tìm phần tử <input> bằng ID
date_out = driver.find_element(By.ID, "datepickerendr")

# Xóa dữ liệu hiện tại trong trường <input>
date_out.clear()

# Gửi ngày vào trường <input>
date_out.send_keys("12/31/2000")  # Thay "10/12/2023" bằng ngày bạn muốn

# Hoặc sử dụng phím Enter để hoàn thành việc nhập liệu
date_out.send_keys(Keys.RETURN)

#Tat
sut = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div[19]/div[1]/div[2]")
sut.click()
time.sleep(0.5)
#Chọn thẻ Agoclimato
wait = WebDriverWait(driver, 10)
select_element = wait.until(EC.presence_of_element_located((By.ID, 'usercommunityr')))

select = Select(select_element)
select.select_by_value("ag")
# Sử dụng XPath để tìm đối tượng
lat_bot = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[19]/div[2]/div/div/div[1]/table[3]/tbody/tr[1]/td[2]/input")

# Click vào đối tượng
lat_bot.click()

# Gửi giá trị "18.0060" vào đối tượng
lat_bot.send_keys("18.0060")

######################################
# Sử dụng XPath để tìm đối tượng
long_bot = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[19]/div[2]/div/div/div[1]/table[3]/tbody/tr[2]/td[2]/input")

# Click vào đối tượng
long_bot.click()

# Gửi giá trị "103.177" vào đối tượng
long_bot.send_keys("103.177")
#######################################
# Sử dụng XPath để tìm đối tượng
lat_up = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[19]/div[2]/div/div/div[1]/table[3]/tbody/tr[3]/td[2]/input")

# Click vào đối tượng
lat_up.click()

# Gửi giá trị "20.3561" vào đối tượng
lat_up.send_keys("20.3561")
######################################
# Sử dụng XPath để tìm đối tượng
long_up = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[19]/div[2]/div/div/div[1]/table[3]/tbody/tr[4]/td[2]/input")

# Click vào đối tượng
long_up.click()

# Gửi giá trị "107.154" vào đối tượng
long_up.send_keys("107.154")
#Chọn định dạng file
wait = WebDriverWait(driver, 10)
format_output = wait.until(EC.presence_of_element_located((By.ID, 'regional_format')))

select = Select(format_output)
select.select_by_value("CSV")
#Chọn thuộc tính lần 1
step1 = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div[19]/div[2]/div/div/div[1]/div[3]/ul/li[1]/a")
step1.click()
time.sleep(2)
#Chọn thuộc tính lần 2
step2 = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div[19]/div[2]/div/div/div[1]/div[3]/ul/li[2]/a")
step2.click()
time.sleep(2)
#Chọn thuộc tính lần 3
step3 = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div[19]/div[2]/div/div/div[1]/div[3]/ul/li[3]/a")
step3.click()
time.sleep(2)
#Submit
submit = driver.find_element(By.XPATH,"/html/body/div                       [2]/div[2]/div[1]/div[19]/div[2]/div/div/div[1]/table[4]/tbody/tr/td[1]/div")
submit.click()
time.sleep(30)
#Download file
data = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div[19]/div[2]/div/div/div[2]/div[2]/a[4]")
data.click()
time.sleep(3)
#Back
back = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div[19]/div[2]/div/div/div[2]/div[4]")
back.click()
time.sleep(3)
#Chọn thuộc tính lần 1
step1 = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div[19]/div[2]/div/div/div[1]/div[3]/ul/li[1]/a")
step1.click()
time.sleep(2)
#Chọn thuộc tính lần 2
step2 = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div[19]/div[2]/div/div/div[1]/div[3]/ul/li[2]/a")
step2.click()
time.sleep(2)
#Chọn thuộc tính lần 3
step3 = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div[19]/div[2]/div/div/div[1]/div[3]/ul/li[3]/a")
step3.click()
time.sleep(2)
#Chọn thuộc tính lần 4
step2 = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div[19]/div[2]/div/div/div[1]/div[3]/ul/li[4]/a")
step2.click()
time.sleep(2)
#Chọn thuộc tính lần 5
step3 = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div[19]/div[2]/div/div/div[1]/div[3]/ul/li[5]/a")
step3.click()
time.sleep(2)
#Submit
submit = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div[19]/div[2]/div/div/div[1]/table[4]/tbody/tr/td[1]/div")
submit.click()
time.sleep(30)
#Download file
data = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div[19]/div[2]/div/div/div[2]/div[2]/a[4]")
data.click()
time.sleep(3)
#Back
back = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div[19]/div[2]/div/div/div[2]/div[4]")
back.click()
time.sleep(3)


def perform_data_extraction(start_year, end_year):

    while start_year <= end_year:
      # Tìm phần tử <input> bằng ID
        date_input = driver.find_element(By.ID, "datepickerstartr")

        # Xóa dữ liệu hiện tại trong trường <input>
        date_input.clear()

        # Gửi ngày bạn muốn vào trường <input>
        date_input.send_keys(f"01/01/{start_year}")  # Thay "10/12/2023" bằng ngày bạn muốn

        # Hoặc sử dụng phím Enter để hoàn thành việc nhập liệu
        date_input.send_keys(Keys.RETURN)
        ######################################################
        # Tìm phần tử <input> bằng ID
        date_out = driver.find_element(By.ID, "datepickerendr")

        # Xóa dữ liệu hiện tại trong trường <input>
        date_out.clear()

        # Gửi ngày bạn muốn vào trường <input>
        date_out.send_keys(f"12/31/{start_year}")  # Thay "10/12/2023" bằng ngày bạn muốn

        # Hoặc sử dụng phím Enter để hoàn thành việc nhập liệu
        date_out.send_keys(Keys.RETURN)

        #Tat
        sut = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[19]/div[1]/div[2]")
        sut.click()
        time.sleep(0.5)
        #Chọn thẻ Agoclimato
        wait = WebDriverWait(driver, 10)
        select_element = wait.until(EC.presence_of_element_located((By.ID, 'usercommunityr')))

        select = Select(select_element)
        select.select_by_value("ag")

        # Sử dụng XPath để tìm đối tượng
        lat_bot = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[19]/div[2]/div/div/div[1]/table[3]/tbody/tr[1]/td[2]/input")
        #Xóa dữ liệu cũ
        lat_bot.clear()
        # Click vào đối tượng
        lat_bot.click()
    
        # Gửi giá trị "18.0060" vào đối tượng
        lat_bot.send_keys("18.0060")

        ######################################
        # Sử dụng XPath để tìm đối tượng
        long_bot = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[19]/div[2]/div/div/div[1]/table[3]/tbody/tr[2]/td[2]/input")
        #Xóa dữ liệu cũ
        long_bot.clear()
        # Click vào đối tượng
        long_bot.click()

        # Gửi giá trị "103.177" vào đối tượng
        long_bot.send_keys("103.177")
        #######################################
        # Sử dụng XPath để tìm đối tượng
        lat_up = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[19]/div[2]/div/div/div[1]/table[3]/tbody/tr[3]/td[2]/input")
        #Xóa dữ liệu cũ
        lat_up.clear()
        # Click vào đối tượng
        lat_up.click()

        # Gửi giá trị "20.3561" vào đối tượng
        lat_up.send_keys("20.3561")
        ######################################
        # Sử dụng XPath để tìm đối tượng
        long_up = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[19]/div[2]/div/div/div[1]/table[3]/tbody/tr[4]/td[2]/input")
        #Xóa dữ liệu cũ
        long_up.clear()
        # Click vào đối tượng
        long_up.click()

        # Gửi giá trị "107.154" vào đối tượng
        long_up.send_keys("107.154")
        #Chọn định dạng file
        wait = WebDriverWait(driver, 10)
        format_output = wait.until(EC.presence_of_element_located((By.ID, 'regional_format')))

        select = Select(format_output)
        select.select_by_value("CSV")
        #Chọn thuộc tính lần 1
        step1 = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div[19]/div[2]/div/div/div[1]/div[3]/ul/li[1]/a")
        step1.click()
        time.sleep(2)
        #Chọn thuộc tính lần 2
        step2 = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div[19]/div[2]/div/div/div[1]/div[3]/ul/li[2]/a")
        step2.click()
        time.sleep(2)
        #Chọn thuộc tính lần 3
        step3 = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div[19]/div[2]/div/div/div[1]/div[3]/ul/li[3]/a")
        step3.click()
        time.sleep(2)
        #Chọn thuộc tính lần 4
        step2 = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div[19]/div[2]/div/div/div[1]/div[3]/ul/li[4]/a")
        step2.click()
        time.sleep(2)
        #Chọn thuộc tính lần 5
        step3 = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div[19]/div[2]/div/div/div[1]/div[3]/ul/li[5]/a")
        step3.click()
        time.sleep(2)
        #Submit
        submit = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div[19]/div[2]/div/div/div[1]/table[4]/tbody/tr/td[1]/div")
        submit.click()
        time.sleep(30)
        #Download file
        data = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div[19]/div[2]/div/div/div[2]/div[2]/a[4]")
        data.click()
        time.sleep(3)
        #Back
        back = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div[19]/div[2]/div/div/div[2]/div[4]")
        back.click()
        time.sleep(3)
        
        #Chọn thuộc tính lần 1
        step1 = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div[19]/div[2]/div/div/div[1]/div[3]/ul/li[1]/a")
        step1.click()
        time.sleep(2)
        #Chọn thuộc tính lần 2
        step2 = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div[19]/div[2]/div/div/div[1]/div[3]/ul/li[2]/a")
        step2.click()
        time.sleep(2)
        #Chọn thuộc tính lần 3
        step3 = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div[19]/div[2]/div/div/div[1]/div[3]/ul/li[3]/a")
        step3.click()
        time.sleep(2)
        #Chọn thuộc tính lần 4
        step2 = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div[19]/div[2]/div/div/div[1]/div[3]/ul/li[4]/a")
        step2.click()
        time.sleep(2)
        #Chọn thuộc tính lần 5
        step3 = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div[19]/div[2]/div/div/div[1]/div[3]/ul/li[5]/a")
        step3.click()
        time.sleep(2)
        #Submit
        submit = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div[19]/div[2]/div/div/div[1]/table[4]/tbody/tr/td[1]/div")
        submit.click()
        time.sleep(30)
        #Download file
        data = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div[19]/div[2]/div/div/div[2]/div[2]/a[4]")
        data.click()
        time.sleep(3)
        #Back
        back = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div[19]/div[2]/div/div/div[2]/div[4]")
        back.click()
        time.sleep(3)

        start_year += 1

    driver.quit()

# Gọi hàm để thực hiện công việc từ năm 2000 đến 2023
perform_data_extraction(2001, 2023)
