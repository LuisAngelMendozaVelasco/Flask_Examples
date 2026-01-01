import './App.css'
import Navbar from './components/Navbar';
import About from './components/About';
import Home from './components/Home';
import Users from './components/Users';
import Alerts from './components/Alerts';
import Update from './components/Update';
import 'bootswatch/dist/darkly/bootstrap.min.css'
import { BrowserRouter as Router, Route, Routes, useLocation } from 'react-router-dom';
import { AlertProvider, useAlert } from './contexts/AlertContext';
import { useEffect } from 'react';

function AppContent() {
  const location = useLocation();
  const { setAlertMessage } = useAlert();

  useEffect(() => {setAlertMessage('');}, [location.pathname, setAlertMessage]);

  return (
    <>
      <Navbar />
      <Alerts />
      <Routes>
        <Route index element={<Home />} />
        <Route path="users" element={<Users />} />
        <Route path="update/:userId" element={<Update />} />
        <Route path="about" element={<About />} />
      </Routes>
    </>
  );
}

function App() {
  return (
    <AlertProvider>
      <Router>
        <AppContent />
      </Router>
    </AlertProvider>
  );
}

export default App