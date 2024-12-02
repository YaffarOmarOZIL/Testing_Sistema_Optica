# Incluir acá los test cases para el módulo específico.
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
 
class TestLogin:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://127.0.0.1:8000/")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//a[text() = 'Informativa']").click()
        time.sleep(2)
    
    def teardown_method(self):
        self.driver.quit()
        print("Prueba visual completa")
    
    def test_verificar_quienes_somos(self):
        self.driver.find_element(By.XPATH, "//a[@href  = '#somos-proya']").click()
        time.sleep(2)
        actual = self.driver.find_element(By.XPATH, "//h2[contains(text(), 'Somos')]").text
        esperado = "Somos OPTICA MEDOP"
        assert esperado in actual, f"ERROR: Actual es: {actual} y el Esperado: {esperado}"
        
    def test_verificar_nuestras_diferentes_opciones(self):
        self.driver.find_element(By.XPATH, "//a[@href  = '#nuestros-programas']").click()
        time.sleep(2)
        actual = self.driver.find_element(By.XPATH, "//h2[contains(text(), 'ofrecemos')]").text
        esperado = "Te ofrecemos"
        assert esperado in actual, f"ERROR: Actual es: {actual} y el Esperado: {esperado}"

    def test_verificar_nuestras_caracteristicas(self):
        self.driver.find_element(By.XPATH, "//a[@href  = '#caracteristicas']").click()
        time.sleep(2)
        actual = self.driver.find_element(By.XPATH, "//li[contains(text(), '✔️ Vidrio')]").text
        esperado = "✔️"
        assert esperado in actual, f"ERROR: Actual es: {actual} y el Esperado: {esperado}"

    def test_verificar_visitanos_uno(self):
        self.driver.find_element(By.XPATH, "//section[@id='hero']//button").click()
        time.sleep(6)
        actual = self.driver.find_element(By.XPATH, "//*[@id='QA0Szd']/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[3]/div/div[2]/div[4]/div[1]/div/div/div[2]/div[1]/div[2]").text
        esperado = "medop"
        assert esperado in actual, f"ERROR: Actual es: {actual} y el Esperado: {esperado}"
    
    