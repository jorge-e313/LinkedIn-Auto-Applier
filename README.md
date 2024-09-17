<h1 align="center">🤖 LinkedIn Auto-Applier | Automates job application process 📝</h1>

<p align="center">LinkedIn Auto-Applier is developed in Python and uses Selenium technology to automatically fill out simple job applications on LinkedIn.</p>

<p align="center">
  <a href="https://www.linkedin.com/in/tu_perfil_linkedin">
    <img src="https://img.shields.io/badge/LinkedIn-Perfil-blue" alt="LinkedIn">
  </a>
  <br>
  <a href="https://www.youtube.com/watch?v=mlzIrIZFGoQ">
    <img src="https://img.shields.io/badge/YouTube-Tutorial-red" alt="YouTube Tutorial">
  </a>
</p>

## Tabla de Contenidos
1. [Requisitos previos](#requisitos-previos)
   - [Instalar Python](#instalar-python)
   - [Instalar Google Chrome](#instalar-google-chrome)
   - [Configurar ChromeDriver](#configurar-chromedriver)
   - [Instalar las bibliotecas necesarias](#instalar-las-bibliotecas-necesarias)
   - [Iniciar sesión en LinkedIn](#iniciar-sesión-en-linkedin)
2. [Resumen de pasos](#resumen-de-pasos)
3. [Ejecución del script](#ejecución-del-script)
4. [Tutorial de uso](#tutorial-de-uso)

## Requisitos previos

### 1. Instalar Python

El usuario debe descargar e instalar [Python](https://www.python.org/downloads/). Durante la instalación, asegúrate de marcar la opción "Add Python to PATH" (Agregar Python a la ruta del sistema).

### 2. Instalar Google Chrome

El programa depende de Google Chrome, por lo que el usuario debe tener instalado [Google Chrome](https://www.google.com/intl/es_es/chrome/).

### 3. Configurar ChromeDriver

El usuario necesitará tener descargado el [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads), que sea compatible con la versión de Google Chrome instalada.  

Sin embargo, el script incluye la línea:

```python
from webdriver_manager.chrome import ChromeDriverManager
```
Esto descargará automáticamente la versión correcta de ChromeDriver. Solo será necesario descargarlo manualmente si esta parte no funciona correctamente.

## 4. Instalar las bibliotecas necesarias

Las siguientes bibliotecas deben instalarse mediante pip (Python Package Installer):

- Selenium (`pip install selenium`)
- PyAutoGUI (`pip install pyautogui`)
- Colorama (`pip install colorama`)
- PyFiglet (`pip install pyfiglet`)
- Webdriver Manager para Chrome (`pip install webdriver-manager`)

El usuario puede ejecutar el siguiente comando en su terminal para instalar todas las bibliotecas necesarias a la vez:

```bash
pip install selenium pyautogui colorama pyfiglet webdriver-manager
```

### 5. Iniciar sesión en LinkedIn
Es necesario tener una sesión activa de LinkedIn en Google Chrome antes de ejecutar el programa, ya que el script usa la sesión actual del navegador para automatizar las acciones.
