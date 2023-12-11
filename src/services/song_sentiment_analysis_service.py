from src.config import get_settings
from transformers import pipeline
from src.schemas.song_structure import SongStructure
from src.schemas.sentiment_score_output import SentimentScoreOutput
from src.schemas.song_section_sentiment import SongSectionSentiment
SETTINGS = get_settings()
class SongSentimentAnalysisService:
    def __init__(self) -> None:
        self.pipe = pipeline("text-classification", model=SETTINGS.models_versions[0], top_k = None)
    def get_overall_sentiment(self, song_structure_scores: list[SongSectionSentiment]) -> SongSectionSentiment:
        overall_sentiment = SongSectionSentiment(section="Overall", scores=[])
        overall_positive_score = 0
        overall_negative_score = 0
        chorus_weight = 5
        total_sections = 0

        for score in song_structure_scores:
            for sentiment_score in score.scores:
                if sentiment_score.label == "POSITIVE":
                    if score.section == "Chorus":
                        overall_positive_score += chorus_weight * sentiment_score.score
                    else:
                        overall_positive_score += sentiment_score.score
                else:
                    if score.section == "Chorus":
                        overall_negative_score += chorus_weight * sentiment_score.score
                    else:
                        overall_negative_score += sentiment_score.score

                total_sections += 1

        if total_sections > 0:
            overall_positive_score /= total_sections
            overall_negative_score /= total_sections

        overall_sentiment.scores.append(SentimentScoreOutput(label="POSITIVE", score=overall_positive_score))
        overall_sentiment.scores.append(SentimentScoreOutput(label="NEGATIVE", score=overall_negative_score))

        normalization_factor = 1 / (overall_positive_score + overall_negative_score)
        overall_sentiment.scores[0].score *= normalization_factor
        overall_sentiment.scores[1].score *= normalization_factor

        return overall_sentiment


            

        
    def predict(self, song_structure:SongStructure) -> SongSectionSentiment:
        results:list[SongSectionSentiment] = []
        for section in song_structure.sections:
            print(section.lyrics)
            result = self.pipe(section.lyrics)
            list_of_scores:list[SentimentScoreOutput] = [(SentimentScoreOutput(label = score['label'], score = score['score'])) for score in result[0]]
            song_section_sentiment = SongSectionSentiment(section = section.section, scores = list_of_scores)
            results.append(song_section_sentiment)        
        overall_sentiment = self.get_overall_sentiment(results)
        return overall_sentiment   
              
        