import axios from 'axios';

// URL base usando o proxy do Vite
const API_URL = '/api';

const api = axios.create({
    baseURL: API_URL,
    headers: {
        'Content-Type': 'application/json'
    }
});

export const sendDataToBackend = async (data) => {
    try {
        const response = await api.post('/predict', data);
        return response.data;
    } catch (error) {
        console.error('Erro ao enviar dados para o backend:', error);
        throw error;
    }
};

export default api;
