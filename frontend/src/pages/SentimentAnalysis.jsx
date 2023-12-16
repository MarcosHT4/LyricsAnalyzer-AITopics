import sentimentAnalysis from "../media/sentimentAnalysis.jpg";
import  {useState} from "react";
import {Button, inputLabelClasses, TextField} from "@mui/material"
import api from "../api/songs";
import {CircularProgressbar, buildStyles} from "react-circular-progressbar";
import "react-circular-progressbar/dist/styles.css";

const SentimentAnalysis = () => {

    const [link, setLink] = useState('')
    const [sentiment, setSentiment] = useState([])
    const [song, setSong] = useState('')
    const [artist, setArtist] = useState('')
    const [error, setError] = useState('')
    const handleSubmit = async(e) => {
        console.log(link)
        e.preventDefault()
        try {
            const response = await api.post('/sentiment_url', {song_url: link})
            setSentiment(response.data.analysis.scores)
            setSong(response.data.name)
            setArtist(response.data.artist)
            console.log(response.data.analysis.scores)
        } catch(e) {
            setError(e.response.data.detail)
        }



    }


    return sentiment.length !==0  ? (
        <main>
            <h1>Sentiment Results</h1>
            <div className="div__introduction">
                <div className="div__sentiment-results" style={{ width: 1000, height: 400 }}>
                    {sentiment.map((score, idx)  => (
                        <div key = {idx} className ="div__progress">
                        <CircularProgressbar key = {idx} value={score.score} maxValue={1} text={`${Math.round(score.score*100)}%`}
                        styles={buildStyles({
                            rotation: 0.25,
                            strokeLinecap: 'butt',
                            textSize: '16px',
                            pathTransitionDuration: 1,
                            pathColor: `${idx === 0 ? '#008000' : '#FF0000'}`,
                            textColor: '#FFFFFF',
                            trailColor: '#d6d6d6',
                            backgroundColor: '#3e98c7',
                     })}/>
                        <h2 >{score.label}</h2>
                        </div>
                    ))}
                </div>

                <h2>The song {song} by {artist} is more {sentiment[0].score > sentiment[1].score ? "positive than negative" : "negative than positive"}</h2>

                <Button sx={{color: "white", padding:"16px"}} style={{backgroundColor:"purple", width:"200px"}} onClick={() => {setSentiment([])}}>TRY AGAIN</Button>

            </div>
        </main>
    ):(
        <main>
            <h1>Sentiment Analysis</h1>
            <div className="div__introduction">
                <img src={sentimentAnalysis} alt="Sentiment Analysis"
                     width="700" height="400"/>
                <p className="p__service-introduction">
                    Introducing the Song Sentiment Analyzer, a revolutionary tool that unravels the emotional tapestry of
                    your favorite tunes. Music has the power to evoke a myriad of feelings, and our innovative technology
                    is here to decode the sentiments embedded within each melody and lyric. Whether you seek the euphoria
                    of uplifting anthems, the melancholy of soulful ballads, or the energy of upbeat tracks, our analyzer goes beyond the surface, delving into the heart of music to capture its emotional essence. Join us
                    on a journey to explore the sentiments that resonate with you, as we unveil the hidden emotions woven
                    into the fabric of every song, bringing a new dimension to your musical experience.
                </p>

            </div>
            <h1>Get the sentiment of your favorite song!</h1>
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

export default SentimentAnalysis;