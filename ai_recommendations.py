import anthropic
import os


ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

def get_recommendation(imc, categoria, edad, sexo, peso, altura):
    """
    Genera una recomendación personalizada usando Claude de Anthropic.
    """
    try:
        client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

        prompt = f"""Eres un nutricionista y especialista en salud. 
        
Un paciente acaba de calcular su IMC con los siguientes datos:
- Edad: {edad} años
- Sexo: {sexo}
- Peso: {peso} kg
- Altura: {altura} m
- IMC calculado: {imc}
- Categoría: {categoria}

Por favor genera una recomendación personalizada, empática y motivadora de máximo 4 oraciones. 
Debe incluir:
1.  Un saludo cordial y empático
2. Una evaluación breve de su estado actual
3. 2-3 recomendaciones concretas y prácticas
4. Un mensaje motivador al final
5. Indica que esto no reemplaza la consulta con un profesional de salud, pero que es un buen punto de partida para mejorar su bienestar.

Responde en español, de forma amigable y profesional. No uses asteriscos ni markdown, solo texto plano."""

        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=400,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return message.content[0].text

    except Exception as e:
        # Si falla la IA, devolver mensaje predefinido según categoría
        return get_fallback_recommendation(categoria, imc)


def get_fallback_recommendation(categoria, imc):
    """Recomendaciones predefinidas si la IA no está disponible."""
    mensajes = {
        'Bajo peso': f"Hola, tu IMC de {imc} indica bajo peso. Es importante que consultes con un médico o nutricionista para desarrollar un plan alimenticio que te ayude a alcanzar un peso saludable. Incluye alimentos ricos en nutrientes y calorías de calidad como frutos secos, aguacate y proteínas. ¡Con el apoyo adecuado puedes lograrlo!",
        'Peso normal': f"¡Excelente! Tu IMC de {imc} está dentro del rango saludable. Mantén tus buenos hábitos con una dieta equilibrada y actividad física regular de al menos 30 minutos al día. Continúa con controles periódicos para monitorear tu salud. ¡Sigue así!",
        'Sobrepeso': f"Hola, tu IMC de {imc} indica sobrepeso leve. Con pequeños cambios en tu rutina puedes mejorar significativamente: reduce el consumo de ultraprocesados, aumenta frutas y verduras, e incorpora 30 minutos de caminata diaria. ¡Cada pequeño cambio cuenta y tú tienes toda la capacidad de lograrlo!",
        'Obesidad grado I': f"Hola, tu IMC de {imc} indica obesidad grado I. Te recomendamos consultar con un profesional de salud para un plan personalizado. Comienza con cambios graduales: más agua, menos azúcar y actividad física moderada. ¡El camino hacia una vida más saludable empieza hoy!",
        'Obesidad grado II': f"Hola, con un IMC de {imc} es importante que busques orientación médica profesional. Un equipo de salud puede ayudarte con un plan integral de nutrición y ejercicio. Recuerda que cada paso cuenta y mereces vivir con bienestar. ¡No estás solo en este camino!",
        'Obesidad grado III': f"Hola, tu IMC de {imc} requiere atención médica especializada. Por favor consulta con un médico a la brevedad para recibir el apoyo que necesitas. Con el tratamiento adecuado es posible mejorar tu salud y calidad de vida. ¡Tu bienestar es lo más importante!"
    }
    return mensajes.get(categoria, f"Hola, te recomendamos consultar con un profesional de salud para orientación personalizada basada en tu IMC de {imc}.")
