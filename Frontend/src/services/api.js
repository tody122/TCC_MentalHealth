import axios from 'axios';

// Detectar se está em desenvolvimento ou produção
const isDevelopment = import.meta.env.DEV;
const API_URL = isDevelopment ? '/api' : 'https://tcc-mentalhealth.onrender.com';

console.log('🌍 Ambiente:', isDevelopment ? 'Desenvolvimento' : 'Produção');
console.log('🔗 API URL:', API_URL);

const api = axios.create({
    baseURL: API_URL,
    headers: {
        'Content-Type': 'application/json'
    }
});

export const sendDataToBackend = async (data) => {
    try {
        console.log('📤 Enviando dados para:', API_URL + '/predict');
        console.log('📤 Dados:', data);
        const response = await api.post('/predict', data);
        console.log('✅ Resposta recebida:', response.data);
        return response.data;
    } catch (error) {
        console.error('❌ Erro ao enviar dados para o backend:', error);
        console.error('❌ Detalhes do erro:', {
            message: error.message,
            code: error.code,
            status: error.response?.status,
            statusText: error.response?.statusText,
            url: error.config?.url
        });
        throw error;
    }
};

export default api;
