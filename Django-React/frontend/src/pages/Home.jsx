import { useState,  useEffect} from "react"
import api from "../api"

function Home(){

    const [notes, setNotes] = useState([]);
    const [content, setContent] = useState("");
    const [title, setTitle] = useState("");

    const getNotes = () => {
        api.get("/api/notes/")
        .then((res) => res.data)        // Extract the data (the actual notes) from the response object
        .then((data) => setNotes(data)) // Update the 'notes' state with the data we got from the server
        .catch((err) => alert(err))     // If something goes wrong (e.g. server is down), show an alert
    }

    return <div>Home</div>
}

export default Home