import random

class Team:
    def __init__(self, name):
        self.name = name
        self.matchups = []

    def get_name(self):
        return self.name

    def get_matchups(self):
        return self.matchups

    def add_matchup(self, opponent):
        self.matchups.append(opponent)

    def has_matchup(self, opponent):
        for old_opponent in self.matchups:
            if opponent == old_opponent:
                return True
        return False

def __main__():
    teams = []

    num_teams = int(input("Enter number of teams: "))
    num_weeks = num_teams - 1

    for i in range(num_teams):
        user_team = input(f"Enter team {i+1}: ")
        new_team = Team(user_team)
        teams.append(new_team)

    for i in range(num_weeks):
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
        print("----------------------------------")

if __name__ == "__main__":
    __main__()