// URL dinâmica apontando para o endpoint da API
const API_URL = window.location.hostname === 'localhost' 
  ? 'http://localhost:8000/api/v1' 
  : '/api/v1';

document.addEventListener('DOMContentLoaded', () => {
  checkApiHealth();
  fetchVisitors();

  document.getElementById('visitor-form').addEventListener('submit', handleRegister);
});

async function checkApiHealth() {
  const badge = document.getElementById('status-badge');
  try {
    const res = await fetch(`${API_URL}/health`);
    if (res.ok) {
      badge.textContent = 'API Online';
      badge.className = 'badge online';
    } else {
      throw new Error();
    }
  } catch {
    badge.textContent = 'API Offline (Modo Dev)';
    badge.className = 'badge offline';
  }
}

async function fetchVisitors() {
  try {
    const res = await fetch(`${API_URL}/visitors`);
    if (!res.ok) return;
    const visitors = await res.json();
    renderTable(visitors);
  } catch (err) {
    console.warn('Não foi possível carregar a lista de visitantes:', err);
  }
}

async function handleRegister(e) {
  e.preventDefault();
  const formData = new FormData(e.target);
  const payload = Object.fromEntries(formData.entries());

  try {
    const res = await fetch(`${API_URL}/visitors`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    if (res.ok) {
      e.target.reset();
      fetchVisitors();
    }
  } catch (err) {
    console.error('Erro ao registrar visitante:', err);
  }
}

function renderTable(visitors) {
  const tbody = document.getElementById('visitors-list');
  tbody.innerHTML = visitors.map(v => `
    <tr>
      <td>${v.nome}</td>
      <td>${v.documento}</td>
      <td>${v.unidade}</td>
      <td>${new Date(v.entrada).toLocaleTimeString()}</td>
      <td>
        <button class="btn-checkout" onclick="checkout('${v.id}')">Registrar Saída</button>
      </td>
    </tr>
  `).join('');
}