from lib2to3.pgen2 import driver
from select import select
from socket import if_nameindex
from turtle import down
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class usando_unittest(unittest.TestCase):
    def setUp(self):
        print("Este es el setUp")
        self.driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe")

    # test1
    def test_IrPagina(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://qainterview.pythonanywhere.com/")
        self.assertIn("Factoriall", driver.title, msg="no estas en la pagina correcto")

     # test2
    def test_CalcularFactorial(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://qainterview.pythonanywhere.com/")
        elemento = driver.find_element_by_id("number")
        elemento.send_keys("10")
        elemento = driver.find_element_by_xpath("//*[@id='getFactorial']")
        elemento.send_keys(Keys.ENTER)
        time.sleep(10)

     # test3
    ##def test_NoCalcularConTextVacio(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://qainterview.pythonanywhere.com/")
        elemento = driver.find_element_by_xpath("//*[@id='getFactorial']")
        elemento.send_keys(Keys.ENTER)
        self.assertIn("Please enter an integer", driver.find_element_by_css_selector("#resultDiv"), msg="no se puede calcular con el textbox vacio")
        time.sleep(10)

    # siempre se ejecuta de ultimo
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
