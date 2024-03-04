# from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('http://ticket.yes24.com/Special/48195')
wait = WebDriverWait(driver, 1.5)
chk = input()

driver.switch_to.window(driver.window_handles[-1])
driver.switch_to.frame("ifrmSeatFrame")

while(1):
    try:
        driver.find_element(By.XPATH, "/html/body/form/div[6]/map/area[1]").click()    ##새로고침
    except:
        print("새로고침없음")
        chk=input()
        continue
    try:
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "s13")))
    except:
        print("timeout")
        continue
    try:
        driver.find_element(By.CLASS_NAME, "s9").click()
        driver.find_element(By.XPATH,'//*[@id="form1"]/div[3]/div[2]/div/div[2]/p[2]/a/img').click()    # 다음
        driver.switch_to.default_content()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="StepCtrlBtn03"]/a[2]/img')))    ## 로딩대기
        driver.find_element(By.XPATH,'//*[@id="StepCtrlBtn03"]/a[2]/img').click()   # 다음(할인/쿠폰)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="StepCtrlBtn04"]/a[2]/img')))    ## 로딩대기
        driver.find_element(By.XPATH,'//*[@id="StepCtrlBtn04"]/a[2]/img').click()   # 다음 (수령방법)

        chk = input()
    except:
        print(f" 좌석없음or오류")
