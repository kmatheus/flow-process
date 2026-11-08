import axios from 'axios';

// Cria a instância do Axios apontando para o backend
const api = axios.create({
  baseURL: 'http://localhost:8000/api/v1',
  headers: {
    'Content-Type': 'application/json',
  },
});

// Interceptor para adicionar o token automaticamente em todas as requisições
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('@FlowProcess:accessToken');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export default api;