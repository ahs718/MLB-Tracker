import datetime
from mlbdata.game import Game
from mlbdata.team import Team
import mlbdata.constants as c


# Parses UTC time from string
def setUTC(gameDate, fmt, timezone):
    return datetime.datetime.strptime(gameDate, fmt).replace(tzinfo=timezone)

# Converts UTC time to EST (12-hr format)
def convertUTCReadable(utcTime, fmt, timezone):
    return utcTime.astimezone(timezone).strftime(fmt)

# Gets game data from MLB API and stores it in a list
def fetchData():
    games = []
    for i in c.SCHEDULE["dates"][0]["games"]:
        timeUTC = setUTC(i["gameDate"], c.FMTUTC, c.UTC)
        timeEST = convertUTCReadable(timeUTC, c.FMTEST, c.EST)
        venue = i["venue"]["name"]
        
        # Create the home team object 
        status = "Home"
        name = i["teams"]["home"]["team"]["name"]
        
        if "score" in i["teams"]["home"]:
            score = i["teams"]["home"]["score"]
        else:
            score = "N/A"
            
        wins = i["teams"]["home"]["leagueRecord"]["wins"]
        losses = i["teams"]["home"]["leagueRecord"]["losses"]
        pct = i["teams"]["home"]["leagueRecord"]["pct"]
        home = Team(status, name, score, wins, losses, pct)
        
        # Create the away team object
        status = "Away"
        name = i["teams"]["away"]["team"]["name"]
        
        if "score" in i["teams"]["away"]:
            score = i["teams"]["away"]["score"]
        else:
            score = "N/A"
            
        wins = i["teams"]["away"]["leagueRecord"]["wins"]
        losses = i["teams"]["away"]["leagueRecord"]["losses"]
        pct = i["teams"]["away"]["leagueRecord"]["pct"]
        away = Team(status, name, score, wins, losses, pct)
        
        # Store home and away teams into game object
        game = Game(timeEST, venue, home, away)
        
        # Add game object to games list
        games.append(game)
    
    # Return list of games
    return games