import imageDescriptionP from "../media/imageDescriptionP.jpeg";
import  {useState} from "react";
import {Button} from "@mui/material"
import api from "../api/songs";
import "react-circular-progressbar/dist/styles.css";

const ImageDescription = () => {

    const [file, setFile] = useState(null)
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
            formData.append('file', file)
            convertToBase64(file)
            const response = await api.post('/cover-description', formData)
            console.log(response.data)
            setImageDescription(response.data)
            window.scrollTo(0, 0)

        } catch (e) {
            setError(e.response.data.detail)

        } finally {
            setIsLoading(false)
        }

    }


    return imageDescription !== ''  ? (
        <main>
            <h1>Song Cover Art Description Results</h1>
            <div className="div__introduction">
                <img src={base64IMG} alt="Meaning Analysis"/>
                <p style={{fontSize:"1.2rem"}}>
                    {imageDescription }
                </p>
            </div>
            <Button sx={{color: "white", padding:"16px"}} style={{backgroundColor:"purple", width:"200px"}} onClick={() => {
                setImageDescription('')
                window.scrollTo(0, 0)
            }}>TRY AGAIN</Button>
        </main>
    ):(
        <main>
            <h1>Song Cover Art Description</h1>
            <div className="div__introduction">
                <img src={imageDescriptionP} alt="Song Convert Art Analysis"
                     width="700" height="400"/>
                <p className="p__service-introduction">

                    Welcome to the Song Cover Art Analyzer, a cutting-edge tool designed to unravel the visual
                    narratives embedded within the album and single covers that complement your favorite tunes.
                    In a world where album art is a captivating gateway to the soul of music, this analyzer invites
                    you to explore the evocative imagery that accompanies each track. By dissecting the symbolism,
                    color palette, and design elements, we delve into the visual language that artists use to enhance
                    and complement their musical creations. Whether it's the enigmatic allure of a minimalist design
                    or the vibrant chaos of an abstract masterpiece, our analyzer decodes the visual poetry, offering
                    insights into the artistic choices that shape the aesthetic identity of a song. Join us in unlocking
                    the hidden visual stories that dance alongside the melodies, adding a new layer of appreciation to
                    the immersive experience of your favorite music.
                </p>

            </div>
            <h1>Get the description of your favorite song's cover art!</h1>

            <br/>
            <p className="p__service-introduction">Input the GENIUS link to your song lyrics!</p>
            <form className="form__sentiment-analysis" onSubmit={handleSubmit}>
                <p className="p__service-introduction">Upload the song's album cover!</p>
                <input type="file" onChange={handleFileInputChange}/>
                {error ? <p style={{color:"red"}}>{error}</p> : null}
                <Button sx={{color: "white", padding:"16px"}} style={{backgroundColor:"purple", width:"100px"}} type="submit" disabled={isLoading}>{isLoading ? "LOADING" : "SUBMIT"}</Button>
            </form>
        </main>
    );
};

export default ImageDescription;