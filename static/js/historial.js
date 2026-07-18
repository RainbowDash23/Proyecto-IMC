// Renderiza las gráficas de historial usando Chart.js.
// Espera que `window.categoriasData` y `window.medicionesData` ya existan
// (se definen inline en historial.html a partir de los datos de Jinja).

document.addEventListener('DOMContentLoaded', () => {
  const categorias = window.categoriasData || [];
  const mediciones = window.medicionesData || [];

  const pieCanvas = document.getElementById('pieChart');
  const lineCanvas = document.getElementById('lineChart');
  if (!pieCanvas || !lineCanvas) return;

  new Chart(pieCanvas.getContext('2d'), {
    type: 'doughnut',
    data: {
      labels: categorias.map((c) => c.categoria),
      datasets: [{
        data: categorias.map((c) => c.cantidad),
        backgroundColor: ['#60a5fa', '#4ade80', '#fbbf24', '#f97316', '#f87171', '#dc2626'],
        borderWidth: 2,
        borderColor: '#fff',
      }],
    },
    options: {
      responsive: true,
      plugins: {
        legend: {
          position: 'bottom',
          labels: { font: { family: 'Open Sans', size: 11 }, padding: 10 },
        },
      },
    },
  });

  const last20 = [...mediciones].reverse().slice(0, 20);

  new Chart(lineCanvas.getContext('2d'), {
    type: 'line',
    data: {
      labels: last20.map((m) => m.fecha.split(' ')[0]),
      datasets: [{
        label: 'Historial IMC',
        data: last20.map((m) => m.imc),
        borderColor: '#2d6a4f',
        backgroundColor: 'rgba(45,106,79,0.08)',
        borderWidth: 2.5,
        pointBackgroundColor: last20.map((m) =>
          m.imc < 18.5 ? '#60a5fa' : m.imc < 25 ? '#4ade80' : m.imc < 30 ? '#fbbf24' : '#f87171'
        ),
        pointRadius: 5,
        tension: 0.3,
        fill: true,
      }],
    },
    options: {
      responsive: true,
      plugins: { legend: { display: false } },
      scales: {
        y: {
          min: 10,
          max: 45,
          grid: { color: 'rgba(0,0,0,0.05)' },
          ticks: { font: { family: 'Open Sans', size: 10 } },
        },
        x: {
          ticks: { font: { family: 'Open Sans', size: 10 }, maxRotation: 35 },
          grid: { display: false },
        },
      },
    },
  });
});
