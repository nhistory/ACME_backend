from pydantic import BaseModel, UUID4
from typing import Optional
from .models import LeagueEnum

# Base class for Team schemas
class TeamBase(BaseModel):
    name: str
    nickname: str
    display_name: str
    conference: Optional[str] = None
    division: Optional[str] = None

# Schema for creating a Team (includes league)
class TeamCreate(TeamBase):
    league: LeagueEnum

# Schema for reading a Team (includes id and league)
class Team(TeamBase):
    id: UUID4
    league: LeagueEnum

    class Config:
        orm_mode = True