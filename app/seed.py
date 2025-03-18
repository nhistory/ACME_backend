from sqlalchemy.orm import Session
from sqlalchemy import inspect, exc
from .models import Team, LeagueEnum, engine, Base, SessionLocal
from uuid import uuid4

def create_dummy_teams(db: Session):
    """Creates dummy team data in the database."""

    # Check if the table exists, and skip creation if it does (optional)
    inspector = inspect(engine)
    if not inspector.has_table("teams"):
        Base.metadata.create_all(bind=engine)
    else:
        print("Teams table already exists. Skipping table creation.")


    teams_data = [
        # NCAAB
        {"name": "Duke Blue Devils", "nickname": "Duk", "display_name": "Duke", "league": LeagueEnum.NCAAB, "conference": "ACC", "division": None},
        {"name": "North Carolina Tar Heels", "nickname": "UNC", "display_name": "North Carolina", "league": LeagueEnum.NCAAB, "conference": "ACC", "division": None},
        {"name": "Kentucky Wildcats", "nickname": "UK", "display_name": "Kentucky", "league": LeagueEnum.NCAAB, "conference": "SEC", "division": None},
        {"name": "Kansas Jayhawks", "nickname": "KU", "display_name": "Kansas", "league": LeagueEnum.NCAAB, "conference": "Big 12", "division": None},
        {"name": "UCLA Bruins", "nickname": "UCLA", "display_name": "UCLA", "league": LeagueEnum.NCAAB, "conference": "Pac-12", "division": None},
        {"name": "Gonzaga Bulldogs", "nickname": "Zags", "display_name": "Gonzaga", "league": LeagueEnum.NCAAB, "conference": "WCC", "division": None},
        {"name": "Arizona Wildcats", "nickname": "UA", "display_name": "Arizona", "league": LeagueEnum.NCAAB,"conference": "Pac-12", "division": None},
        {"name": "Baylor Bears", "nickname": "BU", "display_name": "Baylor", "league": LeagueEnum.NCAAB, "conference": "Big 12", "division": None},
        {"name": "Purdue Boilermakers", "nickname": "PU", "display_name": "Purdue", "league": LeagueEnum.NCAAB, "conference": "Big Ten", "division": None},
        {"name": "Houston Cougars", "nickname": "UH", "display_name": "Houston", "league": LeagueEnum.NCAAB, "conference": "Big 12", "division": None},

        # NCAAF
        {"name": "Alabama Crimson Tide", "nickname": "Bama", "display_name": "Alabama", "league": LeagueEnum.NCAAF, "conference": "SEC", "division": "West"},
        {"name": "Georgia Bulldogs", "nickname": "UGA", "display_name": "Georgia", "league": LeagueEnum.NCAAF, "conference": "SEC", "division": "East"},
        {"name": "Ohio State Buckeyes", "nickname": "OSU", "display_name": "Ohio State", "league": LeagueEnum.NCAAF, "conference": "Big Ten", "division": "East"},
        {"name": "Michigan Wolverines", "nickname": "UM", "display_name": "Michigan", "league": LeagueEnum.NCAAF, "conference": "Big Ten", "division": "East"},
        {"name": "Texas Longhorns", "nickname": "UT", "display_name": "Texas", "league": LeagueEnum.NCAAF, "conference": "Big 12", "division": None},
        {"name": "USC Trojans", "nickname": "USC", "display_name": "USC", "league": LeagueEnum.NCAAF, "conference": "Pac-12", "division": None},
        {"name": "Clemson Tigers", "nickname": "Clem", "display_name": "Clemson", "league": LeagueEnum.NCAAF, "conference": "ACC", "division": "Atlantic"},
        {"name": "Florida State Seminoles", "nickname": "FSU", "display_name": "Florida State", "league": LeagueEnum.NCAAF, "conference": "ACC", "division": "Atlantic"},
        {"name": "LSU Tigers", "nickname": "LSU", "display_name": "LSU", "league": LeagueEnum.NCAAF, "conference": "SEC", "division": "West"},
        {"name": "Oregon Ducks", "nickname": "UO", "display_name": "Oregon", "league": LeagueEnum.NCAAF, "conference": "Pac-12", "division": None},

        # NFL
        {"name": "Kansas City Chiefs", "nickname": "KC", "display_name": "Kansas City", "league": LeagueEnum.NFL, "conference": "AFC", "division": "West"},
        {"name": "Buffalo Bills", "nickname": "BUF", "display_name": "Buffalo", "league": LeagueEnum.NFL, "conference": "AFC", "division": "East"},
        {"name": "Cincinnati Bengals", "nickname": "CIN", "display_name": "Cincinnati", "league": LeagueEnum.NFL, "conference": "AFC", "division": "North"},
        {"name": "Jacksonville Jaguars", "nickname": "JAX", "display_name": "Jacksonville", "league": LeagueEnum.NFL, "conference": "AFC", "division": "South"},
        {"name": "Los Angeles Chargers", "nickname": "LAC", "display_name": "Los Angeles", "league": LeagueEnum.NFL, "conference": "AFC", "division": "West"},
        {"name": "Miami Dolphins", "nickname": "MIA", "display_name": "Miami", "league": LeagueEnum.NFL, "conference": "AFC", "division": "East"},
        {"name": "Baltimore Ravens", "nickname": "BAL", "display_name": "Baltimore", "league": LeagueEnum.NFL, "conference": "AFC", "division": "North"},
        {"name": "Tennessee Titans", "nickname": "TEN", "display_name": "Tennessee", "league": LeagueEnum.NFL, "conference": "AFC", "division": "South"},
        {"name": "New England Patriots", "nickname": "NE", "display_name": "New England", "league": LeagueEnum.NFL, "conference": "AFC", "division": "East"},
        {"name": "Pittsburgh Steelers", "nickname": "PIT", "display_name": "Pittsburgh", "league": LeagueEnum.NFL, "conference": "AFC", "division": "North"},
        {"name": "Las Vegas Raiders", "nickname": "LV", "display_name": "Las Vegas", "league": LeagueEnum.NFL, "conference": "AFC", "division": "West"},
        {"name": "Indianapolis Colts", "nickname": "IND", "display_name": "Indianapolis", "league": LeagueEnum.NFL, "conference": "AFC", "division": "South"},
        {"name": "Denver Broncos", "nickname": "DEN", "display_name": "Denver", "league": LeagueEnum.NFL, "conference": "AFC", "division": "West"},
        {"name": "Cleveland Browns", "nickname": "CLE", "display_name": "Cleveland", "league": LeagueEnum.NFL, "conference": "AFC", "division": "North"},
        {"name": "New York Jets", "nickname": "NYJ", "display_name": "New York", "league": LeagueEnum.NFL, "conference": "AFC", "division": "East"},
        {"name": "Houston Texans", "nickname": "HOU", "display_name": "Houston", "league": LeagueEnum.NFL, "conference": "AFC", "division": "South"},
        {"name": "Philadelphia Eagles", "nickname": "PHI", "display_name": "Philadelphia", "league": LeagueEnum.NFL, "conference": "NFC", "division": "East"},
        {"name": "Dallas Cowboys", "nickname": "DAL", "display_name": "Dallas", "league": LeagueEnum.NFL, "conference": "NFC", "division": "East"},
        {"name": "San Francisco 49ers", "nickname": "SF", "display_name": "San Francisco", "league": LeagueEnum.NFL, "conference": "NFC", "division": "West"},
        {"name": "Minnesota Vikings", "nickname": "MIN", "display_name": "Minnesota", "league": LeagueEnum.NFL, "conference": "NFC", "division": "North"},
		{"name": "Detroit Lions", "nickname": "DET", "display_name": "Detroit", "league": LeagueEnum.NFL, "conference": "NFC", "division": "North"},
		{"name": "Green Bay Packers", "nickname": "GB", "display_name": "Green Bay", "league": LeagueEnum.NFL, "conference": "NFC", "division": "North"},
		{"name": "Chicago Bears", "nickname": "CHI", "display_name": "Chicago", "league": LeagueEnum.NFL, "conference": "NFC", "division": "North"},
		{"name": "Seattle Seahawks", "nickname": "SEA", "display_name": "Seattle", "league": LeagueEnum.NFL, "conference": "NFC", "division": "West"},
		{"name": "Los Angeles Rams", "nickname": "LAR", "display_name": "Los Angeles", "league": LeagueEnum.NFL, "conference": "NFC", "division": "West"},
		{"name": "Arizona Cardinals", "nickname": "ARI", "display_name": "Arizona", "league": LeagueEnum.NFL, "conference": "NFC", "division": "West"},
		{"name": "New Orleans Saints", "nickname": "NO", "display_name": "New Orleans", "league": LeagueEnum.NFL, "conference": "NFC", "division": "South"},
		{"name": "Tampa Bay Buccaneers", "nickname": "TB", "display_name": "Tampa Bay", "league": LeagueEnum.NFL, "conference": "NFC", "division": "South"},
		{"name": "Atlanta Falcons", "nickname": "ATL", "display_name": "Atlanta", "league": LeagueEnum.NFL, "conference": "NFC", "division": "South"},
		{"name": "Carolina Panthers", "nickname": "CAR", "display_name": "Carolina", "league": LeagueEnum.NFL, "conference": "NFC", "division": "South"},
		{"name": "New York Giants", "nickname": "NYG", "display_name": "New York", "league": LeagueEnum.NFL, "conference": "NFC", "division": "East"},
		{"name": "Washington Commanders", "nickname": "WAS", "display_name": "Washington", "league": LeagueEnum.NFL, "conference": "NFC", "division": "East"},

        # UFL
        {"name": "Birmingham Stallions", "nickname": "BHM", "display_name": "Birmingham", "league": LeagueEnum.UFL, "conference": "USFL", "division": None},
        {"name": "Michigan Panthers", "nickname": "MICH", "display_name": "Michigan", "league": LeagueEnum.UFL, "conference": "USFL", "division": None},
        {"name": "Houston Roughnecks", "nickname": "HOU", "display_name": "Houston", "league": LeagueEnum.UFL, "conference": "USFL", "division": None},
        {"name": "Memphis Showboats", "nickname": "MEM", "display_name": "Memphis", "league": LeagueEnum.UFL, "conference": "USFL", "division": None},
        {"name": "St. Louis Battlehawks", "nickname": "STL", "display_name": "St. Louis", "league": LeagueEnum.UFL, "conference": "XFL", "division": None},
        {"name": "Arlington Renegades", "nickname": "ARL", "display_name": "Arlington", "league": LeagueEnum.UFL, "conference": "XFL", "division": None},
        {"name": "San Antonio Brahmas", "nickname": "SA", "display_name": "San Antonio", "league": LeagueEnum.UFL, "conference": "XFL", "division": None},
        {"name": "DC Defenders", "nickname": "DC", "display_name": "DC", "league": LeagueEnum.UFL, "conference": "XFL", "division": None},

        # USFL (included as an example, as there might be previous data)
        {"name": "New Jersey Generals", "nickname": "NJ", "display_name": "New Jersey", "league": LeagueEnum.USFL, "conference": None, "division": None},
        {"name": "Philadelphia Stars", "nickname": "PHI", "display_name": "Philadelphia", "league": LeagueEnum.USFL, "conference": None, "division": None},
    ]


    try:
        for team_data in teams_data:
            team_id = team_data.get("id", uuid4())
            db_team = Team(
                id=team_id,
                name=team_data["name"],
                nickname=team_data["nickname"],
                display_name=team_data["display_name"],
                league=team_data["league"],
                conference=team_data.get("conference"),
                division=team_data.get("division"),
            )
            db.add(db_team)
            print(f"Added team: {team_data['name']}")
        db.commit()  # Commit only if everything was successful
    except exc.SQLAlchemyError as e:  # Catch SQLAlchemy specific exceptions
        print(f"An error occurred: {e}")
        db.rollback()  # Rollback changes if an error occurred
        raise  # Re-raise the exception to see the traceback
    finally:
        db.close()


if __name__ == "__main__":
    #  No need to create a session here, since create_dummy_teams handles it.
    #  Instead, call create_dummy_teams directly, passing a new session.

    db = SessionLocal()  # Create session here.
    create_dummy_teams(db)  # Now we are *always* creating/closing a session.
    print("Dummy teams creation attempted.") # More general message