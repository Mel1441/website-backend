import { useState, useEffect } from 'react';
import LoginWrapper from '../../components/school/LoginWrapper';
import FormCard from '../../components/school/FormCard';
import InputGroup from '../../components/school/InputGroup';
import ErrorToast from '../../components/school/ErrorToast';
import LoadingOverlay from '../../components/school/LoadingOverlay';
import CTASection from '../../components/school/CTASection';



export default function LoginPage() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError]     = useState('');
  const [loading, setLoading] = useState(false);

  // read the right API URL
  const API_BASE = import.meta.env.VITE_API_BASE_URL;

  const handleLogin = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');

    try {
      const form = new URLSearchParams();
      form.append('username', username);
      form.append('password', password);
      console.log(API_BASE)
      const res = await fetch(`${API_BASE}/auth/auth/login`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: form,
      });

      const data = await res.json();
      if (!res.ok) throw new Error(data.detail || 'Login failed');

      localStorage.setItem('token', data.access_token);
      window.location.href = '/dashboard';
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
      <LoginWrapper>
  <FormCard>
    <form onSubmit={handleLogin}>
      <h2 className="text-2xl font-semibold text-center mb-4">
        Sign in to your account
      </h2>

      <InputGroup
        label="Username"
        type="text"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />

      <InputGroup
        label="Password"
        type="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />

      <CTASection loading={loading} />

      {error && <ErrorToast message={error} />}
    </form>
  </FormCard>

  {loading && <LoadingOverlay />}
</LoginWrapper>
  );
  
}
