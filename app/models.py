from __future__ import annotations

import enum
from sqlalchemy import String, Enum
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional
from uuid import uuid4, UUID
from sqlalchemy.dialects.postgresql import UUID as PostgresUUID
from .database import Base


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
