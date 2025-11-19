<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useRespostasStore } from '../stores/respostas'

const router = useRouter()
const respostasStore = useRespostasStore()
const resultado = ref(null)

// Controle do modal de aviso
const showWarningModal = ref(false)

// Mostrar modal quando a página carregar
onMounted(() => {
  showWarningModal.value = true

  // Pegar a última resposta do store
  const ultimaResposta = respostasStore.respostas[respostasStore.respostas.length - 1]
  console.log('🔍 Última resposta do store:', ultimaResposta)
  console.log('🔍 predicted_class:', ultimaResposta?.predicted_class)
  console.log('🔍 confidence:', ultimaResposta?.confidence)

  if (ultimaResposta) {
    resultado.value = ultimaResposta
    console.log('✅ Resultado definido:', resultado.value)
  }
})

const closeWarningModal = () => {
  showWarningModal.value = false
}

const getGrauGravidade = (probabilidade) => {
  const prob = probabilidade * 100;
  if (prob <= 20) return {
    titulo: "Baixa probabilidade de sintomas relacionados",
    recomendacao: "Ainda que os indicadores sejam baixos, é importante manter hábitos saudáveis e cuidar da saúde mental. Em caso de dúvidas ou mudanças no bem-estar, a orientação de um profissional qualificado é sempre recomendada."
  };
  if (prob <= 40) return {
    titulo: "Indícios leves de possíveis sintomas.",
    recomendacao: "Os dados sugerem uma atenção inicial. Mesmo em estágios leves, procurar um profissional qualificado pode oferecer suporte e esclarecimento adequados."
  };
  if (prob <= 60) return {
    titulo: "Probabilidade moderada de sintomas.",
    recomendacao: "Este resultado aponta sinais que merecem atenção. A avaliação com um profissional da saúde mental é altamente recomendada para compreender melhor a situação e buscar orientações adequadas."
  };
  if (prob <= 80) return {
    titulo: "Sinais relevantes de possíveis sintomas.",
    recomendacao: "A análise indica um nível significativo de possíveis indícios. Buscar o acompanhamento de um profissional qualificado é uma medida essencial para cuidado e prevenção."
  };
  return {
    titulo: "Alta probabilidade de sintomas consistentes.",
    recomendacao: "O resultado sugere fortes indícios que podem estar associados a quadros de depressão ou ansiedade. Recomendamos com ênfase que procure um profissional de saúde mental para avaliação individual e orientação especializada."
  };
}

const getMensagemPredicao = (predicao) => {
  console.log('Valor da predição recebido:', predicao, 'Tipo:', typeof predicao)
  if (predicao === "1" || predicao === 1) return "Os dados sugerem que vocês não se encontram em um bom estado emocional"
  if (predicao === "0" || predicao === 0) return "Os dados sugerem que você se encontra em um bom estado emocional."
  return "Resultado não disponível"
}

const getRecomendacaoPersonalizada = (predicted_class, confidence) => {
  // Converte predicted_class para número se for string
  const predicao = predicted_class === "1" || predicted_class === 1 ? 1 : 0
  const confianca = confidence || 0

  // Caso 1: Predição positiva (tem sintomas)
  if (predicao === 1) {
    if (confianca >= 0.8) {
      return "Com base na análise dos seus padrões de resposta, há indicações significativas que sugerem a presença de sintomas relacionados a ansiedade, depressão ou estresse. Recomendamos fortemente que busque avaliação com um profissional de saúde mental o quanto antes. O apoio profissional pode ajudá-lo a compreender melhor sua situação e desenvolver estratégias adequadas de cuidado."
    } else if (confianca >= 0.6) {
      return "Os resultados indicam a possibilidade de sintomas relacionados a ansiedade, depressão ou estresse. Embora a análise não seja definitiva, é importante considerar buscar orientação profissional para uma avaliação mais completa. A atenção precoce pode fazer uma grande diferença no seu bem-estar."
    } else if (confianca >= 0.4) {
      return "Há alguns indícios que podem sugerir a presença de sintomas leves. Embora não seja conclusivo, estar atento ao seu bem-estar emocional é importante. Considere praticar atividades que promovam seu equilíbrio mental e, se os sintomas persistirem ou piorarem, busque apoio profissional."
    } else {
      return "Os resultados apresentam indícios leves que merecem atenção. Mantenha hábitos saudáveis, como exercícios físicos, boa alimentação e sono adequado. Se notar mudanças significativas no seu estado emocional, não hesite em procurar um profissional de saúde mental para orientação."
    }
  }

  // Caso 2: Predição negativa (não tem sintomas)
  if (predicao === 0) {
    if (confianca >= 0.8) {
      return "Os resultados indicam que você apresenta um padrão de respostas que não sugere sintomas significativos de ansiedade, depressão ou estresse no momento. Continue mantendo hábitos saudáveis e prestando atenção ao seu bem-estar emocional. Lembre-se de que buscar ajuda profissional sempre é uma opção válida, mesmo quando tudo parece estar bem."
    } else if (confianca >= 0.6) {
      return "Com base na análise, não há indicações claras de sintomas relacionados a ansiedade, depressão ou estresse. Isso é positivo! Continue investindo em sua saúde mental através de práticas como exercícios, alimentação equilibrada e manutenção de relacionamentos saudáveis."
    } else {
      return "Os resultados sugerem que você está em um bom estado de bem-estar mental. Continue cuidando de si mesmo e mantenha uma rotina equilibrada. Se surgirem preocupações no futuro, não hesite em buscar apoio profissional quando necessário."
    }
  }

  // Caso padrão (resultado não disponível ou incerto)
  return "Não foi possível gerar uma recomendação precisa com base nos dados disponíveis. Se tiver preocupações sobre sua saúde mental, recomendamos buscar orientação de um profissional qualificado."
}

const voltarParaInicio = () => {
  router.push('/')
}
</script>

<template>
  <!-- Modal de Aviso -->
  <div v-if="showWarningModal" class="modal-overlay" @click.self="closeWarningModal">
    <div class="modal-content">
      <div class="modal-header">
        <h2 class="modal-title">Aviso Importante</h2>
        <button class="modal-close" @click="closeWarningModal" aria-label="Fechar">×</button>
      </div>
      <div class="modal-body">
        <p class="warning-text">
          <strong>Este resultado não deve ser usado como palavra final de um médico.</strong>
        </p>
        <p class="warning-text">
          Esta ferramenta é apenas para <strong>fins de estudo e pesquisa</strong>.
          Os resultados obtidos aqui são informativos e não substituem uma avaliação profissional.
        </p>
        <p class="warning-text">
          Se você tiver preocupações sobre sua saúde mental, procure um profissional qualificado para obter um diagnóstico adequado.
        </p>
      </div>
      <div class="modal-footer">
        <button class="modal-button" @click="closeWarningModal">Entendi, continuar</button>
      </div>
    </div>
  </div>

  <div class="results-container">
    <div class="results-content">
      <div class="results-header">
        <h1>Resultado da Análise</h1>
      </div>

      <div v-if="resultado" class="results-main">
        <div class="prediction-section">
          <h2>Predição</h2>
          <div class="prediction-result" :class="{
            'positive-result': resultado.predicted_class === '1' || resultado.predicted_class === 1,
            'negative-result': resultado.predicted_class === '0' || resultado.predicted_class === 0
          }">
            {{ getMensagemPredicao(resultado.predicted_class) }}
          </div>
        </div>

        <div class="analysis-section">
          <h2>Análise Detalhada</h2>
          <div class="analysis-content">
            <h3 class="result-title">{{ getGrauGravidade(resultado.confidence).titulo }}</h3>
            <p class="result-recommendation">{{ getRecomendacaoPersonalizada(resultado.predicted_class, resultado.confidence) }}</p>
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

/* Estilos do Modal de Aviso */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.6);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
  padding: 1rem;
  animation: fadeIn 0.3s ease;
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

.modal-content {
  background: white;
  border-radius: 16px;
  max-width: 500px;
  width: 100%;
  max-height: 90vh;
  overflow-y: auto;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
  animation: slideUp 0.3s ease;
  position: relative;
}

@keyframes slideUp {
  from {
    transform: translateY(50px);
    opacity: 0;
  }
  to {
    transform: translateY(0);
    opacity: 1;
  }
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem;
  border-bottom: 1px solid #e0e0e0;
}

.modal-title {
  color: #2c3e50;
  font-size: 24px;
  font-weight: 600;
  margin: 0;
}

.modal-close {
  background: none;
  border: none;
  font-size: 32px;
  color: #999;
  cursor: pointer;
  line-height: 1;
  padding: 0;
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 4px;
  transition: all 0.2s ease;
}

.modal-close:hover {
  background-color: #f0f0f0;
  color: #333;
}

.modal-body {
  padding: 2rem 1.5rem;
  text-align: center;
}

.warning-icon {
  font-size: 48px;
  margin-bottom: 1rem;
}

.warning-text {
  color: #2c3e50;
  font-size: 16px;
  line-height: 1.6;
  margin-bottom: 1rem;
}

.warning-text:last-of-type {
  margin-bottom: 0;
}

.warning-text strong {
  color: #e74c3c;
  font-weight: 600;
}

.modal-footer {
  padding: 1.5rem;
  border-top: 1px solid #e0e0e0;
  display: flex;
  justify-content: center;
}

.modal-button {
  background-color: #3498db;
  color: white;
  padding: 0.875rem 2rem;
  border: none;
  border-radius: 8px;
  font-size: 16px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
  min-width: 200px;
}

.modal-button:hover {
  background-color: #2980b9;
  transform: translateY(-1px);
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.modal-button:active {
  transform: translateY(0);
}

/* Responsividade do Modal */
@media (max-width: 768px) {
  .modal-content {
    max-width: 90%;
    border-radius: 12px;
  }

  .modal-header {
    padding: 1.25rem;
  }

  .modal-title {
    font-size: 20px;
  }

  .modal-body {
    padding: 1.5rem 1.25rem;
  }

  .warning-icon {
    font-size: 40px;
  }

  .warning-text {
    font-size: 14px;
  }

  .modal-footer {
    padding: 1.25rem;
  }

  .modal-button {
    width: 100%;
    min-width: auto;
  }
}

@media (max-width: 480px) {
  .modal-overlay {
    padding: 0.5rem;
  }

  .modal-content {
    max-width: 100%;
    border-radius: 12px;
  }

  .modal-header {
    padding: 1rem;
  }

  .modal-title {
    font-size: 18px;
  }

  .modal-close {
    font-size: 28px;
    width: 28px;
    height: 28px;
  }

  .modal-body {
    padding: 1.25rem 1rem;
  }

  .warning-icon {
    font-size: 36px;
  }

  .warning-text {
    font-size: 13px;
  }

  .modal-footer {
    padding: 1rem;
  }

  .modal-button {
    font-size: 14px;
    padding: 0.75rem 1.5rem;
  }
}
</style>
