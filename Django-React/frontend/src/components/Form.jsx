import { useState } from "react";              // Import React hook to manage component state
import api from "../api";                      // Import custom axios instance for API requests
import { useNavigate } from "react-router-dom"; // Import navigation hook to programmatically change pages
import { ACCESS_TOKEN, REFRESH_TOKEN } from "../constants"; // Import token keys for localStorage
import "../styles/Form.css"
import Loading from "./Loading";

// The Form component receives two props:
//  - route: the API endpoint to send the form data to (e.g., "api/login/")
//  - method: determines if this is a "login" or "register" form
function Form({route, method}) {
    // State variables for the form inputs and loading state
    const [username, setUsername] = useState("");  // Store username input, initially empty
    const [password, setPassword] = useState("");  // Store password input, initially empty
    const [loading, setLoading] = useState(false); // Track if form is currently submitting

    // Hook to programmatically redirect user to different pages
    const navigate = useNavigate();

    // Function called when form is submitted
    const handleSubmit = async (e) => {
        setLoading(true);           // Start loading (disable form/buttons if needed)
        e.preventDefault();         // Prevent default form submit that reloads page

        try {
            // Send POST request to the API with username and password data
            const response = await api.post(route, { username, password });

            // If method is "login", save tokens and redirect to home page
            if (method === "login") {
                localStorage.setItem(ACCESS_TOKEN, response.data.access);    // Save access token in localStorage
                localStorage.setItem(REFRESH_TOKEN, response.data.refresh);  // Save refresh token in localStorage
                navigate("/");  // Redirect user to home page
            } else {
                // If method is "register", redirect user to login page after registration
                navigate("/login");
            }
        } catch (error) {
            alert(error);   // Show error message if API request fails
        } finally {
            setLoading(false); // Stop loading state whether success or failure
        }
    };

    // Set the form title and button text dynamically based on method
    const name = method === "login" ? "Login" : "Register";

    // Render the form JSX
    return (
        <form onSubmit={handleSubmit} className="form-container">
            <h1>{name}</h1> {/* Display form title */}
            {/* Username input box */}
            <input
                type="text"
                className="form-input"
                value={username}                          // Controlled input linked to username state
                onChange={(e) => setUsername(e.target.value)}  // Update username state on typing
                placeholder="username"                    // Placeholder text
            />
            {/* Password input box */}
            <input
                type="password"
                className="form-input"
                value={password}                          // Controlled input linked to password state
                onChange={(e) => setPassword(e.target.value)}  // Update password state on typing
                placeholder="password"                    // Placeholder text
            />
            {/* Submit button */}
            {Loading && <Loading />}
            <button className="form-button" type="submit">
                {name}  {/* Button text based on method */}
            </button>
        </form>
    );
}

export default Form