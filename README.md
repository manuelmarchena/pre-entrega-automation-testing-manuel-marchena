# 🧪 Pre‑Entrega | Automatización QA con Selenium & Pytest

Este proyecto corresponde a la **Pre‑Entrega del curso Automation QA – Talento Tech**, y tiene como propósito demostrar la capacidad para **automatizar flujos básicos de navegación web** aplicando los conocimientos adquiridos hasta la Clase 8.  
El objetivo es implementar casos de prueba automatizados con **Selenium WebDriver**, **Pytest** y **Python**, sobre la aplicación demo [SauceDemo](https://www.saucedemo.com).

---

## 🌐 Sitio Web a Automatizar  
**URL:** [https://www.saucedemo.com](https://www.saucedemo.com)  
Aplicación web diseñada para prácticas de testing automatizado.

---

## ⚙️ Tecnologías Utilizadas  
- 🐍 **Python 3.10+**  
- 🌐 **Selenium WebDriver**  
- 🧪 **Pytest** (framework de testing)  
- ⚙️ **Webdriver‑Manager** (gestión automática de drivers)  
- 🧾 **Pytest‑HTML** (reportes HTML)  
- 💻 **Git & GitHub** (control de versiones)

---

## 📁 Estructura del Proyecto  

```
Preentrega/
│
├── tests/                           # Carpeta de pruebas automatizadas
│   ├── test_access_page.py          # Verifica acceso al sitio y elementos del formulario
│   ├── test_login.py                # Escenarios de login (válido, inválido, campos vacíos)
│   ├── test_catalog.py              # Verifica catálogo: título, productos, interfaz
│   └── test_cart.py                 # Flujo del carrito: agregar, verificar, eliminar
│
├── utils/                           # Funciones auxiliares y constantes
│   ├── constants.py                 # URLs, credenciales, locators
│   └── helpers.py                   # Funciones reutilizables (login, esperar, etc.)
│
├── reports/                         # Reportes HTML y capturas automáticas
├── conftest.py                      # Fixtures comunes (p. ej., driver)
├── requirements.txt                 # Dependencias del proyecto
├── README.md                        # Este archivo
└── .gitignore                       # Archivos/carpetas ignorados por Git
```

---

## 🧩 Instalación y Configuración  

### 1️⃣ Clonar el repositorio  
```bash
git clone https://github.com/manuelmarchena/pre-entrega-automation-testing-manuel-marchena.git  
cd pre‑entrega‑automation‑testing‑manuel‑marchena  
```

### 2️⃣ Crear y activar entorno virtual  
```bash
python -m venv .venv  
.\.venv\Scripts\Activate
```

### 3️⃣ Instalar dependencias  
```bash
pip install -r requirements.txt
```

---

## 🚀 Ejecución de los Tests  

### Ejecutar todos los casos  
```bash
pytest -v -s
```

### Generar reporte HTML  
```bash
pytest -v --html=reports/reporte.html
```

📄 El reporte se generará en la carpeta `reports/` con un resumen de todos los casos ejecutados.

---

## 🧪 Test Scenarios y Casos de Prueba

| ID    | Módulo   | Tipo               | Escenario                                                  | Caso de prueba                                         | Resultado esperado                                           |
|-------|----------|--------------------|------------------------------------------------------------|--------------------------------------------------------|--------------------------------------------------------------|
| **TC000** | Acceso   | Funcional / Smoke   | Validar que la página de login cargue correctamente        | Verificar URL `https://www.saucedemo.com`, título “Swag Labs”, y elementos del formulario visibles. | Página accesible, título correcto y formulario visible.     |
| **TC001** | Login    | Funcional           | Login exitoso con credenciales válidas                     | Usuario: `standard_user` / Contraseña: `secret_sauce`  | Redirección a `/inventory.html`, título “Products”.          |
| **TC002** | Login    | Negativo            | Intentar login con usuario/contraseña inválidos            | Usuario: `fake_user` / Contraseña: `wrong_pass`        | Mensaje de error *“Username and password do not match…”*.   |
| **TC003** | Login    | Negativo            | Campos vacíos                                               | No completar usuario ni contraseña                    | Mensaje *“Username is required”*.                            |
| **TC004** | Login    | Negativo            | Contraseña vacía                                            | Usuario válido / contraseña vacía                      | Mensaje *“Password is required”*.                            |
| **TC005** | Login    | Negativo            | Usuario bloqueado                                           | Usuario: `locked_out_user`                             | Mensaje *“Sorry, this user has been locked out.”*.           |
| **TC006** | Catálogo | Funcional           | Validar título y carga de productos                          | Ingresar al inventario luego del login                 | Título “Products”, al menos un producto visible.             |
| **TC007** | Catálogo | Visual              | Validar elementos de interfaz                                | Verificar menú lateral, ícono del carrito y filtro     | Elementos visibles y funcionales.                            |
| **TC008** | Catálogo | Funcional           | Verificar información del primer producto                    | Nombre y precio del primer producto                    | Nombre y precio visibles y no vacíos.                        |
| **TC009** | Carrito  | Funcional           | Agregar producto al carrito                                  | Hacer clic en “Add to cart”                            | Contador del carrito muestra “1”.                             |
| **TC010** | Carrito  | Funcional           | Verificar producto en el carrito                              | Ingresar al carrito y confirmar producto agregado     | El producto está listado correctamente.                       |
| **TC011** | Carrito  | Funcional           | Quitar producto del carrito                                   | Eliminar el producto desde el carrito                  | Contador desaparece y carrito queda vacío.                    |

---

## 🧠 Casos de Prueba Automatizados  

### 🔹 1. Acceso a la Página  
- Validar carga del sitio, URL correcta y presencia de los campos de login.

### 🔹 2. Login  
- Escenarios exitoso, inválido, usuario bloqueado y campos vacíos.  
- Validar redirección y mensajes de error.

### 🔹 3. Catálogo  
- Validar título “Products”, visibilidad de productos y elementos de interfaz.  
- Confirmar nombre y precio del primer producto.

### 🔹 4. Carrito  
- Agregar, verificar y eliminar productos.  
- Confirmar contador y estado del carrito.

---

## 🧭 Orden Recomendado de Ejecución  
1️⃣ test_access_page.py  
2️⃣ test_login.py  
3️⃣ test_catalog.py  
4️⃣ test_cart.py  

Esto asegura validar primero la disponibilidad del sitio y luego los flujos funcionales dependientes.

---

## 📷 Evidencias y Reportes  
- **Reporte HTML:** `reports/reporte.html`  
- **Capturas automáticas:** generadas en caso de fallos.  
- **Logs de ejecución:** visibles en consola Pytest.

---

## 🧑‍💻 Autor  
**Manuel Marchena**  
📧 [GitHub Profile](https://github.com/manuelmarchena)  
🎓 Curso: *Automation QA – Talento Tech*  
🗓️ Pre‑Entrega Proyecto Selenium WebDriver con Python  
