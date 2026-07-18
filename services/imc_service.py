"""
Lógica pura de cálculo y clasificación de IMC (sin dependencias de Flask
ni de la base de datos), según los rangos estándar de la OMS.
"""

# (límite superior EXCLUSIVO, nombre de categoría, color hexadecimal)
_CATEGORIAS = [
    (18.5, 'Bajo peso', '#60a5fa'),
    (25.0, 'Peso normal', '#4ade80'),
    (30.0, 'Sobrepeso', '#fbbf24'),
    (35.0, 'Obesidad grado I', '#f97316'),
    (40.0, 'Obesidad grado II', '#f87171'),
]
_CATEGORIA_MAXIMA = ('Obesidad grado III', '#dc2626')


def calcular_imc(peso_kg: float, altura_m: float) -> float:
    """IMC = peso (kg) / altura (m) al cuadrado, redondeado a 2 decimales."""
    imc = peso_kg / (altura_m ** 2)
    return round(imc, 2)


def clasificar_imc(imc: float) -> tuple[str, str]:
    """Devuelve (categoria, color) según el valor de IMC."""
    for limite, categoria, color in _CATEGORIAS:
        if imc < limite:
            return categoria, color
    return _CATEGORIA_MAXIMA
