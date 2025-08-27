from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def initialize_driver():  
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    return driver  

def login(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))
    print("✅ Login exitoso")

def ir_a_PIM(driver):
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a'))
    ).click()
    print("✅ Entrando al módulo PIM.")
    # Esperar que cargue el formulario de búsqueda
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a'))
    )
    print("📋 Formulario 'Employee Information' cargado.")






def hacer_click_en_boton_add(driver):
    try:
        boton_add = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button'))
        )
        boton_add.click()
        print("➕ Hiciste clic en el botón 'Add'")
    except Exception as e:
        print(f"❌ Error al hacer clic en 'Add': {e}")


def rellenar_formulario_empleado(driver, first, middle, last, emp_id="12345"):
    try:
        # First Name
        campo_first = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input'))
        )
        campo_first.send_keys(first)
        # Middle Name
        campo_middle = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/input')
        campo_middle.send_keys(middle)
        # Last Name
        campo_last = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input')
        campo_last.send_keys(last)
        # Employee ID
        campo_emp_id = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input')
        campo_emp_id.clear()  # 👈 Esto borra el valor por defecto
        campo_emp_id.send_keys(emp_id)
        print(f"✅ Formulario rellenado: {first} {middle} {last}, ID: {emp_id}")
    except Exception as e:
        print(f"❌ Error al rellenar formulario de empleado: {e}")



def hacer_click_en_boton_save(driver):
    try:
        boton_save = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'))
        )
        boton_save.click()
        print("💾 Hiciste clic en el botón 'Save'")
    except Exception as e:
        print(f"❌ Error al hacer clic en 'Save': {e}")

def hacer_click_en_segundo_boton_save(driver):
    try:
        segundo_boton_save = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button'))
        )
        segundo_boton_save.click()
        print("💾 Hiciste clic en el segundo botón 'Save'")
    except Exception as e:
        print(f"❌ Error al hacer clic en el segundo 'Save': {e}")

def segundo_boton_abajo(driver):
    try:
        cancelar_segundo = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[2]/button'))
        )
        segundo_boton_abajo.click()
        print("hiciste click en el save de abajo")
    except Exception as e:
        print("Error al hacer clic enb el de abjo 'save': {e}")



def main():  
    driver = initialize_driver()
    try:
        login(driver)
        ir_a_PIM(driver)
        time.sleep(2)
        hacer_click_en_boton_add(driver)
        time.sleep(2)
        rellenar_formulario_empleado(driver, "Adan", "Tabilo", "Soria", '111978')
        time.sleep(2)
        hacer_click_en_boton_save(driver)
        hacer_click_en_segundo_boton_save(driver)
        time.sleep(2)
        segundo_boton_abajo(driver)
        time.sleep(2)

       


    finally:
        driver.quit()
if __name__ == '__main__':
    main()

