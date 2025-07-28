// Import axios library for making HTTP requests
import axios from "axios";

// Import the key name used to store the access token in localStorage
import { ACCESS_TOKEN } from "./constants";

// Create an axios instance with a base URL from environment variables
// Example: VITE_API_URL = 'http://localhost:8000/api'
const api = axios.create({
    baseURL: import.meta.env.VITE_API_URL
});

// Add an interceptor to attach the access token to every request (if it exists)
api.interceptors.request.use(
    (config) => {
        // Get the access token from localStorage
        const token = localStorage.getItem(ACCESS_TOKEN);

        // If token exists, add it to the Authorization header
        if (token) {
            config.headers.Authorization = `Bearer ${token}`;
            // This sets: Authorization: Bearer <your_token>
        }

        // Always return the config so the request can continue
        return config;
    },
    (error) => {
        // If there's an error before sending the request, reject the Promise
        return Promise.reject(error);
    }
);

// Export the custom axios instance for use in your app
export default api;
