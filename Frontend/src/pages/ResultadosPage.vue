<script setup>
import { ref, computed } from 'vue'
import { useRespostasStore } from '../stores/respostas'

const activeTab = ref('resultado')
const respostasStore = useRespostasStore()

// Obter a última resposta (mais recente)
const ultimaResposta = computed(() => {
  console.log('=== VERIFICANDO STORE ===')
  console.log('Store respostas:', respostasStore.respostas)
  console.log('Quantidade de respostas:', respostasStore.respostas.length)

  if (respostasStore.respostas.length === 0) {
    console.log('❌ NENHUMA RESPOSTA NO STORE!')
    return null
  }

  console.log('✅ RESPOSTAS ENCONTRADAS:', respostasStore.respostas)
  console.log('✅ ÚLTIMA RESPOSTA:', respostasStore.respostas[respostasStore.respostas.length - 1])

  return respostasStore.respostas[respostasStore.respostas.length - 1]
})

// Determinar o status de saúde mental
const statusSaude = computed(() => {
  if (!ultimaResposta.value) return null

  console.log('🔍 MAPEANDO ESTRUTURA COMPLETA:')
  console.log('📦 ultimaResposta.value:', ultimaResposta.value)
  console.log('📦 Tipo:', typeof ultimaResposta.value)
  console.log('📦 Chaves principais:', Object.keys(ultimaResposta.value))

  // Verificar predicted_class no nível raiz
  console.log('🎯 predicted_class (raiz):', ultimaResposta.value.predicted_class)
  console.log('🎯 Tipo predicted_class:', typeof ultimaResposta.value.predicted_class)
  console.log('🎯 predicted_class existe?', 'predicted_class' in ultimaResposta.value)

  // Verificar se está em dados_enviados
  if (ultimaResposta.value.dados_enviados) {
    console.log('📁 dados_enviados:', ultimaResposta.value.dados_enviados)
    console.log('📁 predicted_class em dados_enviados:', ultimaResposta.value.dados_enviados.predicted_class)
  }

  // Verificar se está em algum objeto aninhado
  console.log('🔍 Estrutura completa (JSON):', JSON.stringify(ultimaResposta.value, null, 2))

  // Verificar se há predição na resposta
  const predicao = ultimaResposta.value.predicted_class !== undefined ? ultimaResposta.value.predicted_class :
                   ultimaResposta.value.prediction !== undefined ? ultimaResposta.value.prediction :
                   ultimaResposta.value.pred !== undefined ? ultimaResposta.value.pred :
                   ultimaResposta.value.result
  const confianca = ultimaResposta.value.confidence || ultimaResposta.value.confidence_score || 0

  // Verificar se está dentro de dados_enviados
  console.log('DEBUG - dados_enviados:', ultimaResposta.value.dados_enviados)
  if (ultimaResposta.value.dados_enviados) {
    console.log('DEBUG - predicted_class em dados_enviados:', ultimaResposta.value.dados_enviados.predicted_class)
  }

  console.log('DEBUG - predicao final:', predicao)
  console.log('DEBUG - tipo predicao:', typeof predicao)
  console.log('DEBUG - predicao === 0:', predicao === 0)
  console.log('DEBUG - predicao === "0":', predicao === "0")
  console.log('DEBUG - Valor da predição recebido:', predicao, 'Tipo:', typeof predicao)

  if (predicao === 0 || predicao === '0') {
    return {
      status: 'saudavel',
      titulo: 'Você está saudável!',
      mensagem: 'Parabéns! Com base na sua avaliação, você não apresenta sinais significativos de problemas de saúde mental.',
      cor: '#27ae60',
      icone: '✅',
      confianca: confianca
    }
  } else if (predicao === 1 || predicao === '1') {
    return {
      status: 'atencao',
      titulo: 'Atenção necessária',
      mensagem: 'Sua avaliação indica que pode ser benéfico buscar apoio profissional para sua saúde mental.',
      cor: '#e74c3c',
      icone: '⚠️',
      confianca: confianca
    }
  } else {
    return {
      status: 'indefinido',
      titulo: 'Resultado não disponível',
      mensagem: 'Não foi possível processar o resultado da sua avaliação.',
      cor: '#95a5a6',
      icone: '❓',
      confianca: 0
    }
  }
})
</script>

<template>
  <div class="resultados-page">
    <div class="resultados-container">
      <h1>Resultados da Pesquisa</h1>

      <div class="tabs">
        <button
          :class="['tab-button', { active: activeTab === 'resultado' }]"
          @click="activeTab = 'resultado'"
        >
          Resultado da Avaliação
        </button>
        <button
          :class="['tab-button', { active: activeTab === 'json' }]"
          @click="activeTab = 'json'"
        >
          Dados Técnicos
        </button>
      </div>

      <!-- Resultado Principal -->
      <div v-if="activeTab === 'resultado'" class="resultado-container">
        <div v-if="!ultimaResposta" class="no-data">
          <h2>Nenhuma avaliação encontrada</h2>
          <p>Complete a avaliação DASS-21 para ver seus resultados.</p>
        </div>

        <div v-else class="resultado-content">
          <div class="resultado-card" :style="{ borderColor: statusSaude?.cor }">
            <div class="resultado-header">
              <span class="resultado-icone">{{ statusSaude?.icone }}</span>
              <h2 :style="{ color: statusSaude?.cor }">{{ statusSaude?.titulo }}</h2>
            </div>

            <div class="resultado-mensagem">
              <p>{{ statusSaude?.mensagem }}</p>
              <div v-if="statusSaude?.confianca > 0" class="confianca-info">
                <p><strong>Confiança da análise:</strong> {{ Math.round(statusSaude.confianca * 100) }}%</p>
              </div>
            </div>

            <div v-if="statusSaude?.status === 'atencao'" class="recomendacoes">
              <h3>Recomendações:</h3>
              <ul>
                <li>Consulte um profissional de saúde mental</li>
                <li>Procure apoio de familiares e amigos</li>
                <li>Mantenha uma rotina saudável</li>
                <li>Pratique atividades que te fazem bem</li>
              </ul>
            </div>

            <div v-if="statusSaude?.status === 'saudavel'" class="recomendacoes">
              <h3>Continue assim:</h3>
              <ul>
                <li>Mantenha hábitos saudáveis</li>
                <li>Pratique exercícios regularmente</li>
                <li>Mantenha conexões sociais</li>
                <li>Busque ajuda se precisar no futuro</li>
              </ul>
            </div>
          </div>
        </div>
      </div>

      <!-- Dados JSON Técnicos -->
      <div v-if="activeTab === 'json'" class="data-container">
        <h2>Dados Técnicos da Avaliação</h2>
        <div class="data-content">
          <div v-if="respostasStore.respostas.length === 0" class="no-data">
            Nenhuma resposta registrada ainda.
          </div>
          <div v-else class="data-list">
            <div v-for="(resposta, index) in respostasStore.respostas" :key="index" class="data-item">
              <h3>Avaliação {{ index + 1 }}</h3>
              <pre>{{ JSON.stringify(resposta, null, 2) }}</pre>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.resultados-page {
  width: 100%;
  padding: 2rem;
}

@media (max-width: 768px) {
  .resultados-page {
    padding: 1rem;
  }
}

@media (max-width: 480px) {
  .resultados-page {
    padding: 0.5rem;
  }
}

.resultados-container {
  max-width: 1200px;
  margin: 0 auto;
}

.resultados-container h1 {
  color: #2c3e50;
  font-size: 28px;
  margin-bottom: 2rem;
  text-align: center;
}

@media (max-width: 768px) {
  .resultados-container h1 {
    font-size: 24px;
    margin-bottom: 1.5rem;
  }
}

@media (max-width: 480px) {
  .resultados-container h1 {
    font-size: 20px;
    margin-bottom: 1rem;
  }
}

.tabs {
  display: flex;
  gap: 1rem;
  margin-bottom: 2rem;
  border-bottom: 1px solid #e0e0e0;
  padding-bottom: 1rem;
}

@media (max-width: 768px) {
  .tabs {
    gap: 0.5rem;
    margin-bottom: 1.5rem;
  }
}

@media (max-width: 480px) {
  .tabs {
    gap: 0.25rem;
    margin-bottom: 1rem;
    flex-wrap: wrap;
  }
}

.tab-button {
  padding: 0.75rem 1.5rem;
  border: none;
  background: none;
  font-size: 16px;
  font-weight: 500;
  color: #666;
  cursor: pointer;
  border-radius: 8px;
  transition: all 0.3s ease;
}

@media (max-width: 768px) {
  .tab-button {
    padding: 0.625rem 1rem;
    font-size: 14px;
  }
}

@media (max-width: 480px) {
  .tab-button {
    padding: 0.5rem 0.75rem;
    font-size: 13px;
    flex: 1;
    min-width: 120px;
  }
}

.tab-button:hover {
  background-color: #f0f0f0;
}

.tab-button.active {
  background-color: #3498db;
  color: white;
}

.data-container {
  background-color: #fff;
  border-radius: 16px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  padding: 2rem;
}

@media (max-width: 768px) {
  .data-container {
    padding: 1.5rem;
  }
}

@media (max-width: 480px) {
  .data-container {
    padding: 1rem;
    border-radius: 12px;
  }
}

.data-container h2 {
  color: #2c3e50;
  margin-bottom: 1.5rem;
  font-size: 24px;
}

.data-content {
  background-color: #f8f9fa;
  border-radius: 8px;
  padding: 1rem;
}

.no-data {
  text-align: center;
  color: #666;
  padding: 2rem;
  font-size: 16px;
}

.data-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.data-item {
  background-color: white;
  border-radius: 8px;
  padding: 1rem;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
}

.data-item pre {
  margin: 0;
  white-space: pre-wrap;
  word-wrap: break-word;
  font-family: 'Courier New', Courier, monospace;
  font-size: 14px;
  color: #2c3e50;
  overflow-x: auto;
}

@media (max-width: 480px) {
  .data-item pre {
    font-size: 11px;
  }
}

/* Estilos para resultado principal */
.resultado-container {
  background-color: #fff;
  border-radius: 16px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  padding: 2rem;
}

.resultado-content {
  display: flex;
  justify-content: center;
}

.resultado-card {
  max-width: 600px;
  width: 100%;
  background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
  border-radius: 20px;
  padding: 2rem;
  border: 3px solid;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
  text-align: center;
}

@media (max-width: 768px) {
  .resultado-card {
    padding: 1.5rem;
    border-radius: 16px;
  }
}

@media (max-width: 480px) {
  .resultado-card {
    padding: 1rem;
    border-radius: 12px;
    border-width: 2px;
  }
}

.resultado-header {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 1.5rem;
}

.resultado-icone {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.resultado-card h2 {
  font-size: 28px;
  font-weight: 600;
  margin: 0;
}

@media (max-width: 768px) {
  .resultado-card h2 {
    font-size: 24px;
  }
}

@media (max-width: 480px) {
  .resultado-card h2 {
    font-size: 20px;
  }
}

.resultado-mensagem {
  margin-bottom: 2rem;
}

.resultado-mensagem p {
  font-size: 18px;
  line-height: 1.6;
  color: #2c3e50;
  margin: 0;
}

@media (max-width: 768px) {
  .resultado-mensagem p {
    font-size: 16px;
  }
}

@media (max-width: 480px) {
  .resultado-mensagem p {
    font-size: 14px;
    line-height: 1.5;
  }
}

.confianca-info {
  margin-top: 1rem;
  padding: 1rem;
  background-color: rgba(52, 152, 219, 0.1);
  border-radius: 8px;
  border-left: 4px solid #3498db;
}

.confianca-info p {
  margin: 0;
  font-size: 16px;
  color: #2c3e50;
}

.recomendacoes {
  background-color: rgba(52, 152, 219, 0.1);
  border-radius: 12px;
  padding: 1.5rem;
  text-align: left;
}

.recomendacoes h3 {
  color: #2c3e50;
  font-size: 20px;
  margin-bottom: 1rem;
  text-align: center;
}

.recomendacoes ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.recomendacoes li {
  padding: 0.5rem 0;
  position: relative;
  padding-left: 1.5rem;
  color: #2c3e50;
  font-size: 16px;
  line-height: 1.5;
}

.recomendacoes li::before {
  content: "•";
  color: #3498db;
  font-weight: bold;
  position: absolute;
  left: 0;
}

.no-data {
  text-align: center;
  color: #666;
  padding: 3rem;
}

.no-data h2 {
  color: #2c3e50;
  margin-bottom: 1rem;
}

.no-data p {
  font-size: 16px;
  line-height: 1.5;
}

@media (max-width: 768px) {
  .resultado-icone {
    font-size: 2.5rem;
  }

  .recomendacoes {
    padding: 1rem;
  }

  .recomendacoes h3 {
    font-size: 18px;
  }

  .recomendacoes li {
    font-size: 14px;
  }

  .confianca-info {
    padding: 0.875rem;
  }

  .confianca-info p {
    font-size: 14px;
  }
}

@media (max-width: 480px) {
  .resultado-icone {
    font-size: 2rem;
    margin-bottom: 0.75rem;
  }

  .recomendacoes {
    padding: 0.75rem;
  }

  .recomendacoes h3 {
    font-size: 16px;
    margin-bottom: 0.75rem;
  }

  .recomendacoes li {
    font-size: 13px;
    padding: 0.375rem 0;
    padding-left: 1.25rem;
  }

  .confianca-info {
    padding: 0.75rem;
  }

  .confianca-info p {
    font-size: 13px;
  }
}
</style>
