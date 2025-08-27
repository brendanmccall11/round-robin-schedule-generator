import random

def schedule_team(schedule_matrix, teams, team, team_index):
    available_teams = teams[:]
    available_teams.remove(team)

    for opponent in range(len(schedule_matrix[team_index])):
        random_opponent = random.choice(available_teams)
        schedule_matrix[team_index][opponent] = random_opponent
        available_teams.remove(random_opponent)


def __main__():
    teams = []
    
    num_teams = input("Enter number of teams: ")

    for i in range(int(num_teams)):
        user_input = input(f"Enter team {i+1}: ")
        teams.append(user_input)

    num_games_per_team = input("Input number of games per team: ")

    schedule_matrix = [['.' for _ in range(int(num_games_per_team))] for _ in range(int(num_teams))]

    for team_index in range(len(teams)):
        schedule_team(schedule_matrix, teams, teams[team_index], team_index)

    for rows in schedule_matrix:
        print(rows)

if __name__ == "__main__":
    __main__()