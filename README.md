# SISSU — Sistema de Servicio Social Unadista
## Módulo de Evaluación Nutricional mediante Índice de Masa Corporal (IMC)

**Universidad Nacional Abierta y a Distancia — UNAD**
Acción Solidaria Universitaria · 2026

---

## Descripción

SISSU es una aplicación web desarrollada como parte de la iniciativa de servicio social de la UNAD, orientada a brindar herramientas de salud preventiva a la comunidad. Este módulo permite calcular el Índice de Masa Corporal (IMC) de forma interactiva, clasificar el resultado según estándares internacionales de la OMS, y generar recomendaciones personalizadas mediante inteligencia artificial.

La aplicación registra cada medición en una base de datos PostgreSQL y ofrece un panel de historial con estadísticas y visualizaciones gráficas de los datos recopilados.

---

## Funcionalidades

- Cálculo de IMC con soporte para unidades métricas e imperiales
- Clasificación automática según categorías de la OMS
- Recomendaciones personalizadas generadas por inteligencia artificial (Groq)
- Escala visual interactiva del resultado
- Historial de mediciones persistente
- Panel de estadísticas y gráficas (distribución por categoría, evolución temporal)
- Encuesta de satisfacción integrada

---

## Tecnologías utilizadas

| Componente | Tecnología |
|---|---|
| Backend | Python 3.12 · Flask 3.0 |
| Base de datos | PostgreSQL |
| Inteligencia artificial | Groq API (nivel gratuito) |
| Gráficas | Chart.js |
| Frontend | HTML5 · CSS3 · JavaScript |

---

## Estructura del proyecto

```
imc-unad/
├── app.py                      # Punto de entrada — ensambla la aplicación
├── config.py                   # Variables de configuración desde el entorno
├── requirements.txt
├── Procfile                     # Comando de arranque para Render
├── .env.example                 # Plantilla de variables de entorno
├── database/
│   ├── __init__.py
│   └── connection.py            # Conexión y consultas SQL
├── services/
│   ├── __init__.py
│   ├── imc_service.py           # Cálculo y clasificación de IMC
│   └── ai_service.py            # Recomendaciones con Groq + respaldo
├── routes/
│   ├── __init__.py
│   ├── main_routes.py           # Rutas de páginas (/ , /historial)
│   └── api_routes.py            # Ruta de API (/calcular)
├── static/
│   ├── css/style.css
│   ├── js/calculadora.js
│   ├── js/historial.js
│   ├── Logo_unad.png
│   ├── ods3.jpg
│   └── favicon.ico
└── templates/
    ├── layout.html
    ├── index.html
    └── historial.html
```

---

## Instalación y ejecución local

**1. Clonar el repositorio**
```bash
git clone https://github.com/TU_USUARIO/TU_REPOSITORIO.git
cd imc-unad
```

**2. Crear entorno virtual**
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Mac / Linux
source .venv/bin/activate
```

**3. Instalar dependencias**
```bash
pip install -r requirements.txt
```

**4. Ejecutar la aplicación:configurar config.py y ejecutar la aplicación**
```bash
python app.py
```

**5. Abrir en el navegador**
```
http://localhost:8000
```

---

## Variables de entorno

| Variable | Descripción | Requerida |
|---|---|---|
| `DATABASE_URL` | Cadena de conexión a PostgreSQL | Sí |
| `GROQ_API_KEY` | Clave de la API gratuita de Groq | No* |
| `GROQ_MODEL` | Modelo a usar (por defecto `llama-3.3-70b-versatile`) | No |
| `PORT` | Puerto del servidor (Render lo asigna solo) | No |

\* Sin `GROQ_API_KEY`, la app funciona igual pero usa mensajes de recomendación predefinidos en vez de generarlos con IA.

### Obtener una base de datos PostgreSQL gratuita

Las bases de datos PostgreSQL **gratuitas de Render expiran a los 30 días** y se eliminan junto con sus datos. Para evitar este ciclo, se recomienda usar **[Neon](https://neon.tech)**: su plan gratuito no tiene fecha de expiración (0.5 GB, sin tarjeta de crédito). Crea un proyecto ahí, copia la cadena de conexión que te dan, y pégala como `DATABASE_URL`.

### Obtener una API key gratuita de Groq

1. Entra a [console.groq.com](https://console.groq.com) y crea una cuenta (no pide tarjeta)
2. Genera una API key
3. Pégala en `GROQ_API_KEY`

El nivel gratuito de Groq permite aproximadamente 1,000 solicitudes por día — más que suficiente para un proyecto universitario.

---

## Rutas de la aplicación

| Ruta | Método | Descripción |
|---|---|---|
| `/` | GET | Página principal con la calculadora de IMC |
| `/historial` | GET | Panel de historial, estadísticas y gráficas |
| `/calcular` | POST | Endpoint de cálculo — recibe datos y retorna resultado en JSON |

---

## Clasificación IMC (OMS)

| Categoría | Rango IMC |
|---|---|
| Bajo peso | < 18.5 |
| Peso normal | 18.5 — 24.9 |
| Sobrepeso | 25.0 — 29.9 |
| Obesidad grado I | 30.0 — 34.9 |
| Obesidad grado II | 35.0 — 39.9 |
| Obesidad grado III | ≥ 40.0 |

---

## Alineación con los Objetivos de Desarrollo Sostenible

Este proyecto contribuye al **ODS 3 — Salud y Bienestar**, promoviendo el acceso a herramientas de salud preventiva y fomentando hábitos de vida saludable en la comunidad universitaria y el público general.

---

## Licencia

Proyecto académico desarrollado en el marco del programa de Acción Solidaria de la UNAD. Uso educativo y social sin fines comerciales.
