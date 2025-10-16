# Criar o arquivo index.html completo com JavaScript embutido
index_html = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Laboratório Virtual de Física Matemática</title>
    <link rel="stylesheet" href="style.css">
    <meta name="description" content="Jogo educativo que integra matemática e física através de tecnologias assistivas">
</head>
<body>
    <!-- Header Principal -->
    <header class="header">
        <div class="header-content">
            <h1 class="title">🔬 Laboratório Virtual de Física Matemática</h1>
            <p class="subtitle">Tecnologia Assistiva para Educação Inclusiva</p>
            <div class="accessibility-toolbar">
                <button id="contrastToggle" class="accessibility-btn" title="Alternar Alto Contraste">🎨 Contraste</button>
                <button id="fontIncrease" class="accessibility-btn" title="Aumentar Fonte">🔍+ Fonte</button>
                <button id="fontDecrease" class="accessibility-btn" title="Diminuir Fonte">🔍- Fonte</button>
                <button id="helpBtn" class="accessibility-btn" title="Ajuda">❓ Ajuda</button>
            </div>
        </div>
    </header>

    <!-- Menu de Navegação -->
    <nav class="main-nav">
        <div class="nav-container">
            <button id="homeBtn" class="nav-btn active">🏠 Início</button>
            <button id="experimentsBtn" class="nav-btn">🔬 Experimentos</button>
            <button id="calculatorBtn" class="nav-btn">🧮 Calculadora</button>
            <button id="aboutBtn" class="nav-btn">ℹ️ Sobre</button>
        </div>
    </nav>

    <!-- Container Principal -->
    <main class="main-container">
        
        <!-- Tela Inicial -->
        <section id="homeSection" class="section active">
            <div class="welcome-card">
                <h2>Bem-vindo ao Laboratório Virtual!</h2>
                <p>Explore 4 experimentos que integram <strong>matemática e física</strong> de forma visual e interativa.</p>
                
                <div class="experiments-grid">
                    <div class="experiment-card" data-experiment="projectile">
                        <div class="experiment-icon">🎯</div>
                        <h3>Lançamento de Projéteis</h3>
                        <p>Trigonometria + Movimento Parabólico</p>
                        <div class="formula">y = v₀sen(θ)t - ½gt²</div>
                    </div>
                    
                    <div class="experiment-card" data-experiment="freefall">
                        <div class="experiment-icon">⬇️</div>
                        <h3>Queda Livre</h3>
                        <p>Equações 2º Grau + Gravidade</p>
                        <div class="formula">h = ½gt²</div>
                    </div>
                    
                    <div class="experiment-card" data-experiment="kinetic">
                        <div class="experiment-icon">⚡</div>
                        <h3>Energia Cinética</h3>
                        <p>Potências + Energia</p>
                        <div class="formula">Ec = ½mv²</div>
                    </div>
                    
                    <div class="experiment-card" data-experiment="circular">
                        <div class="experiment-icon">🔄</div>
                        <h3>Movimento Circular</h3>
                        <p>Círculo + Força Centrípeta</p>
                        <div class="formula">F = mv²/r</div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Tela de Experimentos -->
        <section id="experimentsSection" class="section">
            <div class="experiment-container">
                <div class="experiment-header">
                    <h2 id="experimentTitle">Selecione um Experimento</h2>
                    <button id="backToHome" class="back-btn">← Voltar</button>
                </div>
                
                <div class="experiment-content">
                    <div class="controls-panel">
                        <h3>Controles</h3>
                        <div class="control-group" id="controls">
                            <!-- Controles dinâmicos serão inseridos aqui -->
                        </div>
                        <button id="runSimulation" class="run-btn">▶️ Executar Simulação</button>
                        <button id="resetSimulation" class="reset-btn">🔄 Reiniciar</button>
                    </div>
                    
                    <div class="visualization-panel">
                        <canvas id="simulationCanvas" width="600" height="400"></canvas>
                        <div id="results" class="results-panel">
                            <h3>Resultados</h3>
                            <div id="calculationResults"></div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Calculadora -->
        <section id="calculatorSection" class="section">
            <div class="calculator-container">
                <h2>🧮 Calculadora Científica</h2>
                <div class="calculator">
                    <div class="calculator-display">
                        <input type="text" id="calculatorInput" readonly>
                    </div>
                    <div class="calculator-buttons">
                        <button class="calc-btn clear">C</button>
                        <button class="calc-btn">±</button>
                        <button class="calc-btn">%</button>
                        <button class="calc-btn operator">÷</button>
                        
                        <button class="calc-btn number">7</button>
                        <button class="calc-btn number">8</button>
                        <button class="calc-btn number">9</button>
                        <button class="calc-btn operator">×</button>
                        
                        <button class="calc-btn number">4</button>
                        <button class="calc-btn number">5</button>
                        <button class="calc-btn number">6</button>
                        <button class="calc-btn operator">-</button>
                        
                        <button class="calc-btn number">1</button>
                        <button class="calc-btn number">2</button>
                        <button class="calc-btn number">3</button>
                        <button class="calc-btn operator">+</button>
                        
                        <button class="calc-btn number zero">0</button>
                        <button class="calc-btn">.</button>
                        <button class="calc-btn equals">=</button>
                        
                        <button class="calc-btn scientific">sin</button>
                        <button class="calc-btn scientific">cos</button>
                        <button class="calc-btn scientific">tan</button>
                        <button class="calc-btn scientific">π</button>
                        <button class="calc-btn scientific">√</button>
                        <button class="calc-btn scientific">x²</button>
                    </div>
                </div>
            </div>
        </section>

        <!-- Sobre -->
        <section id="aboutSection" class="section">
            <div class="about-container">
                <h2>ℹ️ Sobre o Projeto</h2>
                <div class="about-content">
                    <div class="about-card">
                        <h3>🎯 Objetivo</h3>
                        <p>Integrar conceitos de matemática e física através de simulações visuais interativas, utilizando tecnologias assistivas para promover educação inclusiva.</p>
                    </div>
                    
                    <div class="about-card">
                        <h3>♿ Acessibilidade</h3>
                        <ul>
                            <li>Alto contraste para baixa visão</li>
                            <li>Fontes ajustáveis</li>
                            <li>Navegação por teclado</li>
                            <li>Interface responsiva</li>
                            <li>Feedback visual claro</li>
                        </ul>
                    </div>
                    
                    <div class="about-card">
                        <h3>🎓 Contexto Educacional</h3>
                        <p><strong>Disciplina:</strong> Tecnologias Integradas à Educação</p>
                        <p><strong>Foco:</strong> Tecnologia Assistiva</p>
                        <p><strong>Público:</strong> Ensino Fundamental II e Médio</p>
                        <p><strong>Área:</strong> STEM (Ciências, Tecnologia, Engenharia, Matemática)</p>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <!-- Modal de Ajuda -->
    <div id="helpModal" class="modal">
        <div class="modal-content">
            <span class="close">&times;</span>
            <h2>📖 Como Usar</h2>
            <div class="help-content">
                <h3>🎮 Navegação:</h3>
                <ul>
                    <li><strong>Tab/Shift+Tab:</strong> Navegar entre elementos</li>
                    <li><strong>Enter/Space:</strong> Ativar botões</li>
                    <li><strong>Setas:</strong> Ajustar valores nos controles</li>
                </ul>
                
                <h3>🔬 Experimentos:</h3>
                <ul>
                    <li>Escolha um experimento na tela inicial</li>
                    <li>Ajuste os parâmetros usando os controles</li>
                    <li>Clique em "Executar Simulação"</li>
                    <li>Observe a animação e os resultados</li>
                </ul>
                
                <h3>♿ Acessibilidade:</h3>
                <ul>
                    <li><strong>Contraste:</strong> Alterna modo de alto contraste</li>
                    <li><strong>Fonte:</strong> Aumenta/diminui tamanho do texto</li>
                    <li><strong>Ajuda:</strong> Mostra estas instruções</li>
                </ul>
            </div>
        </div>
    </div>

    <script src="app.js"></script>
</body>
</html>"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(index_html)

print("✅ index.html criado com sucesso!")