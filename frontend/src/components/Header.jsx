import {AppBar, Container, Toolbar, Typography ,Box, Button} from "@mui/material";

const pages = ['Sentiment', 'Emotion', 'Meaning','Image-Description' ,'Analysis','Profile']
import {useNavigate} from "react-router-dom";


const Header = () => {
    const navigate = useNavigate()
    return (
        <header>
            <AppBar color="secondary" className='appbar'>
                <Container maxWidth='x1'>
                    <Toolbar disableGutters >

                        <Typography
                            className='header__title'
                            variant="h6"
                            noWrap
                            sx={{
                                mr: 2,
                                flexGrow: 8,
                                display: { xs: 'none', md: 'flex' },
                                fontFamily: 'monospace',
                                fontWeight: 700,
                                letterSpacing: '.3rem',
                                color: 'inherit',
                                textDecoration: 'none',
                            }}
                        >
                            LYRIC ANALYZER
                        </Typography>
                        <Box sx={{ flexGrow: 1, display: { xs: 'none', md: 'flex' } }}>
                            {pages.map((page) => (
                                <Button
                                    key={page}
                                    sx={{ my: 2, color: 'white', display: 'block' }}
                                    onClick={(e) => {
                                        navigate("/" + page.toLowerCase())
                                    }}
                                >
                                    {page}
                                </Button>
                            ))}
                        </Box>
                    </Toolbar>
                </Container>
            </AppBar>
            
        </header>
    );
};

export default Header;