import {Typography} from "@mui/material";
import lyricAnalyzer from "../media/lyricAnalyzer.jpg";


const HomePage = () => {
    return (
        <main className="main__home-page">

            <Typography
                className='header__title'
                variant="h3"
                noWrap
                sx={{
                    fontFamily: 'monospace',
                    fontWeight: 700,
                    letterSpacing: '.3rem',
                    color: 'inherit',
                    textDecoration: 'none',
                }}
            >
                LYRIC ANALYZER
            </Typography>
            <img src={lyricAnalyzer} alt="Lyric Analyer Art "
                 width="700" height="400"/>


        </main>
    );
};

export default HomePage;