// Import necessary libraries and helpers
import { Navigate } from "react-router-dom"; // For redirecting to another route
import { jwtDecode } from "jwt-decode";       // For decoding the access token
import api from "../api";                     // Custom Axios instance
import { REFRESH_TOKEN, ACCESS_TOKEN } from "../constants"; // Token storage keys
import { useState, useEffect } from "react";  // React hooks

// This component protects a route: only shows the children if user is authenticated
function ProtectedRoute({ children }) {

    // This hook runs once when the component is first rendered
    useEffect(() => {
        auth().catch(() => setIsAuthorized(false));
    }, []);

    // React state: null = loading, true = authorized, false = not authorized
    const [isAuthorized, setIsAuthorized] = useState(null);

    // Function to refresh the access token using the refresh token
    const refreshToken = async () => {
        const refresToken = localStorage.getItem(REFRESH_TOKEN); // Get refresh token
        try {
            // Try sending refresh request to the API
            const res = await api.post("api/token/refresh/", { refresh: refresToken });

            if (res.status == 200) {
                // If success, save new access token
                localStorage.setItem(ACCESS_TOKEN, res.data.access);
                setIsAuthorized(true); // Allow access
            } else {
                setIsAuthorized(false); // Deny access
            }
        } catch (error) {
            // If an error happens (like expired refresh token)
            console.log(error);
            setIsAuthorized(false); // Deny access
        }
    };

    // Main function to check if user is authenticated
    const auth = async () => {
        const token = localStorage.getItem(ACCESS_TOKEN); // Get access token
        if (!token) {
            setIsAuthorized(false); // No token = not logged in
            return;
        }

        const decoded = jwtDecode(token);         // Decode token to get expiry time
        const tokenExpiration = decoded.exp;      // Get expiration timestamp
        const now = Date.now() / 1000;            // Current time in seconds

        if (tokenExpiration < now) {
            // If token is expired, try refreshing it
            await refreshToken();
        } else {
            setIsAuthorized(true); // Token still valid → allow access
        }
    };

    // While checking auth status, show a loading message
    if (isAuthorized === null) {
        return <div>Loading</div>;
    }

    // If authorized, show the requested (child) component
    if (isAuthorized) {
        return children;
    } else {
        // If not authorized, redirect to the login page
        return <Navigate to="/login" replace />;
    }
}

export default ProtectedRoute;
