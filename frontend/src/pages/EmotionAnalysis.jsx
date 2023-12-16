import emotionAnalysis from "../media/emotionAnalysis.jpg";
import  {useState} from "react";
import {Button, inputLabelClasses, TextField} from "@mui/material"
import api from "../api/songs";
import {CircularProgressbar, buildStyles} from "react-circular-progressbar";
import "react-circular-progressbar/dist/styles.css";

const EmotionAnalysis = () => {

    const [link, setLink] = useState('')
    const [emotion, setEmotion] = useState([])
    const [song, setSong] = useState('')
    const [artist, setArtist] = useState('')
    const [error, setError] = useState('')
    const handleSubmit = async(e) => {
        console.log(link)
        e.preventDefault()
        try {
            const response = await api.post('/emotion_url', {song_url: link})
            setEmotion(response.data.analysis.scores)
            setSong(response.data.name)
            setArtist(response.data.artist)
            console.log(response.data.analysis.scores)
        } catch(e) {
            setError(e.response.data.detail)
        }



    }


    return emotion.length !==0  ? (
        <main>
            <h1>Emotion Results</h1>
            <div className="div__introduction">
                <div className="div__sentiment-results" style={{ width: 1000, height: 400 }}>
                    {emotion.map((score, idx)  => (
                        <div key = {idx} className ="div__progress">
                            <CircularProgressbar key = {idx} value={score.score} maxValue={1} text={`${Math.round(score.score*100)}%`}
                                                 styles={buildStyles({
                                                     rotation: 0.25,
                                                     strokeLinecap: 'butt',
                                                     textSize: '16px',
                                                     pathTransitionDuration: 1,
                                                     pathColor: `rgba(62, 152, 199, ${score.score})})`,
                                                     textColor: '#FFFFFF',
                                                     trailColor: '#d6d6d6',
                                                     backgroundColor: '#3e98c7',
                                                 })}/>
                            <h2 >{score.label.toUpperCase()}</h2>
                        </div>

                    ))}

                </div>

                <h2>The song {song} by {artist} hides {emotion[0].label}, {emotion[1].label} and {emotion[2].label} within its lyrics</h2>

                <Button sx={{color: "white", padding:"16px"}} style={{backgroundColor:"purple", width:"200px"}} onClick={() => {setEmotion([])}}>TRY AGAIN</Button>

            </div>
        </main>
    ):(
        <main>
            <h1>Emotion Analysis</h1>
            <div className="div__introduction">
                <img src={emotionAnalysis} alt="Emotion Analysis"
                     width="700" height="400"/>
                <p className="p__service-introduction">
                    Introducing the Song Emotions Analyzer, a groundbreaking tool that delves into the very heart of
                    music, deciphering the intricate tapestry of emotions woven into every note and lyric. In a world
                    where melodies speak a language of their own, this innovative analyzer serves as a musical compass,
                    navigating the vast spectrum of human emotions encapsulated within each composition. Whether its
                    the soul-stirring resonance of a ballad or the pulsating energy of an upbeat track, our analyzer
                    goes beyond mere sound, offering a profound exploration into the emotional landscapes crafted by
                    artists. Join us on a journey through the evocative power of music as we uncover the sentiments
                    that lie beneath the surface, providing a new dimension to the way we experience and understand
                    the songs that soundtrack our lives.
                </p>

            </div>
            <h1>Get the emotion of your favorite song!</h1>
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
                <Button sx={{color: "white", padding:"16px"}} style={{backgroundColor:"purple", width:"100px"}} type="submit">SUBMIT</Button>
            </form>
        </main>
    );
};

export default EmotionAnalysis;