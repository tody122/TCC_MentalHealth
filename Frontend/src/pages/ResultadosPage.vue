<script setup>
import { ref } from 'vue'
import { useRespostasStore } from '../stores/respostas'

const activeTab = ref('json')
const respostasStore = useRespostasStore()
</script>

<template>
  <div class="resultados-page">
    <div class="resultados-container">
      <h1>Resultados da Pesquisa</h1>

      <div class="tabs">
        <button
          :class="['tab-button', { active: activeTab === 'json' }]"
          @click="activeTab = 'json'"
        >
          Dados JSON (Provisório)
        </button>
      </div>

      <div v-if="activeTab === 'json'" class="data-container">
        <h2>Dados Coletados em JSON</h2>
        <div class="data-content">
          <div v-if="respostasStore.respostas.length === 0" class="no-data">
            Nenhuma resposta registrada ainda.
          </div>
          <div v-else class="data-list">
            <div v-for="resposta in respostasStore.respostas" :key="resposta.id" class="data-item">
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

.tabs {
  display: flex;
  gap: 1rem;
  margin-bottom: 2rem;
  border-bottom: 1px solid #e0e0e0;
  padding-bottom: 1rem;
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
}
</style>
