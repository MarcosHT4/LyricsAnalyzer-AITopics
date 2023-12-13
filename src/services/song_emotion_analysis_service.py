from src.config import get_settings
from transformers import pipeline
from src.schemas.song_structure import SongStructure
from src.schemas.song_section_output import SongSectionOutput
from src.schemas.score_output import ScoreOutput
from collections import defaultdict
SETTINGS = get_settings()
class SongEmotionAnalysisService:
    def __init__(self):
        self.pipe = pipeline("text-classification", model=SETTINGS.models_versions[1], top_k = None)

    def get_overall_emotion(self, song_structure_emotion_scores: list[SongSectionOutput]) -> SongSectionOutput:
        emotion_scores = defaultdict(float)
        for section in song_structure_emotion_scores:
            for score in section.scores:
                emotion_scores[score.label] += score.score
        top_3_emotions = sorted(emotion_scores.items(), key=lambda x: x[1], reverse=True)[:3]   
        total_top3_score = sum(score for emotion, score in top_3_emotions)
        normalized_top3_emotions = [(emotion, score / total_top3_score) for emotion, score in top_3_emotions] 
        return SongSectionOutput(section = 'overall', scores = [ScoreOutput(label = emotion, score = score) for emotion, score in normalized_top3_emotions])



    def predict(self, song_structure:SongStructure) -> SongSectionOutput:
        results:list[SongSectionOutput] = []
        for section in song_structure.sections:
            result = self.pipe(section.lyrics)
            list_of_scores:list[ScoreOutput] = [(ScoreOutput(label = score['label'], score = score['score'])) for score in result[0][:4] if score['label'] != 'neutral']
            song_section_sentiment = SongSectionOutput(section = section.section, scores = list_of_scores)
            results.append(song_section_sentiment)      
        overall_result = self.get_overall_emotion(results)    
        return overall_result    

     