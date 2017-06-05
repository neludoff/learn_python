from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://localhost/litecart/admin/login.php")


def test_login():
    try:

        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("password1").send_keys("admin")
        driver.find_element_by_name("login").click()
    except Exception:
        print('\nSomething awfull has happened')

    driver.close()

