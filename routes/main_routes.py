"""Rutas de páginas HTML (contenido visible al usuario)."""
from flask import Blueprint, render_template

from database.connection import get_all_measurements, get_stats

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    return render_template('index.html')


@main_bp.route('/historial')
def historial():
    measurements = get_all_measurements()
    stats = get_stats()
    return render_template('historial.html', measurements=measurements, stats=stats)
