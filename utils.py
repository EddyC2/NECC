import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

API_BASE = "https://us-central1-neccwebsite.cloudfunctions.net"

HEADERS = {
    "X-NECC-TOKEN": "API_KEY",
    "X-NECC-SECRET": "API_SECRET"
}

def call_necc_api(endpoint: str):
    """Generic NECC API caller. Returns parsed JSON or None."""
    url = f"{API_BASE}/{endpoint}"
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        data = response.json()
        if "data" in data and data["data"]:
            return data["data"]
        else:
            return None
    except requests.exceptions.HTTPError as e:
        if response.status_code in [403]:
            print(f"{endpoint}: Authentication error - check your API keys 🔑")
        elif response.status_code in [404, 500]:
            print(f"{endpoint}: No data available yet or endpoint issue ({response.status_code})")
        else:
            print(f"{endpoint}: API error {response.status_code}")
            print(response.text)
        return None
    except requests.exceptions.RequestException as e:
        print(f"{endpoint}: Network error or invalid request")
        print(e)
        return None

def format_timestamp(ts):
    """Convert Unix timestamp to readable date/time."""
    return datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M")

def summarize_match(match):
    """Create a short readable summary for a match."""
    team_one = match.get("team_one_name", "Team One")
    team_two = match.get("team_two_name", "Team Two")
    score = f"{match.get('team_one_score', 0)} - {match.get('team_two_score', 0)}"
    activity = match.get("activity", "Game")
    date = format_timestamp(match.get("date", 0))
    return f"{date}: {activity} | {team_one} vs {team_two} | Score: {score}"

def summarize_team(team):
    """Create a short summary for a team."""
    name = team.get("name", "Unknown Team")
    activity = team.get("activity_name", "Game")
    roster = team.get("roster", [])
    player_list = ", ".join([p.get("gamer_tag", "N/A") for p in roster])
    return f"{name} ({activity}) | Players: {player_list}"
