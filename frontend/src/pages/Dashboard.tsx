import { useAuth } from '../contexts/AuthContext';

export function Dashboard() {
  const { user, signOut } = useAuth();

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <div className="max-w-4xl mx-auto">
        <div className="flex justify-between items-center mb-8">
          <h1 className="text-3xl font-bold text-gray-800">Dashboard</h1>
          <button
            onClick={signOut}
            className="bg-red-500 text-white px-4 py-2 rounded-md hover:bg-red-600"
          >
            Sair
          </button>
        </div>
        <div className="bg-white p-6 rounded-lg shadow-md">
          <p className="text-gray-600">Bem-vindo, <strong>{user}</strong>!</p>
          <p className="text-gray-500 mt-2">O sistema está funcionando.</p>
        </div>
      </div>
    </div>
  );
}