from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.common.by import By

def get_work_shift_table():
    driver = BuiltIn().get_library_instance('SeleniumLibrary').driver
    rows = driver.find_elements(By.XPATH, "//div[@class='oxd-table-body']//div[@role='row']")
    data = []
    for row in rows:
        name = row.find_element(By.XPATH, ".//div[@role='cell'][2]").text
        from_time = row.find_element(By.XPATH, ".//div[@role='cell'][3]").text
        to_time = row.find_element(By.XPATH, ".//div[@role='cell'][4]").text
        hours = row.find_element(By.XPATH, ".//div[@role='cell'][5]").text

        data.append({
            "name": name,
            "from": from_time,
            "to": to_time,
            "hours": hours
        })
    return data