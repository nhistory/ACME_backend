from fastapi import FastAPI, Security, HTTPException, Depends, status
from fastapi.security import APIKeyHeader
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import nullslast
from .models import Team, LeagueEnum
from .database import get_db
from .schemas import TeamResponse
import os
from dotenv import load_dotenv

# Load environment variables from .env file (if it exists)
load_dotenv()

app = FastAPI()

api_key_header = APIKeyHeader(name="X-API-KEY", auto_error=False)
API_KEY = os.environ.get("API_KEY")

if API_KEY is None:
    raise ValueError("API_KEY environment variable not set!")

async def get_api_key(api_key_header: str = Security(api_key_header)):
    if api_key_header != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key",
        )
    return api_key_header

# Configure CORS
origins = [
    "http://localhost:3000",
    "http://localhost:3001",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # List of allowed origins
    allow_credentials=True, #  Important if you're using cookies or authentication
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],  # Allowed HTTP methods
    allow_headers=["*"],  #  Or specify specific headers: ["X-API-KEY", "Content-Type"]
)

@app.get(
    "/team_list/{league}",
    response_model=list[TeamResponse],
    responses={
        400: {"description": "Invalid request"},
        401: {"description": "Unauthenticated"},
        403: {"description": "Unauthorized"},
        404: {"description": "Teams not found"},
        500: {"description": "Internal Server Error"},
    },
)
def read_teams(
    league: LeagueEnum,
    sort_by: str = "Name",
    db: Session = Depends(get_db),
    api_key: str = Security(get_api_key),
):
    """
    Get a list of teams based on the provided league.
    """
    print(f"Request for league {league} received with API key: {api_key}")
    
    valid_sort_fields = ["Name", "Conference", "Division"]
    if sort_by not in valid_sort_fields:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid sort_by parameter.  Must be one of: {', '.join(valid_sort_fields)}",
        )

    try:
        # Query the database, filtering by the league enum.
        query = db.query(Team).filter(Team.league == league)

        if sort_by == "Conference":
            query = query.order_by(nullslast(Team.conference))
        elif sort_by == "Division":
            query = query.order_by(nullslast(Team.division))
        else:
            query = query.order_by(Team.name)

        teams = query.all()

        # Check if any teams were found.
        if not teams:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"No teams found for league: {league}",
            )

        return teams

    except HTTPException as e:
      raise e

    except Exception as e:
        # Log the exception for debugging purposes.
        print(f"An unexpected error occurred: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred. Please try again later.",
        )