class Team:
    """Represents a team that plays against other teams.

    This class models a team that plays within the round-robin schedule
    that is generated from this program.

    Attributes:
        name (str): The name of the team.
        rivalry_matchup_home (bool): If the team's rivalry game is at home or not.
        rivalry_matchup (Team): A team the team plays against in their rivalry game.
        matchups (list[Team]): A list of team's the team will play.
    """
    def __init__(self, name):
        """Initializes the Team instance.

        Args:
            name (str): The name of the team.
            rivalry_matchup_home (bool): If the team's rivalry game is at home or not.
            rivalry_matchup (Team): A team the team plays against in their rivalry game.
            matchups (list[Team]): A list of team's the team will play.
        """
        self.name = name
        self.rivalry_matchup_home = False
        self.rivalry_matchup = None
        self.matchups = []

    def get_name(self):
        """Gets the name of the team.

        Returns:
            str: The name of the team.
        """
        return self.name

    def get_rivalry_matchup(self):
        """Gets the rival team of the team.

        Returns:
            Team: The rival team of the team.
        """
        return self.rivalry_matchup

    def is_rivalry_matchup_home(self):
        """Gets if the team is at home for their rivalry matchup.

        Returns:
            bool: The value determining if the team is at home for their rivalry matchup.
        """
        return self.rivalry_matchup_home

    def set_rivalry_matchup_home(self):
        """Sets the team at home for their rivalry matchup."""
        self.rivalry_matchup_home = True

    def set_rivalry_matchup(self, opponent):
        """Sets the rival team for the team.

        Args:
            opponent: The rival team of the team.
        """
        self.rivalry_matchup = opponent

    def add_matchup(self, opponent):
        """Adds a matchup of an opponent for the team.

        Args:
            opponent: The other team that matches up with the team.
        """
        self.matchups.append(opponent)

    def has_matchup(self, opponent):
        """Checks if the team has a matchup with an opponent.

        Args:
            opponent: The other team that possibly has a matchup with the team.

        Returns:
            bool: The value determining if the team has a matchup with an opponent.
        """
        for old_opponent in self.matchups:
            if opponent == old_opponent:
                return True
        return False

def get_team_by_name(team_name, team_list):
    """Gets a team from a list of teams given the name of the team to search for.

    Args:
        team_name: The name of the team to search for.
        team_list: The list of teams to search within.

    Returns:
        Team: The team searched for (returns None if no team is found).
    """
    for team in team_list:
        if team.get_name().lower() == team_name.lower():
            return team
    return None