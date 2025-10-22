import axios from 'axios';

// Usar sempre /api (proxy do Vite em dev, proxy do Vercel em prod)
const API_URL = '/api';

console.log('🌍 Usando proxy:', API_URL);

const api = axios.create({
    baseURL: API_URL,
    headers: {
        'Content-Type': 'application/json'
    }
});

export const sendDataToBackend = async (data) => {
    try {
        console.log('📤 Enviando dados para a rota:', API_URL + '/predict');
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
