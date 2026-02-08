# Albion Online – Farming Bot 🤖⚔️

Este proyecto es un **bot de farmeo para Albion Online**, desarrollado en **Python**, que utiliza visión por computadora y control por gamepad virtual para automatizar movimiento y acciones dentro del juego.

> ⚠️ **Aviso**: Este proyecto es únicamente con fines educativos y de experimentación. El uso de bots puede violar los Términos de Servicio de Albion Online. Úsalo bajo tu propia responsabilidad.

---

## 🧩 Requisitos del sistema

* **Sistema Operativo**: Windows (requerido para `pywin32` y `vgamepad`)
* **Python**: 3.8 (recomendado)
* **Albion Online** instalado y configurado en modo ventana (1280x800) se recomienda que la ventada este colcada de lado superior izquierdo si no hay que recalibrar las regiones

---

## 🐍 Versión de Python

Actualmente el bot está probado con:

```text
Python 3.8
```

> ⚠️ Aunque tienes Python **3.12** instalado en el sistema, **se recomienda usar Python 3.8** para evitar problemas de compatibilidad con algunas librerías.

---

## 📦 Instalación del entorno virtual

Se recomienda **usar un entorno virtual** para aislar las dependencias del proyecto.

```bash
python -m venv C:\Users\user\workspace\pybot
```

Activar el entorno virtual:

```bash
C:\Users\user\workspace\pybot\Scripts\activate
```

---

## 📚 Dependencias

Instala las librerías necesarias usando `pip`:

```bash
pip install pywin32
pip install keyboard
pip install pyautogui
pip install opencv-python
pip install Pillow
pip install vgamepad
pip install imagehash
pip install pytesseract
```

### 📌 Notas importantes

* `pywin32` **solo funciona en Windows**
* `pyautogui` requiere que la resolución del juego no cambie
* `opencv-python` se usa para procesamiento de imágenes
* `vgamepad` simula un **Xbox Controller virtual**

---

## 🔤 Instalación de Tesseract OCR

El bot utiliza **Tesseract** para reconocimiento de texto (OCR).

### 1️⃣ Descargar Tesseract

Descárgalo desde el repositorio oficial para Windows:

👉 [https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki)

### 2️⃣ Instalar

Durante la instalación:

* Marca la opción **Add to PATH** (si está disponible)
* Anota la ruta de instalación (ejemplo):

```text
C:\Program Files\Tesseract-OCR\tesseract.exe
```

### 3️⃣ Configurar en Python (si es necesario)

Si Tesseract no está en el PATH, agrega la ruta en tu código:

```python
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

---

## 🕹️ ¿Cómo funciona el bot?

El bot se basa en los siguientes módulos:

* 🎮 **Control de movimiento** usando un Xbox Controller virtual
* 👁️ **Visión por computadora** para detectar:

  * Barra de vida
  * Enemigos
  * Elementos del HUD
* 🧠 **Lógica de estado** para decidir cuándo farmear, moverse o detenerse
* 🗺️ **Navegación inteligente** basada en el mini-mapa (no aleatoria)

---

## ▶️ Ejecución del bot

1. Abre Albion Online
2. Coloca el personaje en una zona segura
3. Activa el entorno virtual
4. Ejecuta el script principal:

```bash
python main.py
```

> ⚠️ No uses el mouse ni el teclado mientras el bot está activo

---

## 🛠️ Problemas comunes

### ❌ `pip no se reconoce`

Asegúrate de que Python esté agregado al PATH o ejecuta:

```bash
python -m pip install nombre_libreria
```

### ❌ El bot no detecta bien la vida

* Verifica la resolución
* Asegúrate de que el HUD no tenga escalado
* Usa imágenes de referencia actualizadas

---

## 🚀 Próximas mejoras

* Anti-stuck logic
* Detección de enemigos y huida
* Mejor cálculo de vida
* Navegación avanzada por mapa

---

## 😎 Nota final

Si llegaste hasta aquí: **bienvenido al farmeo automático**.
Programador o no… este bot te interesa 👀🔥
