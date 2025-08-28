# 🛒 Prac-Selenium

Proyecto de práctica de **automatización web** utilizando **Selenium en Python** por Fernando Blanco.
El script simula un flujo completo de compra en [saucedemo.com](https://www.saucedemo.com/) 🛍️, desde el inicio de sesión hasta la finalización de la transacción.

---

## ✨ Características principales

- 🚀 Automatiza la apertura de un navegador Chrome en modo incógnito y sin extensiones.
- 🔐 Realiza login con credenciales de prueba.
- 🛒 Añade productos al carrito de compra.
- 📦 Completa el proceso de checkout con datos ficticios.
- 🏁 Finaliza la compra y cierra el navegador automáticamente.

---

## 🛠️ Requisitos

- **Python 3.x**
- **Google Chrome**
- **ChromeDriver** (administrado automáticamente por `webdriver_manager`)

### Instalación de dependencias

`pip install selenium webdriver-manager`

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/FernandoBlanco10/Prac-Selenium.git
    cd Prac-Selenium
    ```
2. (Opcional) Crea y activa un entorno virtual:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # en Windows: venv\Scripts\activate
    ```
3. Instala dependencias:
    ```bash
    pip install selenium
    ```
