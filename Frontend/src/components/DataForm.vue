<template>
  <div class="data-form">
    <form @submit.prevent="handleSubmit">
      <div class="form-group">
        <label for="W1">W1 - Satisfação com a vida:</label>
        <select id="W1" v-model="formData.W1" required>
          <option value="">Selecione...</option>
          <option value="1">1 - Muito insatisfeito</option>
          <option value="2">2</option>
          <option value="3">3</option>
          <option value="4">4</option>
          <option value="5">5</option>
          <option value="6">6</option>
          <option value="7">7</option>
          <option value="8">8</option>
          <option value="9">9</option>
          <option value="10">10 - Muito satisfeito</option>
        </select>
      </div>

      <div class="form-group">
        <label for="W2">W2 - Satisfação com a economia:</label>
        <select id="W2" v-model="formData.W2" required>
          <option value="">Selecione...</option>
          <option value="1">1 - Muito insatisfeito</option>
          <option value="2">2</option>
          <option value="3">3</option>
          <option value="4">4</option>
          <option value="5">5</option>
          <option value="6">6</option>
          <option value="7">7</option>
          <option value="8">8</option>
          <option value="9">9</option>
          <option value="10">10 - Muito satisfeito</option>
        </select>
      </div>

      <div class="form-group">
        <label for="W3">W3 - Satisfação com o governo:</label>
        <select id="W3" v-model="formData.W3" required>
          <option value="">Selecione...</option>
          <option value="1">1 - Muito insatisfeito</option>
          <option value="2">2</option>
          <option value="3">3</option>
          <option value="4">4</option>
          <option value="5">5</option>
          <option value="6">6</option>
          <option value="7">7</option>
          <option value="8">8</option>
          <option value="9">9</option>
          <option value="10">10 - Muito satisfeito</option>
        </select>
      </div>

      <div class="form-group">
        <label for="W4">W4 - Satisfação com a democracia:</label>
        <select id="W4" v-model="formData.W4" required>
          <option value="">Selecione...</option>
          <option value="1">1 - Muito insatisfeito</option>
          <option value="2">2</option>
          <option value="3">3</option>
          <option value="4">4</option>
          <option value="5">5</option>
          <option value="6">6</option>
          <option value="7">7</option>
          <option value="8">8</option>
          <option value="9">9</option>
          <option value="10">10 - Muito satisfeito</option>
        </select>
      </div>

      <button type="submit" :disabled="loading">
        {{ loading ? 'Enviando...' : 'Enviar' }}
      </button>
    </form>

    <div class="test-section">
      <h3>Teste Rápido</h3>
      <button @click="enviarDadosParaPrever" class="test-button">
        Testar com Dados Pré-definidos
      </button>
    </div>

    <div v-if="response" class="response">
      <h3>Resultado da Análise:</h3>
      <pre>{{ JSON.stringify(response, null, 2) }}</pre>
    </div>

    <div v-if="error" class="error">
      {{ error }}
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';
import { sendDataToBackend } from '../services/api';

export default {
  name: 'DataForm',
  setup() {
    const formData = ref({
      W1: '',
      W2: '',
      W3: '',
      W4: ''
    });
    const response = ref(null);
    const error = ref(null);
    const loading = ref(false);

    const handleSubmit = async () => {
      loading.value = true;
      error.value = null;

      try {
        const result = await sendDataToBackend(formData.value);
        response.value = result;
      } catch (err) {
        error.value = 'Erro ao enviar dados: ' + err.message;
      } finally {
        loading.value = false;
      }
    };

    const enviarDadosParaPrever = async () => {
      loading.value = true;
      error.value = null;

      try {
        const dadosPaciente = {
          "W5A": 1,
          "W6": 2,
          "MH4A": 3,
          "subjective_Income": 4,
          "MH2A": 1,
          "MH3B": 2,
          "W11B": 2,
          "MH5": 1
        };

        const resposta = await fetch('https://tcc-mentalhealth.onrender.com/prever', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(dadosPaciente)
        });

        const resultado = await resposta.json();
        response.value = resultado;
        console.log('Resultado da previsão:', resultado);
      } catch (err) {
        error.value = 'Erro ao enviar dados de teste: ' + err.message;
        console.error('Erro:', err);
      } finally {
        loading.value = false;
      }
    };

    return {
      formData,
      response,
      error,
      loading,
      handleSubmit,
      enviarDadosParaPrever
    };
  }
};
</script>

<style scoped>
.data-form {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
}

.form-group {
  margin-bottom: 20px;
}

label {
  display: block;
  margin-bottom: 8px;
  font-weight: bold;
}

select {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 16px;
}

button {
  background-color: #4CAF50;
  color: white;
  padding: 12px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  width: 100%;
}

button:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
}

.test-section {
  margin-top: 30px;
  padding: 20px;
  background-color: #f8f9fa;
  border-radius: 4px;
  text-align: center;
}

.test-button {
  background-color: #2196F3;
  margin-top: 10px;
}

.response {
  margin-top: 20px;
  padding: 20px;
  background-color: #f5f5f5;
  border-radius: 4px;
}

.error {
  color: #d32f2f;
  margin-top: 10px;
  padding: 10px;
  background-color: #ffebee;
  border-radius: 4px;
}
</style>
