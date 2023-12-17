import {Route, Routes} from 'react-router-dom';
import Layout from "./components/Layout.jsx";
import SentimentAnalysis from "./pages/SentimentAnalysis.jsx";
import EmotionAnalysis from "./pages/EmotionAnalysis.jsx";
import MeaningAnalysis from "./pages/MeaningAnalysis.jsx";
import FullAnalysis from "./pages/FullAnalysis.jsx";
import Profile from "./pages/Profile.jsx";
import ImageDescription from "./pages/ImageDescription.jsx";
import HomePage from "./pages/HomePage.jsx";


function App() {

  return (
   <Routes>
       <Route path='/' element={<Layout/>}>
           <Route index element={<HomePage/>} />
           <Route path='sentiment' element={<SentimentAnalysis/>} />
           <Route path='emotion' element={<EmotionAnalysis/>} />
           <Route path='meaning' element={<MeaningAnalysis/>} />
           <Route path='image-description' element={<ImageDescription/>} />
           <Route path='analysis' element={<FullAnalysis/>} />
           <Route path='profile' element={<Profile/>} />



       </Route>


   </Routes>
  )
}

export default App
