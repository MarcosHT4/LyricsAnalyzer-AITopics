import {Route, Routes} from 'react-router-dom';
import Layout from "./components/Layout.jsx";
import SentimentAnalysis from "./pages/SentimentAnalysis.jsx";
import EmotionAnalysis from "./pages/EmotionAnalysis.jsx";
import MeaningAnalysis from "./pages/MeaningAnalysis.jsx";
import FullAnalysis from "./pages/FullAnalysis.jsx";
import Profile from "./pages/Profile.jsx";


function App() {

  return (
   <Routes>
       <Route path='/' element={<Layout/>}>
           <Route path='sentiment' element={<SentimentAnalysis/>} />
           <Route path='emotion' element={<EmotionAnalysis/>} />
           <Route path='meaning' element={<MeaningAnalysis/>} />
           <Route path='analysis' element={<FullAnalysis/>} />
           <Route path='profile' element={<Profile/>} />



       </Route>


   </Routes>
  )
}

export default App
