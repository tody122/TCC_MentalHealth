import axios from 'axios';

// URL base do backend
const API_URL = 'https://api-mental-health.onrender.com';

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
