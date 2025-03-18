from __future__ import annotations

import enum
import os
from sqlalchemy import create_engine, String, Enum
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from typing import Optional
from uuid import uuid4, UUID
from sqlalchemy.dialects.postgresql import UUID as PostgresUUID
from dotenv import load_dotenv

load_dotenv()

# Database URL
DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL is None:
    raise ValueError("DATABASE_URL environment variable not set.")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass

class LeagueEnum(str, enum.Enum):
    NCAAB = "NCAAB"
    NCAAF = "NCAAF"
    NFL = "NFL"
    UFL = "UFL"
    USFL = "USFL"

class Team(Base):
    __tablename__ = "teams"

    id: Mapped[UUID] = mapped_column(PostgresUUID(as_uuid=True), primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(String, nullable=False)
    nickname: Mapped[str] = mapped_column(String, nullable=False)
    display_name: Mapped[str] = mapped_column(String, nullable=False)
    league: Mapped[LeagueEnum] = mapped_column(Enum(LeagueEnum), nullable=False)
    conference: Mapped[Optional[str]] = mapped_column(String)
    division: Mapped[Optional[str]] = mapped_column(String)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()