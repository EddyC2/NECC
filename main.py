from utils import call_necc_api, summarize_match, summarize_team

def main():
    print("\n=== Upcoming Matches ===")
    upcoming = call_necc_api("GetSchoolFutureMatches")
    if upcoming:
        for match in upcoming:
            print(summarize_match(match))
    else:
        print("No upcoming matches ❌")

    print("\n=== School Matches ===")
    all_matches = call_necc_api("SchoolsAllMatches")
    if all_matches:
        for match in all_matches:
            print(summarize_match(match))
    else:
        print("No matches found ❌")

    print("\n=== Teams ===")
    teams = call_necc_api("SchoolTeams")
    if teams:
        for team in teams:
            print(summarize_team(team))
    else:
        print("No teams found ❌")



if __name__ == "__main__":
    main()
