// Lógica de la página principal: unidades, cálculo de IMC y llamada a la API.

let currentUnits = 'metric';

function setUnits(units, btnEl) {
  currentUnits = units;
  document.querySelectorAll('.unit-btn').forEach(b => b.classList.remove('active'));
  btnEl.classList.add('active');
  document.getElementById('pesoUnit').textContent = units === 'metric' ? 'kg' : 'lb';
  document.getElementById('alturaUnit').textContent = units === 'metric' ? 'm' : 'in';
  document.getElementById('peso').placeholder = units === 'metric' ? '70' : '154';
  document.getElementById('altura').placeholder = units === 'metric' ? '1.70' : '67';
}

function imcToPercent(imc) {
  // Mapea el rango de IMC 10-45 a un porcentaje 0-100 para la barra visual.
  const min = 10, max = 45;
  return Math.min(Math.max(((imc - min) / (max - min)) * 100, 2), 98);
}

async function calcular() {
  const pesoVal = parseFloat(document.getElementById('peso').value);
  const alturaVal = parseFloat(document.getElementById('altura').value);
  const edad = parseInt(document.getElementById('edad').value, 10);
  const sexo = document.getElementById('sexo').value;

  if (!pesoVal || !alturaVal || !edad) {
    alert('Por favor completa peso, altura y edad.');
    return;
  }

  // Convertir a métrico si el usuario está usando unidades imperiales.
  let peso = pesoVal;
  let altura = alturaVal;
  if (currentUnits === 'imperial') {
    peso = pesoVal * 0.453592;
    altura = alturaVal * 0.0254;
  }

  const btn = document.getElementById('btnCalcular');
  btn.classList.add('loading');
  btn.textContent = 'Calculando...';

  const resultCard = document.getElementById('resultCard');
  resultCard.style.display = 'block';
  document.getElementById('aiText').innerHTML = `
    <span class="ai-loading">
      <span>Generando recomendación personalizada</span>
      <span class="dots"><span>.</span><span>.</span><span>.</span></span>
    </span>`;

  resultCard.scrollIntoView({ behavior: 'smooth', block: 'start' });

  try {
    const res = await fetch('/calcular', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ peso, altura, edad, sexo }),
    });

    const data = await res.json();

    document.getElementById('imcNumber').textContent = data.imc;
    document.getElementById('imcCategoria').textContent = data.categoria;
    document.getElementById('resultHeader').style.background = data.color;

    const pct = imcToPercent(data.imc);
    document.getElementById('scaleMarker').style.left = pct + '%';

    document.getElementById('aiText').className = 'ai-text';
    document.getElementById('aiText').textContent = data.recomendacion;
  } catch (err) {
    document.getElementById('aiText').textContent =
      'Error al conectar con el servidor. Verifica que Flask esté corriendo.';
  }

  btn.classList.remove('loading');
  btn.textContent = 'Calcular IMC';
}

document.addEventListener('keydown', (e) => {
  if (e.key === 'Enter') calcular();
});

// Auto-formateo del campo altura: convierte cm a metros y coma a punto.
// Los listeners se registran UNA sola vez al cargar la página (antes se
// registraban dentro de calcular(), acumulándose en cada clic).
document.addEventListener('DOMContentLoaded', () => {
  const alturaInput = document.getElementById('altura');
  if (!alturaInput) return;

  alturaInput.addEventListener('blur', function (e) {
    const valor = parseFloat(e.target.value.toString().replace(',', '.'));
    if (currentUnits === 'metric' && valor > 3) {
      e.target.value = (valor / 100).toFixed(2);
    }
  });

  alturaInput.addEventListener('input', function (e) {
    const value = e.target.value;
    if (value.length === 3 && !value.includes('.') && !value.includes(',')) {
      e.target.value = (value / 100).toFixed(2);
    }
  });

  alturaInput.addEventListener('beforeinput', function (e) {
    if (e.data === ',') {
      e.preventDefault();
      const start = this.selectionStart;
      const end = this.selectionEnd;
      this.value = this.value.substring(0, start) + '.' + this.value.substring(end);
      this.selectionStart = this.selectionEnd = start + 1;
    }
  });
});
