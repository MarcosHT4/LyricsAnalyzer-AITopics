import profile from "../media/profile.jpg";
import {useState} from "react";
import {Button} from "@mui/material"
import api from "../api/songs";
import "react-circular-progressbar/dist/styles.css";
import {buildStyles, CircularProgressbar} from "react-circular-progressbar";

const Profile = () => {

    const [sentiment, setSentiment] = useState([])
    const [emotion, setEmotion] = useState([])
    const [songs, setSongs] = useState({})
    const [isLoading, setIsLoading] = useState(false)
    const [error, setError] = useState('')

    const countOccurences = (songs) => {
        let count = {}
        for (let i = 0; i < songs.length; i++) {
            count[songs[i]] = (count[songs[i]] || 0) + 1
        }
        return Object.entries(count).sort((x, y) => y[1] - x[1])
            .reduce((acc, [key, value]) => ({...acc, [key]: value}), {})
    }

    const handleSubmit = async(e) => {
        e.preventDefault()
        try {
            setIsLoading(true)
            const response = await api.get('/profile')
            setSongs(countOccurences(response.data.songs))
            console.log(countOccurences(response.data.songs))
            setSentiment(response.data.sentiment.scores)
            setEmotion(response.data.emotion.scores)
            window.scrollTo(0, 0)

        } catch (e) {
            setError(e.response.data.detail)

        } finally {
            setIsLoading(false)
        }

    }


    return sentiment.length !==0  ? (
        <main>
            <h1>Profile Results</h1>
            <h2>1. Your favorite songs</h2>
            <div className="div__introduction">
                {Object.keys(songs).map((song, idx) => (
                    <p key={idx} style={{fontSize:"1.5rem"}}>
                        {idx+1}. {song} - Played {songs[song]} {songs[song] === 1 ? 'time' : 'times'}
                    </p>
                ))}
            </div>
            <h2>2. The sentiment of your songs</h2>
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

                <h2>Your overall sentiment is more {sentiment[0].score > sentiment[1].score ? "positive than negative" : "negative than positive"}</h2>

            </div>
            <h2>3. Emotion Analysis</h2>
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

                <h2>Your favorite songs hide {emotion[0].label}, {emotion[1].label} and {emotion[2].label} within theirx lyrics</h2>

            </div>

            <div>

                <Button sx={{color: "white", padding:"16px"}} style={{backgroundColor:"purple", width:"200px"}} onClick={() => {
                    setSentiment([])
                    window.scrollTo(0, 0)
                }}>TRY AGAIN</Button>
            </div>
        </main>
    ):(
        <main>
            <h1>Profile Generator</h1>
            <div className="div__introduction">
                <img src={profile} alt="Profile Generator"
                     width="700" height="400"/>
                <p className="p__service-introduction">
                    Introducing our Personal Music Profile Generator, a revolutionary tool tailored to curate a unique
                    sonic fingerprint that mirrors the intricacies of your musical preferences. In a world where music
                    is a deeply personal journey, this generator transcends conventional playlists by harnessing the
                    power of artificial intelligence to distill the essence of your diverse tastes. By analyzing your
                    listening history, favorite genres, and mood preferences, it constructs a dynamic profile that
                    reflects the kaleidoscope of your musical identity. Whether you're navigating the peaks of upbeat
                    rhythms or immersing yourself in the introspective valleys of soulful ballads, this generator
                    tailors an audio landscape that resonates with your individuality. Join us on a personalized
                    musical odyssey, where your distinct preferences converge into a harmonious symphony, celebrating
                    the multifaceted tapestry of your unique musical journey.
                </p>

            </div>
            <h1>Get your musical profile</h1>

            <br/>
            <form className="form__sentiment-analysis" onSubmit={handleSubmit}>
                {error ? <p style={{color:"red"}}>{error}</p> : null}
                <Button sx={{color: "white", padding:"16px"}} style={{backgroundColor:"purple", width:"100px"}} type="submit" disabled={isLoading}>{isLoading ? "LOADING" : "SUBMIT"}</Button>
            </form>
        </main>
    );
};

export default Profile;