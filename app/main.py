from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .models import get_db, Team, LeagueEnum
from .schemas import Team as SchemaTeam

app = FastAPI()

@app.get("/team_list/{league}", response_model=list[SchemaTeam])
def read_teams(league: LeagueEnum, sort_by: str = "Name", db: Session = Depends(get_db)):
    """
    Get a list of teams based on the provided league.

    Args:
        league: The league to filter by (using the LeagueEnum).
        sort_by: The attribute to sort by ('Name', 'Conference', or 'Division').
        db: The database session (dependency injection).

    Returns:
        A list of Team objects.
    """

    # Query the database, filtering by the league enum.
    query = db.query(Team).filter(Team.league == league)

    # Apply sorting.
    if sort_by == "Conference":
        query = query.order_by(Team.conference)
    elif sort_by == "Division":
        query = query.order_by(Team.division)
    else:  # Default to sorting by name
        query = query.order_by(Team.name)

    teams = query.all()
    return teams