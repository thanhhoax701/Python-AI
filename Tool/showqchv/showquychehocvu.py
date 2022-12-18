from selenium import webdriver

driver = webdriver.Chrome(executable_path='..\showqchv\chromedriver.exe')

driver.get("https://dsa.ctu.edu.vn/")
driver.find_element_by_link_text("Nội quy-Quy chế").click()
driver.find_element_by_link_text("Quy chế học vụ").click()
driver.find_element_by_link_text("Xem chi tiết").click()