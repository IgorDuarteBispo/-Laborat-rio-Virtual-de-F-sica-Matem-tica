# Criar arquivo app.js com lógica de app
app_js = """// ================================================================
// LABORATÓRIO VIRTUAL DE FÍSICA MATEMÁTICA - APP.JS
// ================================================================

// Seletores Globais
const navButtons = document.querySelectorAll('.nav-btn');
const sections = document.querySelectorAll('.section');
const homeSection = document.getElementById('homeSection');
const experimentsSection = document.getElementById('experimentsSection');
const calculatorSection = document.getElementById('calculatorSection');
const aboutSection = document.getElementById('aboutSection');
const experimentTitle = document.getElementById('experimentTitle');
const backToHomeBtn = document.getElementById('backToHome');
const controlsPanel = document.getElementById('controls');
const runSimulationBtn = document.getElementById('runSimulation');
const resetSimulationBtn = document.getElementById('resetSimulation');
const canvas = document.getElementById('simulationCanvas');
const ctx = canvas.getContext('2d');
const calculationResults = document.getElementById('calculationResults');

// Acessibilidade
const contrastToggle = document.getElementById('contrastToggle');
const fontIncrease = document.getElementById('fontIncrease');
const fontDecrease = document.getElementById('fontDecrease');
const helpBtn = document.getElementById('helpBtn');
const helpModal = document.getElementById('helpModal');
const closeModal = document.querySelector('.close');

// Calculadora
const calcInput = document.getElementById('calculatorInput');
const calcButtons = document.querySelectorAll('.calc-btn');

// Estado do Aplicativo
let currentExperiment = null;
let fontSizeState = 'font-medium'; // small, medium, large, extra-large

// Utilitários
function clearCanvas() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
}

function setActiveSection(section) {
    sections.forEach(sec => sec.classList.remove('active'));
    section.classList.add('active');
}

function setActiveNav(btn) {
    navButtons.forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
}

function generateControl(id, label, min, max, step, value, unit) {
    const wrapper = document.createElement('div');
    wrapper.className = 'control-item';

    const labelEl = document.createElement('label');
    labelEl.textContent = `${label} (${unit})`;
    labelEl.setAttribute('for', id);

    const range = document.createElement('input');
    range.type = 'range';
    range.id = id;
    range.min = min;
    range.max = max;
    range.step = step;
    range.value = value;

    const valueEl = document.createElement('div');
    valueEl.className = 'control-value';
    valueEl.id = `${id}Value`;
    valueEl.textContent = value;

    range.addEventListener('input', () => {
        valueEl.textContent = range.value;
    });

    wrapper.appendChild(labelEl);
    wrapper.appendChild(range);
    wrapper.appendChild(valueEl);

    return wrapper;
}

function switchExperiment(exp) {
    currentExperiment = exp;
    experimentTitle.textContent = exp.title;
    controlsPanel.innerHTML = '';
    calculationResults.innerHTML = '';
    clearCanvas();

    // Criar controles específicos de cada experimento
    exp.controls.forEach(ctrl => {
        const ctrlEl = generateControl(ctrl.id, ctrl.label, ctrl.min, ctrl.max, ctrl.step, ctrl.value, ctrl.unit);
        controlsPanel.appendChild(ctrlEl);
    });

    setActiveSection(experimentsSection);
    setActiveNav(document.getElementById('experimentsBtn'));
}

// Definição dos Experimentos
const experiments = {
    projectile: {
        title: '🎯 Lançamento de Projéteis',
        controls: [
            { id: 'angle', label: 'Ângulo', min: 10, max: 80, step: 1, value: 45, unit: '°' },
            { id: 'velocity', label: 'Velocidade Inicial', min: 5, max: 50, step: 1, value: 20, unit: 'm/s' }
        ],
        run: () => {
            const angle = parseFloat(document.getElementById('angle').value) * Math.PI / 180;
            const v0 = parseFloat(document.getElementById('velocity').value);
            const g = 9.81;
            const tTotal = (2 * v0 * Math.sin(angle)) / g;
            const range = (v0 * v0 * Math.sin(2 * angle)) / g;
            calculationResults.innerHTML = `Tempo total: ${tTotal.toFixed(2)} s<br> Alcance: ${range.toFixed(2)} m`;

            // Desenhar trajetória
            clearCanvas();
            ctx.strokeStyle = '#ff5722';
            ctx.lineWidth = 2;
            ctx.beginPath();
            ctx.moveTo(0, canvas.height);
            for (let t = 0; t <= tTotal; t += tTotal / 100) {
                const x = (v0 * Math.cos(angle) * t);
                const y = (v0 * Math.sin(angle) * t) - 0.5 * g * t * t;
                const canvasX = (x / range) * canvas.width;
                const canvasY = canvas.height - ((y) / (v0 * v0 / (2 * g))) * canvas.height;
                ctx.lineTo(canvasX, canvasY);
            }
            ctx.stroke();
        },
        reset: () => {
            clearCanvas();
            calculationResults.innerHTML = '';
        }
    },
    freefall: {
        title: '⬇️ Queda Livre',
        controls: [
            { id: 'height', label: 'Altura Inicial', min: 1, max: 100, step: 1, value: 10, unit: 'm' }
        ],
        run: () => {
            const h = parseFloat(document.getElementById('height').value);
            const g = 9.81;
            const t = Math.sqrt((2 * h) / g);
            const v = g * t;
            calculationResults.innerHTML = `Tempo de queda: ${t.toFixed(2)} s<br> Velocidade final: ${v.toFixed(2)} m/s`;

            // Desenhar queda
            clearCanvas();
            ctx.fillStyle = '#2196F3';
            let yPos = 0;
            const interval = setInterval(() => {
                clearCanvas();
                ctx.fillRect(canvas.width/2 - 10, yPos, 20, 20);
                yPos += canvas.height / (t * 60);
                if (yPos >= canvas.height - 20) {
                    clearInterval(interval);
                }
            }, 1000/60);
        },
        reset: () => {
            clearCanvas();
            calculationResults.innerHTML = '';
        }
    },
    kinetic: {
        title: '⚡ Energia Cinética',
        controls: [
            { id: 'mass', label: 'Massa', min: 1, max: 100, step: 1, value: 10, unit: 'kg' },
            { id: 'speed', label: 'Velocidade', min: 1, max: 50, step: 1, value: 10, unit: 'm/s' }
        ],
        run: () => {
            const m = parseFloat(document.getElementById('mass').value);
            const v = parseFloat(document.getElementById('speed').value);
            const ec = 0.5 * m * v * v;
            calculationResults.innerHTML = `Energia Cinética: ${ec.toFixed(2)} J`;

            // Visualização simples
            clearCanvas();
            ctx.fillStyle = '#FFC107';
            const maxEc = 0.5 * 100 * 50 * 50; // valor máximo
            const barWidth = (ec / maxEc) * canvas.width;
            ctx.fillRect(0, canvas.height/2 - 10, barWidth, 20);
        },
        reset: () => {
            clearCanvas();
            calculationResults.innerHTML = '';
        }
    },
    circular: {
        title: '🔄 Movimento Circular',
        controls: [
            { id: 'radius', label: 'Raio', min: 1, max: 20, step: 1, value: 10, unit: 'm' },
            { id: 'speedCircular', label: 'Velocidade', min: 1, max: 20, step: 1, value: 5, unit: 'm/s' },
            { id: 'massCircular', label: 'Massa', min: 1, max: 50, step: 1, value: 5, unit: 'kg' }
        ],
        run: () => {
            const r = parseFloat(document.getElementById('radius').value);
            const v = parseFloat(document.getElementById('speedCircular').value);
            const m = parseFloat(document.getElementById('massCircular').value);
            const f = (m * v * v) / r;
            calculationResults.innerHTML = `Força Centrípeta: ${f.toFixed(2)} N`;

            // Desenhar movimento circular
            clearCanvas();
            const centerX = canvas.width / 2;
            const centerY = canvas.height / 2;
            const scale = 10;
            const drawRadius = r * scale;
            ctx.strokeStyle = '#8E24AA';
            ctx.lineWidth = 2;
            ctx.beginPath();
            ctx.arc(centerX, centerY, drawRadius, 0, Math.PI * 2);
            ctx.stroke();

            let angle = 0;
            const interval = setInterval(() => {
                clearCanvas();
                ctx.strokeStyle = '#8E24AA';
                ctx.beginPath();
                ctx.arc(centerX, centerY, drawRadius, 0, Math.PI * 2);
                ctx.stroke();

                const x = centerX + drawRadius * Math.cos(angle);
                const y = centerY + drawRadius * Math.sin(angle);

                ctx.fillStyle = '#8E24AA';
                ctx.beginPath();
                ctx.arc(x, y, 10, 0, Math.PI * 2);
                ctx.fill();

                angle += v / r * 0.1;
            }, 1000/60);

            // Parar após 1 volta
            setTimeout(() => clearInterval(interval), 2000);
        },
        reset: () => {
            clearCanvas();
            calculationResults.innerHTML = '';
        }
    }
};

// Eventos de navegação
navButtons.forEach(btn => {
    btn.addEventListener('click', () => {
        const target = btn.id;
        setActiveNav(btn);
        switch (target) {
            case 'homeBtn':
                setActiveSection(homeSection);
                break;
            case 'experimentsBtn':
                setActiveSection(homeSection);
                break;
            case 'calculatorBtn':
                setActiveSection(calculatorSection);
                break;
            case 'aboutBtn':
                setActiveSection(aboutSection);
                break;
        }
    });
});

// Clicar em cartões de experimento
const experimentCards = document.querySelectorAll('.experiment-card');
experimentCards.forEach(card => {
    card.addEventListener('click', () => {
        const expId = card.dataset.experiment;
        switchExperiment(experiments[expId]);
    });
});

// Botão Voltar
backToHomeBtn.addEventListener('click', () => {
    setActiveSection(homeSection);
    setActiveNav(document.getElementById('homeBtn'));
});

// Executar e Resetar Simulação
runSimulationBtn.addEventListener('click', () => {
    if (currentExperiment) currentExperiment.run();
});

resetSimulationBtn.addEventListener('click', () => {
    if (currentExperiment) currentExperiment.reset();
});

// Acessibilidade: Contraste
contrastToggle.addEventListener('click', () => {
    document.body.classList.toggle('high-contrast');
});

// Acessibilidade: Fonte
function updateFontSizeState(delta) {
    const sizes = ['font-small', 'font-medium', 'font-large', 'font-extra-large'];
    let index = sizes.indexOf(fontSizeState);
    index = Math.max(0, Math.min(sizes.length - 1, index + delta));
    fontSizeState = sizes[index];
    document.body.classList.remove(...sizes);
    document.body.classList.add(fontSizeState);
}

fontIncrease.addEventListener('click', () => updateFontSizeState(1));
fontDecrease.addEventListener('click', () => updateFontSizeState(-1));

// Modal de ajuda
helpBtn.addEventListener('click', () => {
    helpModal.classList.add('show');
});

closeModal.addEventListener('click', () => helpModal.classList.remove('show'));
window.addEventListener('click', e => {
    if (e.target === helpModal) helpModal.classList.remove('show');
});

// Calculadora
let calcExpression = '';
function updateCalcDisplay() {
    calcInput.value = calcExpression;
}

calcButtons.forEach(btn => {
    btn.addEventListener('click', () => {
        const value = btn.textContent.trim();
        if (btn.classList.contains('number')) {
            calcExpression += value;
        } else if (btn.classList.contains('operator')) {
            calcExpression += ' ' + value + ' ';
        } else if (btn.classList.contains('equals')) {
            try {
                // Substituir símbolos
                const expr = calcExpression.replace(/×/g, '*').replace(/÷/g, '/').replace(/π/g, 'Math.PI').replace(/√/g, 'Math.sqrt');
                calcExpression = eval(expr).toString();
            } catch {
                calcExpression = 'Erro';
            }
        } else if (btn.classList.contains('clear')) {
            calcExpression = '';
        } else if (btn.classList.contains('scientific')) {
            switch (value) {
                case 'sin': calcExpression += ' Math.sin('; break;
                case 'cos': calcExpression += ' Math.cos('; break;
                case 'tan': calcExpression += ' Math.tan('; break;
                case 'π': calcExpression += ' π '; break;
                case '√': calcExpression += ' √('; break;
                case 'x²': calcExpression += '**2'; break;
            }
        } else if (value === '±') {
            calcExpression = calcExpression ? `-(${calcExpression})` : '';
        } else if (value === '.') {
            calcExpression += '.';
        }
        updateCalcDisplay();
    });
});

// Inicialização
setActiveSection(homeSection);
setActiveNav(document.getElementById('homeBtn'));
updateCalcDisplay();
"""

with open("app.js", "w", encoding="utf-8") as f:
    f.write(app_js)

print("✅ app.js criado com sucesso!")