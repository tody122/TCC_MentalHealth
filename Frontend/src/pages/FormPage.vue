<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useRespostasStore } from '../stores/respostas'
import { sendDataToBackend } from '../services/api'

const router = useRouter()
const respostasStore = useRespostasStore()

// Controle do modal de aviso
const showWarningModal = ref(false)

// Mostrar modal quando a página carregar
onMounted(() => {
  showWarningModal.value = true
})

const closeWarningModal = () => {
  showWarningModal.value = false
}

// Dados do formulário DASS-21
const formData = ref({
  idade: '',
  genero: '',
  data: Array(21).fill(null)
})

// Opções de gênero
const opcoesGenero = [
  { value: 'masculino', text: 'Masculino' },
  { value: 'feminino', text: 'Feminino' },
  { value: 'outro', text: 'Outro' }
]

// Escala de resposta do DASS-21
const opcoesDASS21 = [
  { value: 0, text: 'Não se aplicou a mim de forma alguma' },
  { value: 1, text: 'Aplicou-se a mim em algum grau, ou por pouco tempo' },
  { value: 2, text: 'Aplicou-se a mim em um grau considerável, ou por uma boa parte do tempo' },
  { value: 3, text: 'Aplicou-se a mim muito, ou na maior parte do tempo' }
]

// Perguntas do DASS-21
const perguntasDASS21 = [
  // Depressão (1, 3, 4, 7, 8, 9, 10)
  { id: 1, texto: 'Senti dificuldade para relaxar', categoria: 'depressao' },
  { id: 2, texto: 'Tive boca seca', categoria: 'ansiedade' },
  { id: 3, texto: 'Não consegui sentir nenhum sentimento positivo', categoria: 'depressao' },
  { id: 4, texto: 'Tive dificuldade para respirar (ex: respiração ofegante, falta de ar na ausência de esforço físico)', categoria: 'ansiedade' },
  { id: 5, texto: 'Tive dificuldade para me motivar a fazer as coisas', categoria: 'depressao' },
  { id: 6, texto: 'Tendi a reagir de forma exagerada às situações', categoria: 'estresse' },
  { id: 7, texto: 'Senti tremores (ex: nas mãos)', categoria: 'ansiedade' },
  { id: 8, texto: 'Senti que estava nervoso e ansioso', categoria: 'ansiedade' },
  { id: 9, texto: 'Preocupei-me com situações em que poderia entrar em pânico e fazer papel de bobo', categoria: 'ansiedade' },
  { id: 10, texto: 'Senti que não tinha nada a esperar', categoria: 'depressao' },
  { id: 11, texto: 'Senti que estava agitado', categoria: 'estresse' },
  { id: 12, texto: 'Tive dificuldade para relaxar', categoria: 'estresse' },
  { id: 13, texto: 'Senti deprimido e melancólico', categoria: 'depressao' },
  { id: 14, texto: 'Eu era intolerante com qualquer coisa que me impedia de continuar o que estava fazendo', categoria: 'estresse' },
  { id: 15, texto: 'Senti que estava à beira do pânico', categoria: 'ansiedade' },
  { id: 16, texto: 'Não consegui me entusiasmar com nada', categoria: 'depressao' },
  { id: 17, texto: 'Senti que não valia muito como pessoa', categoria: 'depressao' },
  { id: 18, texto: 'Senti que era bastante temperamental', categoria: 'estresse' },
  { id: 19, texto: 'Senti palpitações cardíacas mesmo sem esforço físico (ex: sensação de aumento da frequência cardíaca)', categoria: 'ansiedade' },
  { id: 20, texto: 'Senti medo sem uma boa razão', categoria: 'ansiedade' },
  { id: 21, texto: 'Senti que a vida não tinha sentido', categoria: 'depressao' }
]

const validateForm = () => {
  // Validar idade
  if (!formData.value.idade || formData.value.idade < 0 || formData.value.idade > 120) {
    alert('Por favor, insira uma idade válida (entre 0 e 120 anos)');
    return false;
  }

  // Validar gênero
  if (!formData.value.genero) {
    alert('Por favor, selecione seu gênero');
    return false;
  }

  // Validar todas as respostas do DASS-21
  for (let i = 0; i < formData.value.data.length; i++) {
    if (formData.value.data[i] === null || formData.value.data[i] === undefined) {
      alert(`Por favor, responda a pergunta ${i + 1}: "${perguntasDASS21[i].texto}"`);
      return false;
    }
  }

  return true;
};

const handleSubmit = async () => {
  if (!validateForm()) return;

  // Console log das respostas dadas
  console.log('=== RESPOSTAS DO DASS-21 ===');
  console.log('Idade:', formData.value.idade);
  console.log('Gênero:', formData.value.genero);
  console.log('\n--- Respostas por pergunta ---');

  formData.value.data.forEach((resposta, index) => {
    const pergunta = perguntasDASS21[index];
    const opcaoEscolhida = opcoesDASS21.find(opcao => opcao.value === resposta);
    console.log(`${index + 1}. ${pergunta.texto}`);
    console.log(`   Resposta: ${resposta} - "${opcaoEscolhida?.text || 'Não respondida'}"`);
    console.log('');
  });

  const novaResposta = {
    data: formData.value.data
  };

  // Mostrar o JSON que será enviado
  console.log('=== DADOS ENVIADOS PARA API ===');
  console.log('Dados enviados:', JSON.stringify(novaResposta, null, 2));

  try {
    const response = await sendDataToBackend(novaResposta);
    // Mostrar a resposta do servidor
    console.log('Resposta do servidor (bruta):', response);
    console.log('Tipo da resposta:', typeof response);
    console.log('Resposta do servidor (stringify):', JSON.stringify(response, null, 2));

    // Armazenar a resposta da API no store
    const respostaCompleta = {
      ...response,
      dados_enviados: novaResposta
    };
    console.log('Armazenando no store:', respostaCompleta);
    respostasStore.adicionarResposta(respostaCompleta);
    console.log('✅ DADOS SALVOS NO STORE!');
    console.log('Store após salvar:', respostasStore.respostas);
    router.push('/resultados');
  } catch (error) {
    console.error('Erro ao enviar dados:', error);
    // Removido o alert de erro
  }
};
</script>

<template>
  <!-- Modal de Aviso -->
  <div v-if="showWarningModal" class="modal-overlay" @click.self="closeWarningModal">
    <div class="modal-content">
      <div class="modal-header">
        <h2 class="modal-title">⚠️ Aviso Importante</h2>
        <button class="modal-close" @click="closeWarningModal" aria-label="Fechar">×</button>
      </div>
      <div class="modal-body">
        <div class="warning-icon">🏥</div>
        <p class="warning-text">
          <strong>Este questionário não deve ser usado como palavra final de um médico.</strong>
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

  <div class="form-page">
    <div class="form-container">
      <div class="form-header">
        <div class="header-content">
          <h1>Avaliação de Bem-estar Mental</h1>
          <p class="subtitle">Suas respostas nos ajudarão a entender melhor como você está se sentindo</p>
          <p class="privacy-highlight">* Este formulário é totalmente anônimo</p>
        </div>
      </div>

      <form @submit.prevent="handleSubmit" class="form-content">
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
                <label v-for="opcao in opcoesGenero" :key="opcao.value">
                  <input type="radio" v-model="formData.genero" :value="opcao.value" required>
                  {{ opcao.text }}
                </label>
              </div>
            </div>
          </div>
        </div>

        <div class="form-section">
          <h2>Escala DASS-21 - Avaliação de Depressão, Ansiedade e Estresse</h2>
          <p class="dass-instructions">
            Por favor, leia cada afirmação e marque a opção que melhor descreve como você se sentiu na última semana.
          </p>

          <div v-for="(pergunta, index) in perguntasDASS21" :key="pergunta.id" class="dass-question">
            <div class="question-header">
              <span class="question-number">{{ index + 1 }}.</span>
            </div>
            <p class="question-text">{{ pergunta.texto }}</p>

            <div class="dass-options">
              <label v-for="opcao in opcoesDASS21" :key="opcao.value" class="dass-option">
                <input
                  type="radio"
                  :name="`dass21_${index}`"
                  :value="opcao.value"
                  v-model="formData.data[index]"
                  required
                >
                <span class="option-text">{{ opcao.text }}</span>
              </label>
            </div>
          </div>
        </div>

        <div class="form-footer">
          <p class="privacy-note">* Todas as informações serão mantidas em sigilo e utilizadas apenas para fins de análise.</p>
          <button type="submit" class="submit-button">Enviar Avaliação</button>
        </div>
      </form>
    </div>
  </div>
</template>

<style scoped>
.form-page {
  width: 100%;
}

.form-container {
  max-width: 800px;
  margin: 2rem auto;
  padding: 2rem;
  background-color: #fff;
  border-radius: 16px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

@media (max-width: 768px) {
  .form-container {
    margin: 1rem 0.5rem;
    padding: 1rem;
  }
}

@media (max-width: 480px) {
  .form-container {
    margin: 0.5rem;
    padding: 0.75rem;
    border-radius: 12px;
  }
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

@media (max-width: 768px) {
  .form-header h1 {
    font-size: 24px;
  }
}

@media (max-width: 480px) {
  .form-header h1 {
    font-size: 20px;
  }
}

.subtitle {
  color: #666;
  font-size: 16px;
  line-height: 1.5;
}

@media (max-width: 480px) {
  .subtitle {
    font-size: 14px;
  }
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

/* Estilos específicos para DASS-21 */
.dass-instructions {
  background-color: #e8f4fd;
  padding: 1rem;
  border-radius: 8px;
  margin-bottom: 2rem;
  color: #2c3e50;
  font-size: 14px;
  border-left: 4px solid #3498db;
}

.dass-question {
  margin-bottom: 2rem;
  padding: 1.5rem;
  background-color: #f8f9fa;
  border-radius: 12px;
  border: 1px solid #e9ecef;
}

@media (max-width: 768px) {
  .dass-question {
    margin-bottom: 1.5rem;
    padding: 1rem;
  }
}

@media (max-width: 480px) {
  .dass-question {
    margin-bottom: 1rem;
    padding: 0.75rem;
  }
}

.question-header {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 1rem;
}

.question-number {
  background-color: #3498db;
  color: white;
  padding: 0.25rem 0.5rem;
  border-radius: 4px;
  font-weight: 600;
  font-size: 12px;
}


.question-text {
  font-size: 16px;
  color: #2c3e50;
  margin-bottom: 1rem;
  line-height: 1.5;
  font-weight: 500;
}

@media (max-width: 480px) {
  .question-text {
    font-size: 14px;
    margin-bottom: 0.75rem;
  }
}

.dass-options {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 0.75rem;
}

@media (max-width: 768px) {
  .dass-options {
    grid-template-columns: 1fr;
    gap: 0.5rem;
  }
}

.dass-option {
  display: flex;
  align-items: flex-start;
  gap: 0.75rem;
  padding: 0.75rem;
  background-color: white;
  border: 2px solid #e9ecef;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.dass-option:hover {
  border-color: #3498db;
  background-color: #f8f9fa;
}

.dass-option input[type="radio"] {
  margin: 0;
  flex-shrink: 0;
  margin-top: 0.125rem;
}

.dass-option input[type="radio"]:checked + .option-text {
  color: #3498db;
  font-weight: 500;
}

.dass-option:has(input[type="radio"]:checked) {
  border-color: #3498db;
  background-color: #e8f4fd;
}

.option-text {
  font-size: 14px;
  line-height: 1.4;
  color: #2c3e50;
}

@media (max-width: 480px) {
  .option-text {
    font-size: 13px;
    line-height: 1.3;
  }
}

@media (max-width: 768px) {
  .form-row {
    grid-template-columns: 1fr;
  }

  .checkbox-group {
    grid-template-columns: 1fr;
  }

  .form-section {
    padding: 1rem;
  }

  .form-section h2 {
    font-size: 18px;
  }

  .dass-instructions {
    font-size: 13px;
    padding: 0.875rem;
  }
}

@media (max-width: 480px) {
  .form-header {
    margin-bottom: 1.5rem;
    padding-bottom: 1rem;
  }

  .form-section {
    padding: 0.75rem;
    margin-bottom: 1.5rem;
  }

  .form-section h2 {
    font-size: 16px;
    margin-bottom: 1rem;
  }

  .dass-instructions {
    font-size: 12px;
    padding: 0.75rem;
    margin-bottom: 1.5rem;
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
