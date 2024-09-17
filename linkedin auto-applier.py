import os
import time
import random
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from colorama import Fore, Style, init
import pyfiglet 

# Inicializar Colorama
init(autoreset=True)

# Función para mostrar títulos en ASCII con más detalles
def ascii_title(text, color=Fore.YELLOW):
    # Detalles decorativos previos al arte ASCII
    print(f"{Fore.BLUE}#############################################################")
    print(f"{Fore.YELLOW}#     Programa de Automatización - LinkedIn Auto-Applier    #")
    print(f"{Fore.BLUE}###############################################################################")
    print(f"{Fore.RED}# Nota: Uso laboral y controlado únicamente, no romper procesos de selección  #")
    print(f"{Fore.BLUE}###############################################################################\n")
    
    # Generar arte ASCII para el título
    ascii_art = pyfiglet.figlet_format(text)
    
    # Mostrar el arte ASCII con el color deseado
    print(f"{color}{ascii_art}{Style.RESET_ALL}")
    
    # Información adicional después del arte ASCII
    print(f"{Fore.BLUE}#####################################################################")
    print(f"{Fore.YELLOW}#     Automatiza el proceso de solicitar empleos en LinkedIn!!!     #")
    print(f"{Fore.BLUE}#####################################################################\n")

# Mostrar el título principal en ASCII
ascii_title("LinkedIn Auto-Applier")

# Función para tiempos de espera aleatorios
def espera_aleatoria(min_time=2, max_time=10):
    time_to_wait = random.uniform(min_time, max_time)
    time.sleep(time_to_wait)

# Colores para el output
class color:
    BOLD = Fore.LIGHTWHITE_EX
    GREEN = Fore.GREEN
    YELLOW = Fore.YELLOW
    RED = Fore.RED
    BLUE = Fore.BLUE
    END = Style.RESET_ALL

# Configuración de trabajos predefinidos
configurations = {
    "1": ("Cibersecurity", "España", "24000"),
    "2": ("Developer", "Madrid", "24000"),
    "3": ("Data analyst", "Barcelona", "24000"),
}

# Mostrar opciones y añadir opción personalizada
print(f"{color.BOLD}Opciones disponibles:{color.END}\n")
for num, (work, location, salary) in configurations.items():
    print(f"{color.YELLOW}{num}{color.END}: {work} en {location}")

print(f"{color.YELLOW}4{color.END}: Ingresar datos manualmente\n")
print(f"{color.YELLOW}Puedes cambiar las opciones por defecto editando el archivo.{color.END}")
print(f"{color.YELLOW}Para introducir los datos de forma manual, selecciona la opción 4.{color.END}")

# Pedir selección de trabajo
candidate = input("\nIntroduce el número de la opción de trabajo (1, 2, 3 o 4): ")

# Validar la selección del usuario
if candidate not in configurations and candidate != "4":
    print(f"{color.RED}Opción no válida.{color.END}")
    exit()

# Si selecciona una opción predefinida
if candidate in configurations:
    work, location, salary = configurations[candidate]
else:
    # Opción de ingresar manualmente
    work = input("Introduce el puesto de trabajo: ")
    location = input("Introduce la ciudad o país: ")
    salary = input("Introduce el salario anual bruto (€): ")

# Mostrar la selección final
print(f"\nHas seleccionado: {color.GREEN}{work} en {location} con {salary}€{color.END}")

# Confirmar la selección
if input(f"Confirmas que este es el puesto de trabajo a postular (y/n): ").lower() not in ["y", "sí"]:
    print(f"{color.RED}Proceso cancelado.{color.END}")
    exit()

print(f"{color.GREEN}¡Proceso completado!{color.END}")

# Obtener la ruta del perfil del usuario actual en Windows
user_profile = os.path.expandvars("%USERPROFILE%")

# Configuración de Selenium
options = webdriver.ChromeOptions()
options.add_argument(f"user-data-dir={user_profile}/AppData/Local/Google/Chrome/User Data")
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--ignore-ssl-errors=yes")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--start-maximized")

# Inicializar el navegador
driver = webdriver.Chrome(options=options)
driver.get("https://www.google.com")
espera_aleatoria()

cont_pass, cont_fail = 0, 0

# Función para mostrar el resultado de cada aplicación
def verdict(pass_status, txt):
    global cont_pass, cont_fail
    if pass_status:
        print(f"{color.GREEN}ÉXITO {txt}{color.END}")
        cont_pass += 1
    else:
        print(f"{color.RED}FAIL {txt}{color.END}")
        cont_fail += 1

print(f"{color.YELLOW}AUTO APPLY START{color.END}")

# Función principal para aplicar a trabajos
def apply_to_job(driver, work, location, salary):
    driver.get("https://www.linkedin.com/jobs/")
    espera_aleatoria()

    try:
        # Búsqueda de trabajo y ubicación
        job_input = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "jobs-search-box__text-input")))
        location_input = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Ciudad, provincia/estado o código postal']")))
        job_input.clear()
        job_input.send_keys(work)
        location_input.clear()
        location_input.send_keys(location + Keys.RETURN)
        print(f"Mostrando ofertas de trabajo para: {work} en {location}")
        espera_aleatoria()

        # Aplicar filtros de "Solicitud sencilla"
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="Filtro «Solicitud sencilla»."]'))).click()
        espera_aleatoria()
        jobs = driver.find_elements(By.CSS_SELECTOR, '.jobs-search-results__list-item')
        espera_aleatoria()

        for job in jobs:
            job.click()
            try:
                WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CLASS_NAME, 'jobs-apply-button'))).click()
                espera_aleatoria()
            except (NoSuchElementException, TimeoutException):
                print(f"{color.YELLOW}Empleo ya solicitado anteriormente.{color.END}")
            
            # Intentar enviar la solicitud
            try:
                WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Enviar solicitud']"))).click()
                print(f"{color.GREEN}Solicitud enviada con éxito{color.END}")
                verdict(True, "Solicitud enviada correctamente")
                espera_aleatoria()

                # Cerrar la pestaña de confirmación
                try:
                    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'use[href="#close-medium"]'))).click()
                except (NoSuchElementException, TimeoutException):
                    print(f"{color.YELLOW}No se encontró el botón para cerrar la pestaña de confirmación.{color.END}")

            except TimeoutException:
                espera_aleatoria()

            # Navegar por las etapas de la aplicación
            try:
                WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Ir al siguiente paso']"))).click()
                espera_aleatoria()

                WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Ir al siguiente paso']"))).click()
                espera_aleatoria()

                # Encuentra todos los elementos <select> en la página
                select_elements = driver.find_elements(By.TAG_NAME, "select")

                # Itera sobre todos los elementos select
                for select_element in select_elements:
                    try:
                        # Crea un objeto Select para cada elemento
                        select = Select(select_element)
                        
                        # Intenta seleccionar la opción 'Yes' por el texto visible
                        select.select_by_visible_text("Yes")
                    except Exception as e:
                        # Si ocurre algún error, lo capturamos, pero continuamos con el siguiente elemento
                        print(f"No se pudo seleccionar 'Yes' en un select: {e}")
                        pass

                # Completar detalles adicionales
                for label in driver.find_elements(By.XPATH, "//label[contains(text(), 'años') or contains(text(), 'years')]"):
                    input_field = label.find_element(By.XPATH, "..//input")
                    input_field.clear()
                    input_field.send_keys("1")

                for radio_button in driver.find_elements(By.XPATH, "//input[@value='Yes']"):
                    try:
                        driver.find_element(By.XPATH, f"//label[@for='{radio_button.get_attribute('id')}']").click()
                    except Exception as e3:
                        print(f"Error en la opción 3: {e3}")

                # Ingresar salario esperado
                # Buscar el campo de entrada basado en la etiqueta
                for label in driver.find_elements(By.XPATH, "//label[contains(text(), 'salar') or contains(text(), 'expectativas') or contains(text(), 'remuneración')]"):
                    # Buscar el campo de entrada asociado
                    input_field = label.find_element(By.XPATH, "..//input")
                    # Asegurarse de que el campo de entrada es visible e interactuable
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(input_field))
                    input_field.clear()
                    input_field.send_keys(salary)

                WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Revisar tu solicitud']"))).click()
                espera_aleatoria()

                pyautogui.hotkey('ctrl', '-', 'ctrl', '-', 'ctrl', '-')
                espera_aleatoria()

                WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Enviar solicitud']"))).click()
                print(f"{color.GREEN}Solicitud enviada con éxito{color.END}")
                verdict(True, "Solicitud enviada correctamente")

                pyautogui.hotkey('ctrl', '+', 'ctrl', '+', 'ctrl', '+')
                espera_aleatoria()

                WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Descartar']"))).click()
                driver.back()

            except (NoSuchElementException, TimeoutException) as e:
                verdict(False, "Error en el proceso de solicitud (Empleo ya solicitado anteriormente)")

    except (NoSuchElementException, TimeoutException) as e:
        print(f"Error al aplicar: {e}")
        verdict(False, f"Error inesperado: {e}")

# Ejecutar aplicación a trabajos
apply_to_job(driver, work, location, salary)

# Resultados finales
print(f"{color.YELLOW}Resultados...{color.END}")
print(f"{color.GREEN}Total solicitudes enviadas con éxito: {cont_pass}{color.END}")
print(f"{color.RED}Total solicitudes fallidas: {cont_fail}{color.END}")

# Cerrar navegador tras la espera
espera_aleatoria()
driver.quit()