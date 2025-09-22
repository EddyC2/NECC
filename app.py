
import streamlit as st
from utils import call_necc_api, format_timestamp

#from background import set_png_as_page_bg

# Show banner
st.image("esu.png", use_container_width=True)
#cetner the title page
st.markdown(
    """
    <style>
    .title-box {
        background-color: #000000;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 25px;
        box-shadow: 0px 2px 6px rgba(0,0,0,0.1);
        text-align: center;
    }
    .title-box h1 {
        margin: 0;
        font-size: 3.2em;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Page Title ---
st.markdown(
    """
    <div class="title-box">
        <h1>NECC Event Dashboard</h1>
        <p>Live data pulled from the NECC API</p>
    </div>
    """,
    unsafe_allow_html=True
)


st.markdown(
    """
    <style>
    .section-box { 
        background-color: #000000;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0px 2px 6px rgba(0,0,0,0.1);
        text-align: center;

    }
    .section-box h2 {
        margin-top: 0;
        margin-bottom: 15px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# --- Matches Section ---
matches = call_necc_api("SchoolsAllMatches")

matches_html = """
<div class="section-box">
    <h2>🏆 All Matches 🏆</h2>
"""
if matches and isinstance(matches, list):
    for match in matches:
        matches_html += f"""
        <h4>{match.get('homeTeam', 'Unknown')} vs {match.get('awayTeam', 'Unknown')}</h4>
        <p><b>Date:</b> {format_timestamp(match.get('timestamp', 0))}</p>
        <p><b>Result:</b> {match.get('result', 'Not available')}</p>
        <hr>
        """
else:
    matches_html += "<p>⚠️ No matches available yet</p>"
matches_html += "</div>"
st.markdown(matches_html, unsafe_allow_html=True)


# --- Teams Section ---
teams = call_necc_api("SchoolTeams")

teams_html = """
<div class="section-box">
    <h2>👥 Teams 👥</h2>
"""
if teams and isinstance(teams, list):
    for team in teams:
        players = ', '.join(team.get('players', [])) if team.get('players') else 'No players listed'
        teams_html += f"""
        <h4>{team.get('name', 'Unknown')}</h4>
        <p><b>Coach:</b> {team.get('coach', 'Not listed')}</p>
        <p><b>Players:</b> {players}</p>
        <hr>
        """
else:
    teams_html += "<p>⚠️ No teams available yet</p>"
teams_html += "</div>"
st.markdown(teams_html, unsafe_allow_html=True)


# --- Upcoming Matches Section ---
upcoming = call_necc_api("UpcomingMatches")

upcoming_html = """
<div class="section-box">
    <h2>📅 Upcoming Matches 📅</h2>
"""
if upcoming and isinstance(upcoming, list):
    for match in upcoming:
        upcoming_html += f"""
        <h4>{match.get('homeTeam', 'Unknown')} vs {match.get('awayTeam', 'Unknown')}</h4>
        <p><b>Scheduled:</b> {format_timestamp(match.get('timestamp', 0))}</p>
        <hr>
        """
else:
    upcoming_html += "<p>⚠️ No upcoming matches available yet</p>"
upcoming_html += "</div>"
st.markdown(upcoming_html, unsafe_allow_html=True)