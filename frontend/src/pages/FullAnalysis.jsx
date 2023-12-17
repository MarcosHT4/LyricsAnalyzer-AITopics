import fullAnalysis from "../media/fullAnalysis.jpg";
import  {useState} from "react";
import {Button, inputLabelClasses, TextField} from "@mui/material"
import api from "../api/songs";
import "react-circular-progressbar/dist/styles.css";
import {buildStyles, CircularProgressbar} from "react-circular-progressbar";

const MeaningAnalysis = () => {

    const [link, setLink] = useState('')
    const [file, setFile] = useState(null)
    const [meaning, setMeaning] = useState([])
    const [sentiment, setSentiment] = useState([])
    const [emotion, setEmotion] = useState([])
    const [song, setSong] = useState('')
    const [artist, setArtist] = useState('')
    const [imageDescription, setImageDescription] = useState('')
    const [isLoading, setIsLoading] = useState(false)
    const [base64IMG, setBase64IMG] = useState('')
    const [error, setError] = useState('')

    const convertToBase64 = (image) => {
        const reader = new FileReader()
        reader.readAsDataURL(image)
        reader.onload = () => {
            setBase64IMG(reader.result)
        }
    }
    const handleFileInputChange = (e) => {
        e.preventDefault()
        console.log(e.target.files[0])
        setFile(e.target.files[0])

    }
    const handleSubmit = async(e) => {
        e.preventDefault()
        try {
            setIsLoading(true)
            const formData = new FormData()
            formData.append('image', file)
            convertToBase64(file)
            formData.append('song_url', link)
            const response = await api.post('/analysis_url', formData)
            console.log(response.data)
            setMeaning(response.data.meaning.sections)
            setSentiment(response.data.sentiment.scores)
            setEmotion(response.data.emotion.scores)
            setImageDescription(response.data.image_description)
            setSong(response.data.name)
            setArtist(response.data.artist)
            window.scrollTo(0, 0)

        } catch (e) {
            setError(e.response.data.detail)

        } finally {
            setIsLoading(false)
        }

    }


    return meaning.length !==0  ? (
        <main>
            <h1>Analysis Results</h1>
            <h2>1. Sentiment Analysis</h2>
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

            </div>
            <h2>2. Emotion Analysis</h2>
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

            </div>
            <h2>3. Image Description</h2>
            <div className="div__introduction">
                <img src={base64IMG} alt="Meaning Analysis"/>
                <p style={{fontSize:"1.2rem"}}>
                    {imageDescription }
                </p>
            </div>
            <h2>4. Meaning Analysis</h2>
            <div>
                {meaning.map((section, idx)  => (
                    <div key = {idx} className ="div__sections">
                        <h3>{idx+1}. {section.section.toUpperCase()}</h3>
                        <p style={{fontSize:"1.2rem"}}>
                            {section.meaning}
                        </p>
                    </div>

                ))}
                <Button sx={{color: "white", padding:"16px"}} style={{backgroundColor:"purple", width:"200px"}} onClick={() => {
                    setMeaning([])
                    window.scrollTo(0, 0)
                }}>TRY AGAIN</Button>
            </div>
        </main>
    ):(
        <main>
            <h1>Full Analysis</h1>
            <div className="div__introduction">
                <img src={fullAnalysis} alt="Full Analysis"
                     width="700" height="400"/>
                <p className="p__service-introduction">
                    Step into the realm of comprehensive musical exploration with our Full Song Analyzer—a
                    sophisticated tool crafted for those who seek a profound understanding of every facet of a
                    composition. More than just a melody decipherer or lyric interpreter, this analyzer is your
                    passport to a holistic understanding of the musical journey. From the intricate interplay of
                    instruments to the nuanced dynamics of rhythm and tempo, we delve into the sonic architecture
                    that defines each track. Simultaneously, we unravel the lyrical poetry, exposing the narrative
                    threads that bind the songs emotional core. This all-encompassing analysis offers an immersive
                    experience, unveiling the synergy between music and lyrics, allowing you to appreciate the intricate
                    craftsmanship behind every song. Join us in a musical odyssey where we dissect, appreciate,
                    and celebrate the entirety of the sonic tapestry, offering you a deeper connection to the artistry
                    that resonates through each note and verse.
                </p>

            </div>
            <h1>Get a full analysis of your favorite song!</h1>

            <br/>
            <p className="p__service-introduction">Input the GENIUS link to your song lyrics!</p>
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
                <p className="p__service-introduction">Upload the song's album cover!</p>
                <input type="file" onChange={handleFileInputChange}/>
                {error ? <p style={{color:"red"}}>{error}</p> : null}
                <Button sx={{color: "white", padding:"16px"}} style={{backgroundColor:"purple", width:"100px"}} type="submit" disabled={isLoading}>{isLoading ? "LOADING" : "SUBMIT"}</Button>
            </form>
        </main>
    );
};

export default MeaningAnalysis;