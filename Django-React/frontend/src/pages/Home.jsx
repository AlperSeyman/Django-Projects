import { useState, useEffect } from "react"; // React hooks to manage state and lifecycle
import api from "../api"; // Axios instance to make API requests
import Note from "../components/Notes"
import "../styles/Home.css"

function Home() {
    // State to hold list of notes
    const [notes, setNotes] = useState([]);

    // State for form inputs: title and content of the note
    const [title, setTitle] = useState("");
    const [content, setContent] = useState("");

    // useEffect runs once when the component mounts (because of empty dependency array [])
    useEffect(() => {
        getNotes(); // Call the function to fetch all notes from backend
    }, []);

    // Fetch all notes from the API
    const getNotes = () => {
        api
            .get("/api/notes/") // Send GET request to this endpoint
            .then((res) => res.data) // Extract the data from the response
            .then((data) => {
                setNotes(data); // Save the notes in state
                console.log(data); // Optional: log the notes in browser console
            })
            .catch((err) => alert(err)); // Show alert if something goes wrong
    };

    // Delete a note with given ID
    const deleteNote = (id) => {
        api
            .delete(`/api/notes/delete/${id}/`) // Send DELETE request to delete specific note
            .then((res) => {
                if (res.status === 204) alert("Note deleted!"); // 204 means deleted successfully
                else alert("Failed to delete note.");
                getNotes(); // Refresh the list after deletion
            })
            .catch((error) => alert(error)); // Show alert if deletion fails
    };

    // Create a new note when the form is submitted
    const createNote = (e) => {
        e.preventDefault(); // Prevent the default form submit (which would reload the page)
        api
            .post("/api/notes/", { title, content }) // Send POST request with form data
            .then((res) => {
                if (res.status === 201) alert("Note created!"); // 201 means created successfully
                else alert("Failed to make note.");
                getNotes(); // Refresh the list after creating a note
            })
            .catch((err) => alert(err)); // Show alert if creation fails
    };

    // JSX returned to render the page
    return (
        <div>
            <div>
                <h2>Notes</h2> {/* Heading for the notes section */}
                {notes.map((note) => <Note note={note} onDelete={deleteNote} key={note.id}/>)}
            </div>
            <h2>Create a Note</h2> {/* Heading for the form */}
            <form onSubmit={createNote}> {/* Form that calls createNote on submit */}
                <label htmlFor="title">Title:</label>
                <br />
                <input
                    type="text"
                    id="title"
                    name="title"
                    required
                    onChange={(e) => setTitle(e.target.value)} // Update title state as user types
                    value={title} // Controlled input (value comes from state)
                />
                <label htmlFor="content">Content:</label>
                <br />
                <textarea
                    id="content"
                    name="content"
                    required
                    value={content} // Controlled input (value comes from state)
                    onChange={(e) => setContent(e.target.value)} // Update content state as user types
                ></textarea>
                <br />
                <input type="submit" value="Submit"></input> {/* Submit button */}
            </form>
        </div>
    );
}

export default Home; // Export Home component so it can be used elsewhere
