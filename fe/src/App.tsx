import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import LoginForm from './pages/school/Login';
import Dashboard from './pages/school/Dashboard';
import LearnerProfile from './pages/school/LearnerProfile'

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/school/login" element={<LoginForm />} />
        <Route path="/school/dashboard" element={<Dashboard />} />
        <Route path="/school/profile" element={<LearnerProfile />} />
      </Routes>
    </Router>
  );
}

export default App;
