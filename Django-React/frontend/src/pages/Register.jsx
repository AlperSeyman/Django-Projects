import Form from "../components/Form"


function Register(){
    // - `route`: the API endpoint to send registration data to (with trailing slash!)
    // - `method`: a string that tells the Form to behave like a registration form
    return <Form route="/api/user/register/" method="register"/>
}

export default Register