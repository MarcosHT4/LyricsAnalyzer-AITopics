import meaningAnalysis from "../media/meaningAnalysis.jpg";
import  {useState} from "react";
import {Button, inputLabelClasses, TextField} from "@mui/material"
import api from "../api/songs";
import "react-circular-progressbar/dist/styles.css";

const MeaningAnalysis = () => {

    const [link, setLink] = useState('')
    const [meaning, setMeaning] = useState([])
    const [song, setSong] = useState('')
    const [artist, setArtist] = useState('')
    const [isLoading, setIsLoading] = useState(false)
    const [error, setError] = useState('')
    const handleSubmit = async(e) => {
        e.preventDefault()
        try {
            setIsLoading(true)
            const response = await api.post('/meaning_url', {song_url: link})
            setMeaning(response.data.meaning.sections)
            setSong(response.data.name)
            setArtist(response.data.artist)

        } catch (e) {
            setError(e.response.data.detail)

        } finally {
            setIsLoading(false)
        }

    }


    return meaning.length !==0  ? (
        <main>
            <h1>Meaning Results</h1>
            <h2>The meaning of the song {song} by {artist} is: </h2>
            <div>
                    {meaning.map((section, idx)  => (
                        <div key = {idx} className ="div__sections">
                            <h1>{idx+1}. {section.section}</h1>
                            <p style={{fontSize:"1.2rem"}}>
                                {section.meaning}
                            </p>
                        </div>

                    ))}
                <Button sx={{color: "white", padding:"16px"}} style={{backgroundColor:"purple", width:"200px"}} onClick={() => {setMeaning([])}}>TRY AGAIN</Button>

            </div>
        </main>
    ):(
        <main>
            <h1>Meaning Analysis</h1>
            <div className="div__introduction">
                <img src={meaningAnalysis} alt="Meaning Analysis"
                     width="700" height="400"/>
                <p className="p__service-introduction">
                    Welcome to the Song Meaning Analyzer, an enlightening tool designed to unravel the cryptic
                    narratives and poetic expressions embedded within the lyrics of your favorite tunes. In a world
                    where songs serve as vessels for profound stories and poignant messages, this analyzer acts as a
                    literary guide, decoding the lyrical complexities that often escape casual listeners. Beyond the
                    beats and melodies, we invite you to explore the rich tapestry of meanings woven into each verse
                    and chorus. Whether its the introspective reflections of a singer-songwriter or the allegorical tales
                    spun by a band, our analyzer aims to demystify the lyrical enigma, offering insights into the deeper
                    layers of expression that make each song a unique and compelling work of art. Join us in unlocking
                    the hidden narratives that echo through the chords and words, revealing the captivating stories that
                    linger within the melodies.
                </p>

            </div>
            <h1>Get the meaning  of your favorite song!</h1>
            <p className="p__service-introduction">Input the GENIUS link to your song lyrics!</p>
            <br/>
            <form className="form__sentiment-analysis" onSubmit={handleSubmit}>
                <TextField
                    id="outlined-required"
                    label="Genius Link"
                    sx={{input: {color: 'white'}}}
                    value={link}
                    onChange={(e) => setLink(e.target.value)}
                    InputLabelProps={{
                        sx: {
                            // set the color of the label when not shrinked
                            color: "white",
                            [`&.${inputLabelClasses.shrink}`]: {
                                // set the color of the label when shrinked (usually when the TextField is focused)
                                color: "white"
                            }
                        }
                    }}
                    style={{color: 'white', width:"50%"}}
                />
                {error ? <p style={{color:"red"}}>{error}</p> : null}
                <Button sx={{color: "white", padding:"16px"}} style={{backgroundColor:"purple", width:"100px"}} type="submit" disabled={isLoading}>{isLoading ? "LOADING" : "SUBMIT"}</Button>
            </form>
        </main>
    );
};

export default MeaningAnalysis;