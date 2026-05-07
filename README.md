# SISSU — Sistema de Servicio Social Unadista
## Módulo de Evaluación Nutricional mediante Índice de Masa Corporal (IMC)

**Universidad Nacional Abierta y a Distancia — UNAD**  
Acción Solidaria Universitaria · 2026

---

## Descripción

SISSU es una aplicación web desarrollada como parte de la iniciativa de servicio social de la UNAD, orientada a brindar herramientas de salud preventiva a la comunidad. Este módulo permite calcular el Índice de Masa Corporal (IMC) de forma interactiva, clasificar el resultado según estándares internacionales de la OMS, y generar recomendaciones personalizadas mediante inteligencia artificial.

La aplicación registra cada medición en una base de datos local y ofrece un panel de historial con estadísticas y visualizaciones gráficas de los datos recopilados.

---

## Funcionalidades

- Cálculo de IMC con soporte para unidades métricas e imperiales
- Clasificación automática según categorías de la OMS (bajo peso, peso normal, sobrepeso, obesidad grado I, II y III)
- Recomendaciones personalizadas generadas por inteligencia artificial (Claude — Anthropic)
- Escala visual interactiva del resultado
- Historial de mediciones con registro en base de datos
- Panel de estadísticas: total de mediciones, promedio, mínimo y máximo de IMC
- Gráfica de distribución por categorías (dona)
- Gráfica de evolución de mediciones (línea temporal)

---

## Tecnologías utilizadas

| Componente | Tecnología |
|---|---|
| Backend | Python 3.12 · Flask 3.0 |
| Base de datos | SQLite (integrado en Python) |
| Inteligencia artificial | Claude API — Anthropic |
| Gráficas | Chart.js |
| Frontend | HTML5 · CSS3 · JavaScript |
| Tipografía | Google Fonts (Open Sans) |

---

## Estructura del proyecto

```
Project_IMC/
├── app.py                  # Servidor Flask — rutas y lógica principal
├── database.py             # Gestión de base de datos SQLite
├── ai_recommendations.py   # Integración con la API de Claude
├── requirements.txt        # Dependencias del proyecto
├── Procfile                # Configuración para despliegue en servidor
├── imc.db                  # Base de datos (generada automáticamente)
├── static/
│   ├── Logo_unad.png       # Logotipo institucional
│   └── ods3.jpg            # Imagen ODS 3 - Salud y Bienestar
└── templates/
    ├── layout.html         # Plantilla base con navegación y footer
    ├── index.html          # Página principal — calculadora IMC
    └── historial.html      # Panel de historial y estadísticas
```

---

## Requisitos previos

- Python 3.10 o superior
- Cuenta en [Anthropic Console](https://console.anthropic.com) para obtener una API key

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
