from flask import Flask, render_template, request, jsonify
from database import init_db, save_measurement, get_all_measurements, get_stats
from ai_recommendations import get_recommendation
import os
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)

# Inicializar base de datos al arrancar
init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/historial')
def historial():
    measurements = get_all_measurements()
    stats = get_stats()
    return render_template('historial.html', measurements=measurements, stats=stats)

@app.route('/calcular', methods=['POST'])
def calcular():
    data = request.get_json()
    
    
    peso = float(data.get('peso'))
    altura = float(data.get('altura'))
    edad = int(data.get('edad'))
    sexo = data.get('sexo', 'no especificado')

    # Calcular IMC
    imc = peso / (altura ** 2)
    imc_redondeado = round(imc, 2)

    # Clasificación
    if imc < 18.5:
        categoria = 'Bajo peso'
        color = '#60a5fa'
    elif imc < 25:
        categoria = 'Peso normal'
        color = '#4ade80'
    elif imc < 30:
        categoria = 'Sobrepeso'
        color = '#fbbf24'
    elif imc < 35:
        categoria = 'Obesidad grado I'
        color = '#f97316'
    elif imc < 40:
        categoria = 'Obesidad grado II'
        color = '#f87171'
    else:
        categoria = 'Obesidad grado III'
        color = '#dc2626'

    # Obtener recomendación con IA
    recomendacion = get_recommendation(imc_redondeado, categoria, edad, sexo, peso, altura)

    # Guardar en base de datos
    save_measurement(peso, altura, edad, sexo, imc_redondeado, categoria)

    return jsonify({
        'imc': imc_redondeado,
        'categoria': categoria,
        'color': color,
        'recomendacion': recomendacion
    })

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port, debug=False)
