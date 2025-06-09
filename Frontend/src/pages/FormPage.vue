<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useRespostasStore } from '../stores/respostas'
import { sendDataToBackend } from '../services/api'

const router = useRouter()
const respostasStore = useRespostasStore()
const formData = ref({
  MH6: '',
  Subjective_Income: '',
  MH7B2: '',
  Household_Income: '',
  W3: '',
  WP21759: '',
})

const opcoesGenero = [
  { value: 'masculino', text: 'Masculino' },
  { value: 'feminino', text: 'Feminino' },
  { value: 'outro', text: 'Outro' }
]

const opcoesFamiliaDepressao = [
  { value: '2', text: 'Sim' },
  { value: '1', text: 'Não' },
  { value: '2', text: 'Não quero responder' },
  { value: '2', text: 'Não sei' }
]

const opcoesRendaFamiliar = [
  { value: '1', text: 'Vivendo confortavelmente com a renda atual' },
  { value: '2', text: 'Sobrevivendo com a renda atual' },
  { value: '3', text: 'Encontrando dificuldades com a renda atual' },
  { value: '4', text: 'Encontrando muitas dificuldades com a renda atual' },
  { value: '2', text: 'Não quero responder' },
  { value: '2', text: 'Não sei' }
]

const opcoesIdadePrimeiroSintoma = [

  { value: '1', text: 'Menos que 13 anos' },
  { value: '2', text: '13-19' },
  { value: '3', text: '20-29' },
  { value: '4', text: '30-39' },
  { value: '5', text: '40 ou mais velho' },
  { value: '1', text: 'Não quero responder' },
  { value: '1', text: 'Não sei' },
  { value: '5', text: 'Não sinto os sintomas' }
]

const opcoesDivisaoRenda = [
  { value: '5', text: '20% mais pobres' },
  { value: '4', text: '20% pobres' },
  { value: '3', text: '20% média' },
  { value: '2', text: '20% média alta' },
  { value: '1', text: '20% ricos' }
]

const opcoesUltimaSerieCiencias = [
  { value: '1', text: 'Nenhuma' },
  { value: '2', text: 'Primário' },
  { value: '3', text: 'Fundamental ou Ensino Médio' },
  { value: '4', text: 'Faculdade' }
]

const opcoesPerdaNegocioCovid = [
  { value: '2', text: 'Sim' },
  { value: '1', text: 'Não' },
  { value: '3', text: 'Não se encaixa com o perguntado' },
  { value: '2', text: 'Não quero responder' },
  { value: '2', text: 'Não sei' }
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

  // Validar família depressão
  if (!formData.value.familia_depressao) {
    alert('Por favor, responda sobre depressão/ansiedade na família');
    return false;
  }

  // Validar renda familiar
  if (!formData.value.renda_familiar) {
    alert('Por favor, selecione sua situação de renda familiar');
    return false;
  }

  // Validar idade primeiro sintoma
  if (!formData.value.idade_primeiro_sintoma) {
    alert('Por favor, selecione a idade do primeiro sintoma');
    return false;
  }

  // Validar divisão renda
  if (!formData.value.divisao_renda) {
    alert('Por favor, selecione sua divisão de renda');
    return false;
  }

  // Validar última série ciências
  if (!formData.value.ultima_serie_ciencias) {
    alert('Por favor, selecione sua última série em ciências');
    return false;
  }

  // Validar perda negócio covid
  if (!formData.value.perda_negocio_covid) {
    alert('Por favor, responda sobre perda de negócio/trabalho após covid');
    return false;
  }

  return true;
};

const handleSubmit = async () => {
  if (!validateForm()) return;

  const novaResposta = {
    MH6: formData.value.familia_depressao === 'null' ? '0' : formData.value.familia_depressao,
    Subjective_Income: formData.value.renda_familiar === 'null' ? '0' : formData.value.renda_familiar,
    MH7B2: formData.value.idade_primeiro_sintoma === 'null' ? '0' : formData.value.idade_primeiro_sintoma,
    Household_Income: formData.value.divisao_renda === 'null' ? '0' : formData.value.divisao_renda,
    W3: formData.value.ultima_serie_ciencias === 'null' ? '0' : formData.value.ultima_serie_ciencias,
    WP21759: formData.value.perda_negocio_covid === 'null' ? '0' : formData.value.perda_negocio_covid
  };

  // Mostrar o JSON que será enviado
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
    router.push('/resultados');
  } catch (error) {
    console.error('Erro ao enviar dados:', error);
    alert('Erro ao enviar dados. Por favor, tente novamente.');
  }
};
</script>

<template>
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
          <h2>Avaliação de Contexto</h2>

          <div class="form-group">
            <label for="familia_depressao">Amigos ou família têm se sentido com depressão/ansiedade? *</label>
            <select
              id="familia_depressao"
              v-model="formData.familia_depressao"
              required
              class="select-input"
            >
              <option value="">Selecione uma opção</option>
              <option v-for="opcao in opcoesFamiliaDepressao" :key="opcao.value" :value="opcao.value">
                {{ opcao.text }}
              </option>
            </select>
          </div>

          <div class="form-group">
            <label for="renda_familiar">Qual seu sentimento sobre renda familiar? *</label>
            <select
              id="renda_familiar"
              v-model="formData.renda_familiar"
              required
              class="select-input"
            >
              <option value="">Selecione uma opção</option>
              <option v-for="opcao in opcoesRendaFamiliar" :key="opcao.value" :value="opcao.value">
                {{ opcao.text }}
              </option>
            </select>
          </div>

          <div class="form-group">
            <label for="idade_primeiro_sintoma">Idade em que começou a se sentir deprimido/ansioso pela primeira vez? *</label>
            <select
              id="idade_primeiro_sintoma"
              v-model="formData.idade_primeiro_sintoma"
              required
              class="select-input"
            >
              <option value="">Selecione uma opção</option>
              <option v-for="opcao in opcoesIdadePrimeiroSintoma" :key="opcao.value" :value="opcao.value">
                {{ opcao.text }}
              </option>
            </select>
          </div>

          <div class="form-group">
            <label for="divisao_renda">Em qual divisão de renda você se encontra? *</label>
            <select
              id="divisao_renda"
              v-model="formData.divisao_renda"
              required
              class="select-input"
            >
              <option value="">Selecione uma opção</option>
              <option v-for="opcao in opcoesDivisaoRenda" :key="opcao.value" :value="opcao.value">
                {{ opcao.text }}
              </option>
            </select>
          </div>

          <div class="form-group">
            <label for="ultima_serie_ciencias">Qual série que você estudou ciências pela última vez? *</label>
            <select
              id="ultima_serie_ciencias"
              v-model="formData.ultima_serie_ciencias"
              required
              class="select-input"
            >
              <option value="">Selecione uma opção</option>
              <option v-for="opcao in opcoesUltimaSerieCiencias" :key="opcao.value" :value="opcao.value">
                {{ opcao.text }}
              </option>
            </select>
          </div>

          <div class="form-group">
            <label for="perda_negocio_covid">Você perdeu seu negócio ou trabalho depois do coronavirus? *</label>
            <select
              id="perda_negocio_covid"
              v-model="formData.perda_negocio_covid"
              required
              class="select-input"
            >
              <option value="">Selecione uma opção</option>
              <option v-for="opcao in opcoesPerdaNegocioCovid" :key="opcao.value" :value="opcao.value">
                {{ opcao.text }}
              </option>
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
