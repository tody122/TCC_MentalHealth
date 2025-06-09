<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useRespostasStore } from '../stores/respostas'

const router = useRouter()
const respostasStore = useRespostasStore()
const resultado = ref(null)

const getGrauGravidade = (probabilidade) => {
  const prob = probabilidade * 100;
  if (prob <= 20) return {
    titulo: "Baixa probabilidade de sintomas relacionados",
    recomendacao: "Ainda que os indicadores sejam baixos, é importante manter hábitos saudáveis e cuidar da saúde mental. Em caso de dúvidas ou mudanças no bem-estar, a orientação de um profissional qualificado é sempre recomendada."
  };
  if (prob <= 40) return {
    titulo: "Atenção inicial necessária",
    recomendacao: "Os dados sugerem uma atenção inicial. Mesmo em estágios leves, procurar um profissional qualificado pode oferecer suporte e esclarecimento adequados."
  };
  if (prob <= 60) return {
    titulo: "Sinais que merecem atenção",
    recomendacao: "Este resultado aponta sinais que merecem atenção. A avaliação com um profissional da saúde mental é altamente recomendada para compreender melhor a situação e buscar orientações adequadas."
  };
  if (prob <= 80) return {
    titulo: "Nível significativo de indícios",
    recomendacao: "A análise indica um nível significativo de possíveis indícios. Buscar o acompanhamento de um profissional qualificado é uma medida essencial para cuidado e prevenção."
  };
  return {
    titulo: "Fortes indícios de atenção necessária",
    recomendacao: "Este resultado sugere fortes indícios que podem estar associados a quadros de depressão ou ansiedade. Recomendamos com ênfase que procure um profissional de saúde mental para avaliação individual e orientação especializada."
  };
}

const getMensagemPredicao = (predicao) => {
  console.log('Valor da predição recebido:', predicao, 'Tipo:', typeof predicao)
  if (predicao === "1" || predicao === 1) return "Você apresenta traços de ansiedade ou depressão"
  if (predicao === "0" || predicao === 0) return "Você não apresenta traços de ansiedade ou depressão"
  return "Resultado não disponível"
}

onMounted(() => {
  // Pegar a última resposta do store
  const ultimaResposta = respostasStore.respostas[respostasStore.respostas.length - 1]
  console.log('Última resposta do store:', ultimaResposta)

  if (ultimaResposta) {
    resultado.value = ultimaResposta
    console.log('Resultado definido:', resultado.value)
  }
})

const voltarParaInicio = () => {
  router.push('/')
}
</script>

<template>
  <div class="results-container">
    <div class="results-content">
      <div class="results-header">
        <h1>Resultado da Análise</h1>
      </div>

      <div v-if="resultado" class="results-main">
        <div class="prediction-section">
          <h2>Predição</h2>
          <div class="prediction-result" :class="{
            'positive-result': resultado.previsao === '1' || resultado.previsao === 1,
            'negative-result': resultado.previsao === '0' || resultado.previsao === 0
          }">
            {{ getMensagemPredicao(resultado.previsao) }}
          </div>
        </div>

        <div class="analysis-section">
          <h2>Análise Detalhada</h2>
          <div class="analysis-content">
            <h3 class="result-title">{{ getGrauGravidade(resultado.probabilidade_doente).titulo }}</h3>
            <p class="result-recommendation">{{ getGrauGravidade(resultado.probabilidade_doente).recomendacao }}</p>
          </div>
        </div>
      </div>

      <div v-else class="no-results">
        <p>Nenhum resultado disponível</p>
      </div>

      <div class="results-footer">
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

.results-header {
  text-align: center;
  margin-bottom: 3rem;
}

.results-header h1 {
  color: #1a3a4a;
  font-size: 2.5rem;
  margin-bottom: 1rem;
  font-weight: 700;
}

.results-main {
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem;
  background-color: white;
  border-radius: 16px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.prediction-section,
.analysis-section {
  margin-bottom: 2rem;
  padding-bottom: 2rem;
  border-bottom: 1px solid #e9ecef;
}

.prediction-section:last-child,
.analysis-section:last-child {
  border-bottom: none;
  margin-bottom: 0;
  padding-bottom: 0;
}

h2 {
  color: #1a3a4a;
  font-size: 1.8rem;
  margin-bottom: 1.5rem;
  font-weight: 600;
}

.prediction-result {
  font-size: 1.4rem;
  color: #2c3e50;
  padding: 1.5rem;
  border-radius: 8px;
  text-align: center;
  font-weight: 500;
  transition: all 0.3s ease;
}

.prediction-result.positive-result {
  background-color: #ffebee;
  border: 2px solid #f44336;
  color: #d32f2f;
}

.prediction-result.negative-result {
  background-color: #e8f5e9;
  border: 2px solid #4caf50;
  color: #2e7d32;
}

.analysis-content {
  padding: 1rem;
}

.result-title {
  font-size: 1.6rem;
  font-weight: 600;
  color: #1a3a4a;
  margin-bottom: 1.5rem;
  text-align: center;
  padding-bottom: 1rem;
  border-bottom: 2px solid #3498db;
}

.result-recommendation {
  font-size: 1.1rem;
  line-height: 1.8;
  color: #2c3e50;
  text-align: justify;
  padding: 1rem;
  background-color: #f8f9fa;
  border-radius: 8px;
}

.no-results {
  text-align: center;
  padding: 3rem;
  background-color: white;
  border-radius: 16px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  color: #666;
  font-size: 1.2rem;
}

.back-button {
  background-color: #3498db;
  color: white;
  padding: 1rem 2rem;
  border: none;
  border-radius: 8px;
  font-size: 1.2rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  display: block;
  margin: 2rem auto 0;
}

.back-button:hover {
  background-color: #2980b9;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(52, 152, 219, 0.2);
}

@media (max-width: 768px) {
  .results-container {
    padding: 1rem;
  }

  .results-main {
    padding: 1rem;
  }

  .results-header h1 {
    font-size: 2rem;
  }

  .result-title {
    font-size: 1.4rem;
  }

  .result-recommendation {
    font-size: 1rem;
  }
}
</style>
