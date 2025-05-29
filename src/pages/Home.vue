<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const navigateToForm = () => {
  window.scrollTo({
    top: 0,
    behavior: 'smooth'
  })
  setTimeout(() => {
    router.push('/formulario')
  }, 300)
}
</script>

<template>
  <div class="home-hero">
    <div class="home-text">
      <h1>Análise de problemas mentais<br>baseado em dados comportamentais</h1>
      <p class="intro-text">
        Este questionário foi desenvolvido para ajudar na análise de comportamentos associados à depressão e à ansiedade. Ao preencher, você nos ajuda a criar formas de saúde mental automatizada. Aqui, você poderá refletir sobre seus sentimentos, atitudes e perceber se há algum distúrbio, facilitando possíveis cuidados com a sua saúde.
        <br><br>
        As respostas são anônimas, mas podem auxiliar em um ponto de partida importante para compreender melhor o seu estado emocional. Preencha com sinceridade, buscando autoconhecimento, e lembre-se: não hesite em procurar ajuda especializada caso sinta diferente e tenha o apoio emocional, passo a passo, para se sentir melhor.
      </p>
    </div>
    <div class="home-image">
      <!-- Imagem SVG minimalista -->
      <svg width="180" height="180" viewBox="0 0 180 180" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="160" height="160" rx="32" fill="#f0f2f5" stroke="#3498db" stroke-width="3"/>
        <path d="M90 60c-15 0-27 12-27 27 0 18 27 33 27 33s27-15 27-33c0-15-12-27-27-27zm0 36a9 9 0 1 1 0-18 9 9 0 0 1 0 18z" fill="#3498db"/>
      </svg>
    </div>
  </div>

  <!-- Seção de anonimato e segurança -->
  <section class="anonimato-section">
    <span class="anonimato-icon" aria-label="Segurança e anonimato">🔒</span>
    <span class="anonimato-text">
      Este questionário é <strong>totalmente anônimo</strong>. Nenhuma informação pessoal será coletada.
    </span>
  </section>

  <!-- Seção de objetivos -->
  <section class="objectives-section">
    <h2 class="objectives-title">Qual o objetivo desse questionário de saúde mental?</h2>
    <div class="objectives-cards">
      <div class="objective-card">
        <div class="card-img">
          <font-awesome-icon :icon="['fas', 'magnifying-glass']" size="2x" style="color: #3498db; background: #fff; border-radius: 50%; padding: 10px;" />
        </div>
        <h3>IDENTIFICAR SINAIS PRECOCES</h3>
        <p>Ajudar o usuário a reconhecer possíveis indícios de depressão e ansiedade com base em comportamentos e sentimentos do cotidiano.</p>
      </div>
      <div class="objective-card">
        <div class="card-img">
          <font-awesome-icon :icon="['fas', 'brain']" size="2x" style="color: #3498db; background: #fff; border-radius: 50%; padding: 10px;" />
        </div>
        <h3>INCENTIVAR O AUTOCONHECIMENTO</h3>
        <p>Promover a reflexão sobre o próprio estado emocional e estimular uma maior consciência sobre a saúde mental.</p>
      </div>
      <div class="objective-card">
        <div class="card-img">
          <font-awesome-icon :icon="['fas', 'flag']" size="2x" style="color: #3498db; background: #fff; border-radius: 50%; padding: 10px;" />
        </div>
        <h3>OFERECER UM PONTO DE PARTIDA</h3>
        <p>Servir como uma ferramenta inicial para que o usuário considere procurar apoio psicológico, se necessário.</p>
      </div>
    </div>
  </section>

  <!-- Seção Informativa sobre Depressão e Ansiedade -->
  <section class="info-section">
    <h2 class="info-title">Entendendo a Saúde Mental</h2>
    <div class="info-cards">
      <div class="info-card">
        <h3>O que é Depressão?</h3>
        <p>A depressão é um transtorno mental que afeta o humor, causando tristeza persistente e perda de interesse em atividades. Pode afetar como você se sente, pensa e se comporta, levando a uma variedade de problemas emocionais e físicos.</p>
        <ul class="info-list">
          <li>Sentimentos persistentes de tristeza</li>
          <li>Perda de interesse em atividades</li>
          <li>Alterações no sono e apetite</li>
          <li>Dificuldade de concentração</li>
          <li>Sentimentos de desesperança</li>
        </ul>
      </div>
      <div class="info-card">
        <h3>O que é Ansiedade?</h3>
        <p>A ansiedade é uma resposta natural do corpo ao estresse, mas quando excessiva, pode se tornar um transtorno. Caracteriza-se por preocupação e medo intensos, excessivos e persistentes sobre situações cotidianas.</p>
        <ul class="info-list">
          <li>Preocupação excessiva</li>
          <li>Inquietação e tensão</li>
          <li>Dificuldade de relaxar</li>
          <li>Problemas de concentração</li>
          <li>Sintomas físicos (taquicardia, sudorese)</li>
        </ul>
      </div>
    </div>
  </section>

  <!-- Depoimentos/Frases de Impacto -->
  <section class="depoimentos-section">
    <h2 class="depoimentos-title">Palavras que Inspiram</h2>
    <div class="depoimentos-list">
      <blockquote>"Cuidar da mente é tão importante quanto cuidar do corpo."</blockquote>
      <blockquote>"Buscar ajuda é um ato de coragem, não de fraqueza."</blockquote>
      <blockquote>"Você não está sozinho. Falar é o primeiro passo."</blockquote>
    </div>
  </section>

  <!-- Como Funciona -->
  <section class="como-funciona-section">
    <h2 class="como-funciona-title">Como funciona nossa IA?</h2>
    <div class="como-funciona-content">
      <p class="como-funciona-intro">
        Desenvolvida como parte de um projeto de pesquisa acadêmica, nossa Inteligência Artificial foi treinada para analisar padrões comportamentais e identificar possíveis indicadores de saúde mental. O sistema utiliza algoritmos avançados de machine learning para processar suas respostas e fornecer insights personalizados.
      </p>
      <div class="como-funciona-steps">
        <div class="step">
          <div class="step-icon">🤖</div>
          <div class="step-desc">
            <h4>Análise por IA</h4>
            <p>Nossa IA analisa suas respostas usando algoritmos de machine learning desenvolvidos especificamente para este projeto.</p>
          </div>
        </div>
        <div class="step">
          <div class="step-icon">📊</div>
          <div class="step-desc">
            <h4>Processamento de Dados</h4>
            <p>O sistema processa os dados comportamentais e identifica padrões relevantes para sua saúde mental.</p>
          </div>
        </div>
        <div class="step">
          <div class="step-icon">🎯</div>
          <div class="step-desc">
            <h4>Resultados Personalizados</h4>
            <p>Você recebe um diagnóstico preliminar e recomendações específicas baseadas em sua situação.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Indicadores/Dados -->
  <section class="indicadores-section">
    <div class="indicador-card">
      <span class="indicador-num">1 em cada 4</span>
      <span class="indicador-desc">brasileiros apresenta sintomas de ansiedade, segundo a OMS.</span>
    </div>
  </section>

  <!-- Links Úteis e Recursos -->
  <section class="recursos-section">
    <h2 class="recursos-title">Recursos e Ajuda</h2>
    <ul class="recursos-list">
      <li><a href="https://www.cvv.org.br/" target="_blank" rel="noopener">CVV - Centro de Valorização da Vida</a></li>
      <li><a href="https://www.gov.br/saude/pt-br/composicao/saes/desmad/raps/caps" target="_blank" rel="noopener">CAPS - Centros de Atenção Psicossocial</a></li>
      <li><a href="https://www.unicef.org/brazil/media/16126/file/saude-mental-de-adolescentes-e-jovens.pdf" target="_blank" rel="noopener">UNICEF - Saúde Mental</a></li>
    </ul>
  </section>

  <!-- Seção de Chamada para Ação -->
  <section class="cta-section">
    <div class="cta-content">
      <h2 class="cta-title">Pronto para começar sua jornada de autoconhecimento?</h2>
      <p class="cta-text">
        O questionário é rápido, anônimo e pode ser o primeiro passo para uma vida mais equilibrada.
        Reserve alguns minutos do seu dia para cuidar da sua saúde mental.
      </p>
      <div class="cta-features">
        <div class="cta-feature">
          <span class="feature-icon">⏱️</span>
          <span class="feature-text">Apenas 5 minutos</span>
        </div>
        <div class="cta-feature">
          <span class="feature-icon">🔒</span>
          <span class="feature-text">100% Anônimo</span>
        </div>
        <div class="cta-feature">
          <span class="feature-icon">📊</span>
          <span class="feature-text">Resultado Imediato</span>
        </div>
      </div>
      <button @click="navigateToForm" class="cta-button-large">Fazer o Teste Agora</button>
    </div>
  </section>
</template>

<style scoped>
.home-hero, .objectives-section {
  opacity: 0;
  transform: translateY(40px);
  animation: fadeInUp 0.9s cubic-bezier(.23,1.02,.32,1) forwards;
}
.home-hero {
  animation-delay: 0.1s;
  background: linear-gradient(120deg, #e3f0fc 0%, #bfe0f7 100%);
  border-radius: 18px;
  box-shadow: 0 4px 32px rgba(52,152,219,0.10);

}
.objectives-section {
  animation-delay: 0.4s;
  background: linear-gradient(120deg, #bfe0f7 0%, #e3f0fc 100%);
}
@keyframes fadeInUp {
  to {
    opacity: 1;
    transform: none;
  }
}

.home-hero {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 70vh;
  gap: 2rem;
  max-width: 1100px;
  margin: 0 auto;
  padding: 2rem 1rem;
}

.home-text {
  flex: 1;
  max-width: 520px;
}

.home-text h1 {
  font-size: 2rem;
  font-weight: 700;
  color: #1a3a4a;
  margin-bottom: 1.5rem;
  line-height: 1.2;
}

.intro-text {
  color: #2c3e50;
  font-size: 1.08rem;
  margin-bottom: 2.5rem;
  line-height: 1.7;
}

.cta-button, .cta-button-large {
  cursor: pointer;
  border: none;
  outline: none;
}

.cta-button {
  display: inline-block;
  background: linear-gradient(90deg, #3498db 0%, #217dbb 100%);
  color: white;
  padding: 1rem 2.5rem;
  border-radius: 8px;
  text-decoration: none;
  font-size: 1.1rem;
  font-weight: 500;
  transition: all 0.3s ease;
  box-shadow: 0 4px 16px rgba(52,152,219,0.18);
}

.cta-button:hover {
  background: linear-gradient(90deg, #217dbb 0%, #3498db 100%);
  transform: translateY(-2px);
  box-shadow: 0 8px 32px rgba(52,152,219,0.25);
}

.cta-button-large {
  display: inline-block;
  background: white;
  color: #3498db;
  padding: 1.2rem 3rem;
  border-radius: 50px;
  text-decoration: none;
  font-size: 1.2rem;
  font-weight: 600;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(0,0,0,0.2);
}

.cta-button-large:hover {
  transform: translateY(-3px);
  box-shadow: 0 6px 20px rgba(0,0,0,0.3);
  background: #f8f9fa;
}

.home-image {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  min-width: 220px;
}

/* Seção de objetivos */
.objectives-section {
  border-radius: 0;
  margin: 3rem 0 0 0;
  padding: 4rem 2vw 4rem 2vw;
  width: 100vw;
  box-shadow: 0 2px 12px rgba(52,152,219,0.07);
  position: relative;
  left: 50%;
  right: 50%;
  margin-left: -50vw;
  margin-right: -50vw;
}

.objectives-title {
  text-align: center;
  font-size: 1.25rem;
  font-weight: 600;
  color: #1a3a4a;
  margin-bottom: 2.5rem;
  position: relative;
}

.objectives-title::before {
  content: "💙";
  margin-right: 0.5rem;
  font-size: 1.3rem;
  vertical-align: middle;
}

.objectives-cards {
  display: flex;
  gap: 2rem;
  justify-content: center;
  flex-wrap: wrap;
}

.objective-card {
  background: #f5f8fa;
  border: 2px solid #3498db;
  border-radius: 10px;
  box-shadow: 0 4px 16px rgba(52,152,219,0.10);
  padding: 1.5rem 1.2rem 1.8rem 1.2rem;
  max-width: 320px;
  min-width: 260px;
  flex: 1 1 260px;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  transition: transform 0.3s cubic-bezier(.23,1.02,.32,1), box-shadow 0.3s cubic-bezier(.23,1.02,.32,1);
}

.objective-card:hover {
  transform: translateY(-10px) scale(1.03);
  box-shadow: 0 8px 32px rgba(52,152,219,0.18);
  z-index: 2;
}

.card-img {
  margin-bottom: 1.2rem;
}

.objective-card h3 {
  font-size: 1.08rem;
  font-weight: 700;
  color: #1a3a4a;
  margin-bottom: 0.7rem;
  letter-spacing: 0.5px;
}

.objective-card p {
  color: #2c3e50;
  font-size: 0.98rem;
  line-height: 1.5;
}

/* Depoimentos/Frases de Impacto */
.depoimentos-section {
  background: #e3f0fc;
  padding: 2.5rem 1rem 2rem 1rem;
  margin: 3rem 0 0 0;
  border-radius: 12px;
  box-shadow: 0 4px 16px rgba(52,152,219,0.08);
  max-width: 900px;
  margin-left: auto;
  margin-right: auto;
}

.depoimentos-title {
  text-align: center;
  font-size: 1.18rem;
  font-weight: 600;
  color: #1a3a4a;
  margin-bottom: 1.5rem;
  position: relative;
}

.depoimentos-title::before {
  content: "💙";
  margin-right: 0.5rem;
  font-size: 1.3rem;
  vertical-align: middle;
}

.depoimentos-list {
  display: flex;
  gap: 2rem;
  justify-content: center;
  flex-wrap: wrap;
}

.depoimentos-list blockquote {
  background: #fff;
  border-left: 5px solid #217dbb;
  padding: 1.2rem 1.5rem;
  border-radius: 8px;
  color: #217dbb;
  font-size: 1.05rem;
  font-style: italic;
  max-width: 260px;
  box-shadow: 0 4px 16px rgba(52,152,219,0.10);
}

/* Seção Informativa */
.info-section {
  background: #f8f9fa;
  padding: 4rem 2rem;
  margin: 3rem 0;
  border-radius: 12px;
  box-shadow: 0 4px 16px rgba(52,152,219,0.08);
  max-width: 1200px;
  margin-left: auto;
  margin-right: auto;
}

.info-title {
  text-align: center;
  font-size: 1.5rem;
  font-weight: 600;
  color: #1a3a4a;
  margin-bottom: 2.5rem;
  position: relative;
}

.info-title::before {
  content: "💙";
  margin-right: 0.5rem;
  font-size: 1.3rem;
  vertical-align: middle;
}

.info-cards {
  display: flex;
  gap: 2rem;
  justify-content: center;
  flex-wrap: wrap;
}

.info-card {
  background: white;
  border: 2px solid #3498db;
  border-radius: 12px;
  padding: 2rem;
  flex: 1;
  min-width: 300px;
  max-width: 500px;
  box-shadow: 0 4px 16px rgba(52,152,219,0.10);
}

.info-card h3 {
  color: #1a3a4a;
  font-size: 1.3rem;
  margin-bottom: 1rem;
  font-weight: 600;
}

.info-card p {
  color: #2c3e50;
  font-size: 1.05rem;
  line-height: 1.6;
  margin-bottom: 1.5rem;
}

.info-list {
  list-style: none;
  padding: 0;
}

.info-list li {
  color: #2c3e50;
  font-size: 1rem;
  margin-bottom: 0.8rem;
  padding-left: 1.5rem;
  position: relative;
}

.info-list li::before {
  content: "•";
  color: #3498db;
  position: absolute;
  left: 0;
  font-size: 1.2rem;
}

/* Como Funciona Atualizado */
.como-funciona-section {
  background: #eaf6fb;
  padding: 4rem 2rem;
  margin: 3rem 0;
  border-radius: 12px;
  box-shadow: 0 4px 16px rgba(52,152,219,0.08);
  max-width: 1200px;
  margin-left: auto;
  margin-right: auto;
}

.como-funciona-intro {
  text-align: center;
  color: #2c3e50;
  font-size: 1.1rem;
  line-height: 1.6;
  margin-bottom: 3rem;
  max-width: 800px;
  margin-left: auto;
  margin-right: auto;
}

.como-funciona-steps {
  display: flex;
  gap: 2rem;
  justify-content: center;
  flex-wrap: wrap;
}

.step {
  background: white;
  border: 2px solid #3498db;
  border-radius: 12px;
  padding: 2rem;
  box-shadow: 0 4px 16px rgba(52,152,219,0.10);
  flex: 1;
  min-width: 250px;
  max-width: 350px;
}

.step-icon {
  font-size: 2.5rem;
  margin-bottom: 1rem;
  text-align: center;
}

.step-desc h4 {
  color: #1a3a4a;
  font-size: 1.2rem;
  margin-bottom: 0.8rem;
  font-weight: 600;
  text-align: center;
}

.step-desc p {
  color: #2c3e50;
  font-size: 1rem;
  line-height: 1.5;
  text-align: center;
}

/* Indicadores/Dados */
.indicadores-section {
  display: flex;
  justify-content: center;
  margin: 3rem 0 0 0;
}

.indicador-card {
  background: linear-gradient(90deg, #3498db 0%, #6dd5fa 100%);
  color: #fff;
  border-radius: 12px;
  padding: 2rem 2.5rem;
  font-size: 1.2rem;
  font-weight: 600;
  box-shadow: 0 4px 16px rgba(52,152,219,0.18);
  display: flex;
  flex-direction: column;
  align-items: center;
}

.indicador-num {
  font-size: 2.2rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
}

.indicador-desc {
  font-size: 1rem;
  font-weight: 400;
}

/* Links Úteis e Recursos */
.recursos-section {
  background: #e3f0fc;
  padding: 2.5rem 1rem 2rem 1rem;
  margin: 3rem 0 0 0;
  border-radius: 12px;
  box-shadow: 0 4px 16px rgba(52,152,219,0.08);
  max-width: 900px;
  margin-left: auto;
  margin-right: auto;
}

.recursos-title {
  text-align: center;
  font-size: 1.18rem;
  font-weight: 600;
  color: #1a3a4a;
  margin-bottom: 1.5rem;
  position: relative;
}

.recursos-title::before {
  content: "💙";
  margin-right: 0.5rem;
  font-size: 1.3rem;
  vertical-align: middle;
}

.recursos-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  align-items: center;
  width: 100%;
  padding: 0;
  margin: 0;
}

.recursos-list li {
  width: 100%;
  max-width: 400px;
  text-align: center;
  list-style: none;
  margin: 0 auto;
}

.recursos-list a {
  display: block;
  background: #e3f0fc;
  border-radius: 8px;
  padding: 0.7rem 1rem;
  color: #217dbb;
  font-weight: 500;
  text-decoration: none;
  transition: background 0.2s, color 0.2s;
  width: 100%;
  box-sizing: border-box;
  font-size: 1.05rem;
}

.recursos-list a:hover {
  background: #3498db;
  color: #fff;
}

@media (max-width: 600px) {
  .recursos-list li {
    max-width: 100%;
  }
  .recursos-list a {
    font-size: 0.98rem;
    padding: 0.7rem 0.5rem;
  }
}

/* Seção de anonimato e segurança */
.anonimato-section {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  background: linear-gradient(90deg, #e3f0fc 0%, #bfe0f7 100%);
  border: 2px solid #217dbb;
  border-radius: 10px;
  padding: 1.2rem 2rem;
  margin: 2.5rem auto 2.5rem auto;
  max-width: 600px;
  box-shadow: 0 4px 16px rgba(52,152,219,0.13);
  font-size: 1.08rem;
}

.anonimato-icon {
  font-size: 2rem;
  color: #217dbb;
}

.anonimato-text {
  color: #1a3a4a;
  font-weight: 500;
}

/* Seção de Chamada para Ação */
.cta-section {
  background: linear-gradient(135deg, #3498db 0%, #217dbb 100%);
  margin: 4rem 0 0 0;
  padding: 4rem 2rem;
  border-radius: 0;
  width: 100vw;
  position: relative;
  left: 50%;
  right: 50%;
  margin-left: -50vw;
  margin-right: -50vw;
  color: white;
  text-align: center;
}

.cta-content {
  max-width: 800px;
  margin: 0 auto;
}

.cta-title {
  font-size: 2rem;
  font-weight: 700;
  margin-bottom: 1.5rem;
  color: white;
}

.cta-text {
  font-size: 1.1rem;
  line-height: 1.6;
  margin-bottom: 2.5rem;
  opacity: 0.9;
}

.cta-features {
  display: flex;
  justify-content: center;
  gap: 3rem;
  margin-bottom: 2.5rem;
  flex-wrap: wrap;
}

.cta-feature {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.feature-icon {
  font-size: 1.5rem;
}

.feature-text {
  font-size: 1rem;
  font-weight: 500;
}

@media (max-width: 900px) {
  .home-hero {
    flex-direction: column;
    text-align: center;
    gap: 2.5rem;
  }
  .home-image {
    min-width: 0;
  }
  .home-text {
    max-width: 100%;
  }
  .objectives-cards {
    flex-direction: column;
    gap: 1.5rem;
    align-items: center;
  }
}

@media (max-width: 768px) {
  .cta-section {
    padding: 3rem 1rem;
  }

  .cta-title {
    font-size: 1.5rem;
  }

  .cta-features {
    gap: 1.5rem;
  }

  .cta-button-large {
    padding: 1rem 2rem;
    font-size: 1.1rem;
  }

  .info-cards, .como-funciona-steps {
    flex-direction: column;
    align-items: center;
  }

  .info-card, .step {
    width: 100%;
    max-width: 100%;
  }
}

.como-funciona-title {
  text-align: center;
  font-size: 2rem;
  font-weight: 700;
  color: #1a3a4a;
  margin-bottom: 2rem;
  position: relative;
  padding-bottom: 1rem;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.como-funciona-title::before {
  content: "🤖";
  margin-right: 1rem;
  font-size: 2rem;
  vertical-align: middle;
}

.como-funciona-title::after {
  content: "";
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 100px;
  height: 4px;
  background: linear-gradient(90deg, #3498db, #217dbb);
  border-radius: 2px;
}
</style>
