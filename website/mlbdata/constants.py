import json, requests, pytz

UTC = pytz.utc
EST = pytz.timezone("US/Eastern")
FMTUTC = "%Y-%m-%dT%H:%M:%SZ"
FMTEST = "%m/%d %I:%M %p"

URL = requests.get('https://statsapi.mlb.com/api/v1/schedule/games/?sportId=1')
TEXT = URL.text
SCHEDULE = json.loads(TEXT)

TOTALGAMES = SCHEDULE["totalGames"]
GAMESINPROGRESS = SCHEDULE["totalGamesInProgress"]