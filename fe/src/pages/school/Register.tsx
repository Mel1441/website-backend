import { useState } from "react";
import { registerUser } from "@/services/authService";

export default function RegisterForm() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [role, setRole] = useState("learner");
  const [message, setMessage] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const result = await registerUser({ email, password, role });
    setMessage(result.success ? "User created!" : result.message || "Error");
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Register</h2>
      <input type="email" value={email} onChange={e => setEmail(e.target.value)} placeholder="Email" required />
      <input type="password" value={password} onChange={e => setPassword(e.target.value)} placeholder="Password" required />
      <select value={role} onChange={e => setRole(e.target.value)}>
        <option value="learner">Learner</option>
        <option value="admin">Admin</option>
      </select>
      <button type="submit">Register</button>
      {message && <p>{message}</p>}
    </form>
  );
}