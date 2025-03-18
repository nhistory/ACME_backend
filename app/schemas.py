from pydantic import BaseModel, UUID4
from typing import Optional

# Base class for Team schemas
class TeamBase(BaseModel):
    name: str
    nickname: str
    display_name: str


# Schema for creating a Team (includes league)
class TeamCreate(TeamBase):
    league: "LeagueEnum"

    class Config:
        from_attributes = True


# Schema for reading a Team (includes id and league)
class TeamRead(TeamBase):
    id: UUID4
    league: "LeagueEnum"

    class Config:
        from_attributes = True

# Schema for the API response (list of teams)
class TeamResponse(BaseModel):
    id: UUID4
    name: str
    nickname: str
    display_name: str

    class Config:
        from_attributes = True

from .models import LeagueEnum