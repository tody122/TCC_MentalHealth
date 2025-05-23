<script setup>
import { ref } from 'vue'

const activeTab = ref('form')
const formData = ref({
  idade: '',
  genero: '',
  sintomas: [],
  frequencia: '',
  duracao: '',
  impacto: '',
  comentario: ''
})

const respostas = ref([])

const sintomas = [
  'Ansiedade',
  'Depressão',
  'Insônia',
  'Estresse',
  'Mudanças de humor',
  'Dificuldade de concentração',
  'Fadiga',
  'Irritabilidade'
]

const frequencias = [
  'Raramente',
  'Às vezes',
  'Frequentemente',
  'Sempre'
]

const enviarFormulario = () => {
  const novaResposta = {
    id: Date.now(),
    data: new Date().toLocaleString(),
    ...formData.value
  }
  respostas.value.push(novaResposta)
  console.log('Dados do formulário:', novaResposta)
  alert('Obrigado por compartilhar suas informações. Suas respostas serão analisadas com cuidado e sigilo.')

  // Gerar e baixar CSV
  const criarCSV = (resposta) => {
    const cabecalho = ['id', 'data', 'idade', 'genero', 'sintomas', 'frequencia', 'duracao', 'impacto', 'comentario'];
    // Garante que os valores nulos ou indefinidos sejam strings vazias e que strings com vírgula sejam envolvidas por aspas
    const escaparValorCSV = (valor) => {
      if (valor === null || valor === undefined) {
        return '';
      }
      const strValor = String(valor);
      if (strValor.includes(',') || strValor.includes('\n') || strValor.includes('"')) {
        return `"${strValor.replace(/"/g, '""')}"`; // Aspas duplas são escapadas com outras aspas duplas
      }
      return strValor;
    };

    const linha = [
      escaparValorCSV(resposta.id),
      escaparValorCSV(resposta.data),
      escaparValorCSV(resposta.idade),
      escaparValorCSV(resposta.genero),
      escaparValorCSV(Array.isArray(resposta.sintomas) ? resposta.sintomas.join('; ') : resposta.sintomas), // Junta sintomas com '; '
      escaparValorCSV(resposta.frequencia),
      escaparValorCSV(resposta.duracao),
      escaparValorCSV(resposta.impacto),
      escaparValorCSV(resposta.comentario)
    ].join(',');

    return cabecalho.join(',') + '\n' + linha;
  };

  const csvContent = criarCSV(novaResposta);
  const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
  const link = document.createElement('a');
  if (link.download !== undefined) { // Feature detection
    const url = URL.createObjectURL(blob);
    link.setAttribute('href', url);
    link.setAttribute('download', `resposta_${novaResposta.id}.csv`);
    link.style.visibility = 'hidden';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    URL.revokeObjectURL(url);
  } else {
    alert("Seu navegador não suporta o download automático. Por favor, copie os dados manualmente se necessário.");
  }

  // Limpar o formulário
  formData.value = {
    idade: '',
    genero: '',
    sintomas: [],
    frequencia: '',
    duracao: '',
    impacto: '',
    comentario: ''
  }
}
</script>

<template>
  <div class="form-page">
    <div class="tabs">
      <button
        :class="['tab-button', { active: activeTab === 'form' }]"
        @click="activeTab = 'form'"
      >
        Formulário
      </button>
      <button
        :class="['tab-button', { active: activeTab === 'data' }]"
        @click="activeTab = 'data'"
      >
        Dados (Provisório)
      </button>
    </div>

    <div v-if="activeTab === 'form'" class="form-container">
      <div class="form-header">
        <div class="header-content">
          <h1>Avaliação de Bem-estar Mental</h1>
          <p class="subtitle">Suas respostas nos ajudarão a entender melhor como você está se sentindo</p>
          <p class="privacy-highlight">* Este formulário é totalmente anônimo</p>
        </div>
      </div>

      <form @submit.prevent="enviarFormulario" class="form-content">
        <div class="form-section">
          <h2>Informações Básicas</h2>
          <div class="form-row">
            <div class="form-group">
              <label for="idade">Idade *</label>
              <input
                type="number"
                id="idade"
                v-model="formData.idade"
                required
                min="0"
                max="120"
                placeholder="Sua idade"
              >
            </div>

            <div class="form-group">
              <label>Gênero *</label>
              <div class="radio-group">
                <label>
                  <input type="radio" v-model="formData.genero" value="masculino" required>
                  Masculino
                </label>
                <label>
                  <input type="radio" v-model="formData.genero" value="feminino">
                  Feminino
                </label>
                <label>
                  <input type="radio" v-model="formData.genero" value="outro">
                  Outro
                </label>
              </div>
            </div>
          </div>
        </div>

        <div class="form-section">
          <h2>Avaliação de Sintomas</h2>
          <div class="form-group">
            <label>Quais sintomas você tem experimentado? *</label>
            <div class="checkbox-group">
              <label v-for="sintoma in sintomas" :key="sintoma" class="checkbox-item">
                <input
                  type="checkbox"
                  v-model="formData.sintomas"
                  :value="sintoma"
                  required
                >
                <span>{{ sintoma }}</span>
              </label>
            </div>
          </div>

          <div class="form-group">
            <label for="frequencia">Com que frequência você experimenta estes sintomas? *</label>
            <select
              id="frequencia"
              v-model="formData.frequencia"
              required
              class="select-input"
            >
              <option value="">Selecione uma opção</option>
              <option v-for="freq in frequencias" :key="freq" :value="freq">
                {{ freq }}
              </option>
            </select>
          </div>

          <div class="form-group">
            <label for="duracao">Há quanto tempo você tem notado estes sintomas? *</label>
            <select
              id="duracao"
              v-model="formData.duracao"
              required
              class="select-input"
            >
              <option value="">Selecione uma opção</option>
              <option value="menos-1-mes">Menos de 1 mês</option>
              <option value="1-3-meses">1 a 3 meses</option>
              <option value="3-6-meses">3 a 6 meses</option>
              <option value="mais-6-meses">Mais de 6 meses</option>
            </select>
          </div>

          <div class="form-group">
            <label for="impacto">Como estes sintomas impactam sua vida diária? *</label>
            <select
              id="impacto"
              v-model="formData.impacto"
              required
              class="select-input"
            >
              <option value="">Selecione uma opção</option>
              <option value="leve">Levemente</option>
              <option value="moderado">Moderadamente</option>
              <option value="significativo">Significativamente</option>
              <option value="severo">Severamente</option>
            </select>
          </div>
        </div>

        <div class="form-section">
          <h2>Informações Adicionais</h2>
          <div class="form-group">
            <label for="comentario">Gostaria de compartilhar mais alguma informação?</label>
            <textarea
              id="comentario"
              v-model="formData.comentario"
              placeholder="Sinta-se à vontade para compartilhar mais detalhes sobre sua situação..."
              rows="4"
            ></textarea>
          </div>
        </div>

        <div class="form-footer">
          <p class="privacy-note">* Todas as informações serão mantidas em sigilo e utilizadas apenas para fins de análise.</p>
          <button type="submit" class="submit-button">Enviar Avaliação</button>
        </div>
      </form>
    </div>

    <div v-if="activeTab === 'data'" class="data-container">
      <h2>Dados Coletados (Provisório)</h2>
      <div class="data-content">
        <div v-if="respostas.length === 0" class="no-data">
          Nenhuma resposta registrada ainda.
        </div>
        <div v-else class="data-list">
          <div v-for="resposta in respostas" :key="resposta.id" class="data-item">
            <pre>{{ JSON.stringify(resposta, null, 2) }}</pre>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.form-page {
  width: 100%;
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

.form-container {
  max-width: 800px;
  margin: 2rem auto;
  padding: 2rem;
  background-color: #fff;
  border-radius: 16px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.form-header {
  text-align: center;
  margin-bottom: 3rem;
  padding-bottom: 2rem;
  border-bottom: 1px solid #e0e0e0;
}

.header-content {
  max-width: 600px;
  margin: 0 auto;
}

.form-header h1 {
  color: #2c3e50;
  font-size: 28px;
  margin-bottom: 1rem;
  font-weight: 600;
}

.subtitle {
  color: #666;
  font-size: 16px;
  line-height: 1.5;
}

.form-section {
  margin-bottom: 2.5rem;
  padding: 1.5rem;
  background-color: #f8f9fa;
  border-radius: 12px;
}

.form-section h2 {
  color: #2c3e50;
  font-size: 20px;
  margin-bottom: 1.5rem;
  font-weight: 500;
}

.form-content {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  margin-bottom: 1rem;
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 2fr;
  gap: 1rem;
}

label {
  color: #2c3e50;
  font-size: 14px;
  font-weight: 500;
}

input[type="text"],
input[type="email"],
input[type="number"],
textarea,
.select-input {
  padding: 0.75rem;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  font-size: 14px;
  transition: all 0.3s ease;
  background-color: white;
}

input[type="text"]:focus,
input[type="email"]:focus,
input[type="number"]:focus,
textarea:focus,
.select-input:focus {
  border-color: #3498db;
  box-shadow: 0 0 0 2px rgba(52, 152, 219, 0.2);
  outline: none;
}

.radio-group,
.checkbox-group {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.checkbox-group {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 1rem;
}

.checkbox-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem;
  border-radius: 6px;
  transition: background-color 0.2s;
}

.checkbox-item:hover {
  background-color: #f0f0f0;
}

.radio-group label,
.checkbox-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-weight: normal;
  cursor: pointer;
}

.submit-button {
  background-color: #3498db;
  color: white;
  padding: 1rem 2rem;
  border: none;
  border-radius: 8px;
  font-size: 16px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
  width: 100%;
  max-width: 300px;
  margin: 0 auto;
}

.submit-button:hover {
  background-color: #2980b9;
  transform: translateY(-1px);
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.form-footer {
  text-align: center;
  margin-top: 2rem;
  padding-top: 2rem;
  border-top: 1px solid #e0e0e0;
}

.privacy-note {
  color: #666;
  font-size: 13px;
  margin-bottom: 1rem;
}

.privacy-highlight {
  color: #3498db;
  font-size: 14px;
  font-weight: 500;
  margin-top: 1rem;
  padding: 0.5rem;
  background-color: rgba(52, 152, 219, 0.1);
  border-radius: 6px;
}

@media (max-width: 768px) {
  .form-container {
    margin: 1rem;
    padding: 1rem;
  }

  .form-row {
    grid-template-columns: 1fr;
  }

  .checkbox-group {
    grid-template-columns: 1fr;
  }
}
</style>
