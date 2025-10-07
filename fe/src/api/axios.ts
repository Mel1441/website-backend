import axios from 'axios';
//import os;
//from dotenv import load_dotenv;


const baseURL = import.meta.env.VITE_API_BASE_URL;



const api = axios.create({

//  baseURL : 'http://localhost:8000/auth/login',
  baseURL: import.meta.env.VITE_API_URL,
  withCredentials: true,
});

export default api;