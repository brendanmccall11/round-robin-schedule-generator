import random

class Team:
    def __init__(self, name):
        self.name = name
        self.matchups = []

    def get_matchups(self):
        return self.matchups

    def add_matchup(self, opponent):
        self.matchups.append(opponent)

def schedule_teams(teams, team):
    #random_team = random.choice(teams)
    available_teams = teams[:]
    available_teams.remove(team)
    num_matchups = len(available_teams)

    for i in range(num_matchups):
        random_opponent = random.choice(available_teams)
        team.add_matchup(random_opponent)
        available_teams.remove(random_opponent)


def __main__():
    fantasy_teams = []

    for i in range(8):
        user_input = input(f"Enter team {i+1}: ")
        new_team = Team(user_input)
        fantasy_teams.append(new_team)

    schedule_teams(fantasy_teams, fantasy_teams[0])
    matchups = fantasy_teams[0].get_matchups()
    for i in range(len(matchups)):
       print(f"Matchup {i+1}: " + matchups[i].name)

    # print(fantasy_teams)

if __name__ == "__main__":
    __main__()