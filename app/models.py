from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, Integer, ForeignKey, DateTime, Boolean

from app.database import Base

from datetime import datetime, date, timezone, time



class User(Base):
    __tablename__ = "users"

    id : Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str] = mapped_column(String(128))
    username: Mapped[str] = mapped_column(String(32), unique=True)
    first_name:Mapped[str] = mapped_column(String(32))
    last_name: Mapped[str] = mapped_column(String(32))
    birthdate: Mapped[date] = mapped_column(date)
    joined_at: Mapped[datetime] = mapped_column(datetime, default=datetime.now(timezone.utc))
    is_active:  Mapped[bool] = mapped_column(default=True)
    is_staff:  Mapped[bool] = mapped_column(default=False)
    is_superuser: Mapped[bool] = mapped_column(default=False)



class Topic(Base):
    __tablename__ = "topics"

    id : Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True) 


  
class Game(Base):
    __tablename__="games"

    id : Mapped[int] = mapped_column(primary_key=True)
    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    title: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(1000))
    topic_id: Mapped[int] = mapped_column(Integer, ForeignKey("topics.id"))
    score: Mapped[int] = mapped_column(Integer, default=0)
    start_time:  Mapped[datetime] = mapped_column(DateTime, nullable=False)
    end_time:   Mapped[datetime] = mapped_column(DateTime, nullable=False)

    owner: Mapped = relationship("User", back_populates="Owned_games")
    question:Mapped[list["GameQuestion"]] = relationship("GameQuesstion", back_populates="game")


class GameQuestion(Base):
      __tablename__="gamequestion"

      game_id: Mapped[int] = mapped_column(Integer, ForeignKey("games.id"))
      question_id: Mapped[int] = mapped_column(Integer, ForeignKey("question.id"))

      question: Mapped["Question"] = relationship(back_populates="games")
      game: Mapped["Game"] = relationship( back_populates="questions")


"""
game = Game()
game.owner.region.country.name

user = User()
user.Owned_games

db.query(User).filter(User.id == game.owner_id).first().user
"""


class Participation(Base):
     __tablename__= "participation"


     id: Mapped[int] = mapped_column(primary_key=True)
     user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
     game_id: Mapped[int] = mapped_column(Integer, ForeignKey("games.id"))
     start_time: Mapped[datetime] = mapped_column(DateTime, nullable=True)
     end_time: Mapped[datetime] = mapped_column(DateTime, nullable=True)
     gained_score: Mapped[int] = mapped_column(default=0)
     registered_at:  Mapped[datetime] = mapped_column(datetime, default=datetime.now(timezone.utc))


class Question(Base):
     __tablename__= "question"

     id: Mapped[int] = mapped_column(primary_key=True)
     owner_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
     title: Mapped[str] = mapped_column(String(100))
     description: Mapped[str] = mapped_column(String(1000, nullable=True))
     topic_id: Mapped[int] = mapped_column(Integer, ForeignKey("topics.id"))

     options_id: Mapped[list['Option']] = relationship(back_populates="question")


class Option(Base):
      __tablename__="option"

      id: Mapped[int] = mapped_column(primary_key=True)
      question:  Mapped[int] = mapped_column(Integer, ForeignKey("question.id"))
      title: Mapped[str] = mapped_column(String)
      is_correct: Mapped[bool] = mapped_column(Boolean, default=False)
      created_at: Mapped[datetime] = mapped_column(datetime, default=datetime.now(timezone.utc))
    
      question = relationship("Question", back_populates="option_ids")

o1 = Question()
o1.question.title


class Submission(Base):
     __tablename__="submission"

     user_id: Mapped[int] = mapped_column(primary_key=True)
     question_id: Mapped[int] = mapped_column()
     Option_id: Mapped[str] = mapped_column()
     created_at: Mapped[time] = mapped_column(time)
     is_correct: Mapped[bool] = mapped_column(bool)


