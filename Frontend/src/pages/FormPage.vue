<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useRespostasStore } from '../stores/respostas'

const router = useRouter()
const respostasStore = useRespostasStore()
const formData = ref({
  idade: '',
  genero: '',
  familia_depressao: '',
  renda_familiar: '',
  idade_primeiro_sintoma: '',
  divisao_renda: '',
  ultima_serie_ciencias: '',
  perda_negocio_covid: '',
  comentario: ''
})

const opcoesGenero = [
  { value: 'masculino', text: 'Masculino' },
  { value: 'feminino', text: 'Feminino' },
  { value: 'outro', text: 'Outro' }
]

const opcoesFamiliaDepressao = [
  { value: '1', text: 'Sim' },
  { value: '0', text: 'Não' },
  { value: 'null', text: 'Não quero responder' },
  { value: 'null', text: 'Não sei' }
]

const opcoesRendaFamiliar = [
  { value: 'confortavel', text: 'Vivendo confortavelmente com a renda atual' },
  { value: 'sobrevivendo', text: 'Sobrevivendo com a renda atual' },
  { value: 'dificuldades', text: 'Encontrando dificuldades com a renda atual' },
  { value: 'muitas_dificuldades', text: 'Encontrando muitas dificuldades com a renda atual' },
  { value: 'null', text: 'Não quero responder' },
  { value: 'null', text: 'Não sei' }
]

const opcoesIdadePrimeiroSintoma = [
  { value: 'menos_13', text: 'Menos que 13 anos' },
  { value: '13_19', text: '13-19' },
  { value: '20_29', text: '20-29' },
  { value: '30_39', text: '30-39' },
  { value: '40_mais', text: '40 ou mais velho' },
  { value: 'null', text: 'Não quero responder' },
  { value: 'null', text: 'Não sei' }
]

const opcoesDivisaoRenda = [
  { value: '5', text: '20% mais pobres' },
  { value: '4', text: '20% pobres' },
  { value: '3', text: '20% média' },
  { value: '2', text: '20% média alta' },
  { value: '1', text: '20% ricos' }
]

const opcoesUltimaSerieCiencias = [
  { value: 'nenhuma', text: 'Nenhuma' },
  { value: 'primario', text: 'Primário' },
  { value: 'fundamental_medio', text: 'Fundamental ou Ensino Médio' },
  { value: 'faculdade', text: 'Faculdade' }
]

const opcoesPerdaNegocioCovid = [
  { value: '1', text: 'Sim' },
  { value: '0', text: 'Não' },
  { value: 'null', text: 'Não se encaixa com o perguntado' },
  { value: 'null', text: 'Não quero responder' },
  { value: 'null', text: 'Não sei' }
]

const enviarFormulario = () => {
  const novaResposta = {
    id: Date.now(),
    data: new Date().toLocaleString(),
    ...formData.value
  }
  respostasStore.adicionarResposta(novaResposta)
  console.log('Dados do formulário:', novaResposta)

  // Redirecionar para a página de resultados
  router.push('/resultados')

  // Gerar e baixar CSV
  const criarCSV = (resposta) => {
    const cabecalho = ['id', 'data', 'idade', 'genero', 'familia_depressao', 'renda_familiar', 'idade_primeiro_sintoma', 'divisao_renda', 'ultima_serie_ciencias', 'perda_negocio_covid', 'comentario'];
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
      escaparValorCSV(resposta.familia_depressao),
      escaparValorCSV(resposta.renda_familiar),
      escaparValorCSV(resposta.idade_primeiro_sintoma),
      escaparValorCSV(resposta.divisao_renda),
      escaparValorCSV(resposta.ultima_serie_ciencias),
      escaparValorCSV(resposta.perda_negocio_covid),
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
    familia_depressao: '',
    renda_familiar: '',
    idade_primeiro_sintoma: '',
    divisao_renda: '',
    ultima_serie_ciencias: '',
    perda_negocio_covid: '',
    comentario: ''
  }
}
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
