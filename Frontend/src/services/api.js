import axios from "axios";

const API = axios.create({
  baseURL: "https://password-security-toolkit-production.up.railway.app",
});

export default API;