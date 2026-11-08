import { createContext, useState, useContext, ReactNode } from 'react';
import api from '../services/api';

interface AuthContextData {
  user: string | null;
  signIn: (email: string, senha: string) => Promise<void>;
  signOut: () => void;
  isAuthenticated: boolean;
}

interface AuthProviderProps {
  children: ReactNode;
}

const AuthContext = createContext<AuthContextData>({} as AuthContextData);

export function AuthProvider({ children }: AuthProviderProps) {
  const [user, setUser] = useState<string | null>(null);

  async function signIn(email: string, senha: string) {
    try {
      // Cria o FormData nativo (não URLSearchParams)
      const formData = new URLSearchParams();
      formData.append('username', email);
      formData.append('password', senha);

      const response = await api.post('/auth/login', formData.toString(), {
        headers: { 
          'Content-Type': 'application/x-www-form-urlencoded',
        },
      });

      const { access_token, refresh_token } = response.data;

      localStorage.setItem('@FlowProcess:accessToken', access_token);
      localStorage.setItem('@FlowProcess:refreshToken', refresh_token);

      setUser(email);
    } catch (error: any) {
      console.error('Erro no login:', error.response?.data || error.message);
      throw new Error(error.response?.data?.detail || 'Email ou senha incorretos');
    }
  }

  function signOut() {
    localStorage.removeItem('@FlowProcess:accessToken');
    localStorage.removeItem('@FlowProcess:refreshToken');
    setUser(null);
  }

  return (
    <AuthContext.Provider value={{ user, signIn, signOut, isAuthenticated: !!user }}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  return useContext(AuthContext);
}