from sqlmodel import SQLModel, create_engine, Session, Field, Column,JSON

class SongAnalysisProfile(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    song_title:str
    artist_name:str
    sentiment: dict =  Field(default={}, sa_column=Column(JSON))
    emotion: dict =  Field(default={}, sa_column=Column(JSON))
    meaning: dict =  Field(default={}, sa_column=Column(JSON))
    image_description: str

sqlite_file = "db.sqlite3"
sqlite_url = f"sqlite:///{sqlite_file}"




connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
