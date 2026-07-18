"""
Configuración central de la aplicación.
Todas las variables sensibles se leen desde el entorno (.env en local,
Environment Variables en Render).
"""
import os


class Config:
    # Base de datos PostgreSQL (Render Postgres, Neon, Supabase, etc.)
    DATABASE_URL = os.environ.get("DATABASE_URL")

    # IA gratuita — Groq (https://console.groq.com)
    GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
    GROQ_MODEL = os.environ.get("GROQ_MODEL", "llama-3.3-70b-versatile")

    # Puerto (Render lo asigna automáticamente vía la variable PORT)
    PORT = int(os.environ.get("PORT", 8000))
