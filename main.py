import time
from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait

USER = "standard_user"
PASSWORD = "secret_sauce"

def main():
    """
    Automatiza el proceso de login y compra en saucedemo.com usando Selenium.
    Realiza las siguientes acciones:
    1. Inicia Chrome con opciones para evitar popups y extensiones.
    2. Ingresa usuario y contraseña.
    3. Añade dos productos al carrito.
    4. Realiza el checkout con datos de ejemplo.
    5. Finaliza la compra y cierra el navegador.
    """
    # Configura el servicio y las opciones de Chrome
    service = Service(ChromeDriverManager().install())
    option = webdriver.ChromeOptions()
    option.add_argument("--window-size=1920,1080")  # Tamaño de ventana
    option.add_argument("--incognito")              # Modo incógnito
    option.add_argument("--disable-extensions")     # Sin extensiones
    option.add_experimental_option("excludeSwitches", ["enable-automation"])  # Oculta modo automatizado
    option.add_experimental_option('useAutomationExtension', False)
    option.add_experimental_option("prefs", {
        "credentials_enable_service": False,        # Desactiva gestor de contraseñas
        "profile.password_manager_enabled": False
    })
    driver = Chrome(service=service, options=option)
    driver.get("https://www.saucedemo.com/")
    
    # LOGIN
    driver.find_element(By.ID, "user-name").send_keys(USER)         # Ingresa usuario
    driver.find_element(By.ID, "password").send_keys(PASSWORD)      # Ingresa contraseña
    driver.find_element(By.ID, "login-button").click()              # Click en login
    
    # COMPRAS
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()    # Añade mochila al carrito
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()  # Añade luz de bicicleta
    
    # CARRITO
    driver.find_element(
        By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[3]/a"
    ).click()                                                      # Abre el carrito
    time.sleep(1) 
    
    driver.find_element(
        By.CLASS_NAME, "checkout_button"
    ).click()                                                      # Click en checkout
    time.sleep(1) 
    
    # CHECKOUT
    driver.find_element(By.ID, "first-name").send_keys("Nombre")    # Ingresa nombre
    driver.find_element(By.ID, "last-name").send_keys("Apellido")   # Ingresa apellido
    driver.find_element(By.ID, "postal-code").send_keys("12345")    # Ingresa código postal
    time.sleep(2) 
    
    driver.find_element(By.ID, "continue").click()                  # Continúa con el checkout
    time.sleep(2) 
    
    driver.find_element(By.ID, "finish").click()                    # Finaliza la compra
    
    time.sleep(10)  # Espera para visualizar el resultado
    driver.quit()   # Cierra el navegador

if __name__ == "__main__":
    print("Corriendo main")
    main()