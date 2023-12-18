from sqlmodel import Session, select
from src.db import SongAnalysisProfile
from src.schemas.song_full_analysis_output import SongFullAnalysisOutput
from src.schemas.profile import Profile
class ProfileGenerationService:
    def generate_profile(self,db_session:Session, song_sentiment_analysis, song_emotion_analysis) -> Profile:
        song_profiles = db_session.exec(select(SongAnalysisProfile)).all()
        for song_profile in song_profiles:
            del song_profile.id
        for song_profile in song_profiles:
            if(not song_profile.sentiment):
                del song_profile.sentiment
            if (not song_profile.emotion ):
                del song_profile.emotion
            if (not song_profile.meaning):
                del song_profile.meaning
            if (song_profile.image_description is None):
                del song_profile.image_description            
            song_profile = song_profile.__dict__
            song_profile['name'] = song_profile['song_title']
            del song_profile['song_title']
            song_profile['artist'] = song_profile['artist_name']


        song_profiles = [SongFullAnalysisOutput(**song_profile.__dict__) for song_profile in song_profiles]  


        song_sentiments = [song.sentiment for song in song_profiles if song.sentiment ]
        song_emotions = [song.emotion for song in song_profiles if song.emotion]
        songs = [f"{song.name}-{song.artist}" for song in song_profiles]

        sentiment_profile = song_sentiment_analysis.get_overall_sentiment(song_sentiments)
        emotion_profile = song_emotion_analysis.get_overall_emotion(song_emotions)

        profile = Profile(songs=songs, sentiment=sentiment_profile, emotion=emotion_profile)
        return profile
