import random

class Team:
    def __init__(self, name):
        self.name = name
        self.rivalry_matchup_home = False
        self.rivalry_matchup = None
        self.matchups = []

    def get_name(self):
        return self.name

    def get_rivalry_matchup(self):
        return self.rivalry_matchup

    def is_rivalry_matchup_home(self):
        return self.rivalry_matchup_home

    def set_rivalry_matchup_home(self):
        self.rivalry_matchup_home = True

    def set_rivalry_matchup(self, opponent):
        self.rivalry_matchup = opponent

    def get_matchups(self):
        return self.matchups

    def add_matchup(self, opponent):
        self.matchups.append(opponent)

    def has_matchup(self, opponent):
        for old_opponent in self.matchups:
            if opponent == old_opponent:
                return True
        return False

def get_team_by_name(team_name, team_list):
    for team in team_list:
        if team.get_name().lower() == team_name.lower():
            return team
    return None

def __main__():
    teams = []

    num_teams = int(input("Enter number of teams: "))
    rivalry_week_num = int(input("Enter number of week for rivalry week: "))
    num_weeks = num_teams - 1

    for i in range(num_teams):
        user_team = input(f"Enter team {i+1}: ")
        new_team = Team(user_team)
        teams.append(new_team)

    for i in range(num_teams):
        home_team = teams[i]
        user_answer = input(f"Will {home_team.get_name()} be a home team? (y/n): ")

        if not user_answer == "y":
            away_team_name = input(f"Enter rivalry matchup of {home_team.get_name()} : ")
            away_team = get_team_by_name(away_team_name, teams)
            home_team.set_rivalry_matchup(away_team)
            home_team.add_matchup(away_team)
            home_team.set_rivalry_matchup_home()
            away_team.set_rivalry_matchup(home_team)
            away_team.add_matchup(home_team)

    for i in range(num_weeks):
        if i + 1 != rivalry_week_num:
            available_teams = teams[:]

            print(f"WEEK {i + 1}:")
            for j in range(int(num_teams / 2)):
                random_away_team = random.choice(available_teams)
                available_teams.remove(random_away_team)

                while True:
                    random_home_team = random.choice(available_teams)

                    if not random_away_team.has_matchup(random_home_team):
                        available_teams.remove(random_home_team)
                        random_away_team.add_matchup(random_home_team)
                        random_home_team.add_matchup(random_away_team)
                        print(f"Matchup {j + 1}: {random_away_team.get_name()} @ {random_home_team.get_name()}")
                        break
            print("--------------------------------------------------------------------------")
        else:
            available_teams = teams[:]

            print(f"WEEK {i + 1} (RIVALRY WEEK):")
            for j in range(int(num_teams / 2)):
                random_team = random.choice(available_teams)
                random_team_opponent = random_team.get_rivalry_matchup()
                available_teams.remove(random_team)
                available_teams.remove(random_team_opponent)

                if not random_team.is_rivalry_matchup_home():
                    print(f"Matchup {j + 1}: {random_team_opponent.get_name()} @ {random_team.get_name()}")
                else:
                    print(f"Matchup {j + 1}: {random_team.get_name()} @ {random_team_opponent.get_name()}")
            print("--------------------------------------------------------------------------")
if __name__ == "__main__":
    __main__()