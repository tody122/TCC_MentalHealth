import axios from 'axios';

// Usar proxy local para evitar problemas de CORS
const API_URL = '/api';

const api = axios.create({
    baseURL: API_URL,
    headers: {
        'Content-Type': 'application/json'
    }
});

export const sendDataToBackend = async (data) => {
    try {
        console.log('Enviando dados via proxy:', data);
        const response = await api.post('/predict', data);
        console.log('Resposta recebida:', response.data);
        return response.data;
    } catch (error) {
        console.error('Erro ao enviar dados para o backend:', error);
        console.error('Detalhes do erro:', {
            message: error.message,
            code: error.code,
            status: error.response?.status,
            statusText: error.response?.statusText
        });
        throw error;
    }
};

export default api;
