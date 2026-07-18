"""Rutas de API (JSON) consumidas por el JavaScript del frontend."""
from flask import Blueprint, request, jsonify

from database.connection import save_measurement
from services.imc_service import calcular_imc, clasificar_imc
from services.ai_service import get_recommendation

api_bp = Blueprint('api', __name__)


@api_bp.route('/calcular', methods=['POST'])
def calcular():
    data = request.get_json()

    peso = float(data.get('peso'))
    altura = float(data.get('altura'))
    edad = int(data.get('edad'))
    sexo = data.get('sexo', 'no especificado')

    imc = calcular_imc(peso, altura)
    categoria, color = clasificar_imc(imc)

    recomendacion = get_recommendation(imc, categoria, edad, sexo, peso, altura)

    save_measurement(peso, altura, edad, sexo, imc, categoria)

    return jsonify({
        'imc': imc,
        'categoria': categoria,
        'color': color,
        'recomendacion': recomendacion,
    })
