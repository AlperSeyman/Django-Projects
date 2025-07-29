import Form from "../components/Form"

function Login(){
    // - `route`: the API endpoint to send registration data to (with trailing slash!)
    // - `method`: a string that tells the Form to behave like a login form
    return <Form route="/api/token/" method="login"/>
}

export default Login