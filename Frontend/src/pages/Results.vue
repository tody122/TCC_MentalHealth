<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const resultado = ref(null)
const loading = ref(true)

onMounted(() => {
  // Simulando um resultado para demonstração
  setTimeout(() => {
    resultado.value = {
      tracos: 'Apresenta traços de ansiedade e depressão',
      recomendacoes: [
        'Considere conversar com um profissional de saúde mental',
        'Mantenha uma rotina regular de exercícios físicos',
        'Pratique técnicas de relaxamento e mindfulness',
        'Mantenha contato regular com amigos e familiares'
      ],
      fatores_identificados: [
        'Estresse relacionado à situação financeira',
        'Histórico familiar de problemas de saúde mental',
        'Baixo nível de satisfação com a vida atual'
      ]
    }
    loading.value = false
  }, 2000)
})

const voltarParaInicio = () => {
  router.push('/')
}
</script>

<template>
  <div class="results-container">
    <div v-if="loading" class="loading-container">
      <div class="loading-spinner"></div>
      <p>Analisando suas respostas...</p>
    </div>

    <div v-else class="results-content">
      <div class="results-header">
        <h1>Resultado da Análise</h1>
        <p class="subtitle">Baseado nas suas respostas, geramos o seguinte diagnóstico preliminar</p>
      </div>

      <div class="results-grid">
        <!-- Traços Identificados -->
        <div class="result-card traits">
          <h2>Traços Identificados</h2>
          <div class="traits-indicator">
            {{ resultado.tracos }}
          </div>
        </div>

        <!-- Fatores Identificados -->
        <div class="result-card factors">
          <h2>Fatores Identificados</h2>
          <ul class="factors-list">
            <li v-for="(fator, index) in resultado.fatores_identificados" :key="index">
              <span class="factor-icon">•</span>
              {{ fator }}
            </li>
          </ul>
        </div>

        <!-- Recomendações -->
        <div class="result-card recommendations">
          <h2>Recomendações</h2>
          <ul class="recommendations-list">
            <li v-for="(recomendacao, index) in resultado.recomendacoes" :key="index">
              <span class="recommendation-icon">✓</span>
              {{ recomendacao }}
            </li>
          </ul>
        </div>
      </div>

      <div class="results-footer">
        <div class="disclaimer">
          <p>⚠️ Este é um diagnóstico preliminar baseado em suas respostas. Para um diagnóstico completo e tratamento adequado, consulte um profissional de saúde mental.</p>
        </div>
        <button @click="voltarParaInicio" class="back-button">
          Voltar para o Início
        </button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.results-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
  background-color: #f8f9fa;
}

.loading-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 400px;
}

.loading-container p {
  color: #1a3a4a;
  font-size: 1.2rem;
  font-weight: 500;
}

.loading-spinner {
  width: 50px;
  height: 50px;
  border: 5px solid #e3f0fc;
  border-top: 5px solid #217dbb;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin-bottom: 1rem;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.results-header {
  text-align: center;
  margin-bottom: 3rem;
  background-color: white;
  padding: 2rem;
  border-radius: 16px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.results-header h1 {
  color: #1a3a4a;
  font-size: 2.5rem;
  margin-bottom: 1rem;
  font-weight: 700;
}

.subtitle {
  color: #2c3e50;
  font-size: 1.2rem;
  font-weight: 500;
}

.results-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  margin-bottom: 3rem;
}

.result-card {
  background: white;
  border-radius: 16px;
  padding: 2rem;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.result-card h2 {
  color: #1a3a4a;
  font-size: 1.5rem;
  margin-bottom: 1.5rem;
  text-align: center;
  font-weight: 600;
}

.traits {
  text-align: center;
}

.traits-indicator {
  font-size: 1.8rem;
  font-weight: 600;
  padding: 1.5rem;
  border-radius: 8px;
  margin-bottom: 1.5rem;
  background-color: #f0f7ff;
  color: #1a3a4a;
  border: 2px solid #217dbb;
}

.factors-list, .recommendations-list {
  list-style: none;
  padding: 0;
}

.factors-list li, .recommendations-list li {
  display: flex;
  align-items: center;
  margin-bottom: 1rem;
  padding: 1rem;
  background-color: #f0f7ff;
  border-radius: 8px;
  color: #1a3a4a;
  font-size: 1.1rem;
  line-height: 1.4;
}

.factor-icon, .recommendation-icon {
  margin-right: 1rem;
  color: #217dbb;
  font-weight: bold;
  font-size: 1.2rem;
}

.disclaimer {
  background-color: #fff3cd;
  border: 1px solid #ffeeba;
  color: #856404;
  padding: 1.5rem;
  border-radius: 8px;
  margin-bottom: 2rem;
  text-align: center;
  font-size: 1.1rem;
  font-weight: 500;
  line-height: 1.5;
}

.back-button {
  background-color: #217dbb;
  color: white;
  padding: 1rem 2rem;
  border: none;
  border-radius: 8px;
  font-size: 1.2rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  display: block;
  margin: 0 auto;
}

.back-button:hover {
  background-color: #1a6aa3;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(33, 125, 187, 0.2);
}

@media (max-width: 768px) {
  .results-grid {
    grid-template-columns: 1fr;
  }

  .results-header h1 {
    font-size: 2rem;
  }

  .factors-list li, .recommendations-list li {
    font-size: 1rem;
  }

  .traits-indicator {
    font-size: 1.5rem;
    padding: 1rem;
  }
}
</style>
